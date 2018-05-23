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

explorer = EpsGreedy(num_actions=env_input['NUM_ACTIONS'],
    eps=config.EPS_START, eps_min=config.EPS_MIN,
        decay=config.DECAY)

agent = get_agent(agent_input, env_input)

replay = ReplayBuffer()

writer = EpisodeWriter(config.resultsDir+'/'+env_input['ENV_NAME'],
    env_input['ENV_NAME'])

actor  = ActorThread(agent, env, explorer, replay,
    writer, config)
actor.start()

learner = LearnerThread(agent, replay, config)
learner.start()
