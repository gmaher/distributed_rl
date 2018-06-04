import argparse

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
env = get_environment(env_input)

if "EXPLORER" in agent_input and agent_input['EXPLORER'] == 'EPS_GREEDY':

    explorer = EpsGreedy(num_actions=env_input['NUM_ACTIONS'],
        eps=config.EPS_START, eps_min=config.EPS_MIN,
            decay=config.DECAY)

else:
    explorer = None

learner_agent = get_agent(agent_input, env_input)

parameter_server = ParameterServer(learner_agent)

replay = ReplayBuffer()

for i in range(args.n_agents):
    id_ = str(i)

    actor_agent = get_agent(agent_input, env_input)

    writer = EpisodeWriter(config.resultsDir, env_name=env_input['ENV_NAME'],
        agent_name=agent_input["TYPE"], id_=id_)

    actor  = ActorThread(actor_agent, env, replay, parameter_server,
        writer, config, explorer, name=id_)
    actor.start()

learner = LearnerThread(learner_agent, replay, config)
learner.start()
