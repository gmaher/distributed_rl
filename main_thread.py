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

# explorer = EpsGreedy(num_actions=env_input['NUM_ACTIONS'],
#     eps=config.EPS_START, eps_min=config.EPS_MIN,
#         decay=config.DECAY)

explorer = None

actor_agent = get_agent(agent_input, env_input)
print(actor_agent.q)
learner_agent = get_agent(agent_input, env_input)

parameter_server = ParameterServer(learner_agent)

replay = ReplayBuffer()

writer = EpisodeWriter(config.resultsDir+'/'+env_input['ENV_NAME'],
    env_input['ENV_NAME'])

actor  = ActorThread(actor_agent, env, replay, parameter_server,
    writer, config, explorer)
actor.start()

learner = LearnerThread(learner_agent, replay, config)
learner.start()
