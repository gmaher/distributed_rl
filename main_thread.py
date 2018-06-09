import argparse
import time
from config import config
from src.util import read_json
from src.environment import get_environment
from src.exploration import EpsGreedy
from src.agent_factory import get_agent
from src.replay_buffer import ReplayBuffer
from src.actor import ActorThread
from src.learner import LearnerThread
from src.writer import EpisodeWriter
from src.parameter_server import ParameterServer
import numpy as np
import importlib

parser = argparse.ArgumentParser()
parser.add_argument('-env', type=str)
parser.add_argument('-agent', type=str)
parser.add_argument('-factory', type=str)
parser.add_argument('--n_agents', type=int, default=1)
args = parser.parse_args()

#######################################
# Read inputs
#######################################
env_input   = read_json(args.env)
agent_input = read_json(args.agent)

#######################################
# build agent
#######################################
factory = importlib.import_module(args.factory)

learner = factory.get_learner(agent_input, env_input)

replay = ReplayBuffer(max_size=config.REPLAY_SIZE)

case_id = str(np.random.randint(10000000))
print("Starting experiment {}".format(case_id))
for i in range(args.n_agents):
    id_ = str(i)

    env = get_environment(env_input)

    agent = factory.get_agent(agent_input, env_input)

    writer = EpisodeWriter(config.resultsDir, env_name=env_input['ENV_NAME'],
        agent_name=agent_input["TYPE"]+case_id, id_=id_)

    actor_thread  = ActorThread(agent, env, replay,
        writer, config, name=id_)

    actor.daemon = True

    actor.start()

learner_thread = LearnerThread(learner, replay, config, name="learner")
learner_thread.daemon = True
learner_thread.start()

while True:
    print("checking if done: {}".format(actor_thread.out_count))
    if actor_thread.out_count >= config.NUM_EPISODES-1:
        time.sleep(10)
        exit()
    time.sleep(10)
