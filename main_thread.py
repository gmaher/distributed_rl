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

parser = argparse.ArgumentParser()
parser.add_argument('-env', type=str)
parser.add_argument('-agent', type=str)
parser.add_argument('--n_agents', type=int, default=1)
args = parser.parse_args()

#######################################
# Read inputs
#######################################
env_input   = read_json(args.env)
agent_input = read_json(args.agent)

#######################################
# Set up simulation
#######################################
if "EXPLORER" in agent_input and agent_input['EXPLORER'] == 'EPS_GREEDY':

    explorer = EpsGreedy(num_actions=env_input['NUM_ACTIONS'],
        eps=config.EPS_START, eps_min=config.EPS_MIN,
            decay=config.DECAY)

else:
    explorer = None

learner_agent = get_agent(agent_input, env_input)
print(learner_agent.q)
parameter_server = ParameterServer(learner_agent)

replay = ReplayBuffer(max_size=config.REPLAY_SIZE)

case_id = str(np.random.randint(10000000))
print("Starting experiment {}".format(case_id))
for i in range(args.n_agents):
    id_ = str(i)

    env = get_environment(env_input)

    actor_agent = get_agent(agent_input, env_input)

    writer = EpisodeWriter(config.resultsDir, env_name=env_input['ENV_NAME'],
        agent_name=agent_input["TYPE"]+case_id, id_=id_)

    actor  = ActorThread(actor_agent, env, replay, parameter_server,
        writer, config, explorer, name=id_)
    actor.daemon = True

    actor.start()

learner = LearnerThread(learner_agent, replay, config, name="learner")
learner.daemon = True
learner.start()

while True:
    print("checking if done: {}".format(actor.out_count))
    if actor.out_count >= config.NUM_EPISODES-1: exit()
    time.sleep(10)
