import argparse

from config import config
from src.util import read_json
from src.environment import get_environment
from src.exploration import EpsGreedy
from src.agent import TabularQFunction
from src.replay_buffer import ReplayBuffer
from src.actor import ActorThread
from src.learner import LearnerThread

parser = argparse.ArgumentParser()
parser.add_argument('-env', type=str)

args = parser.parse_args()

#######################################
# Read inputs
#######################################
env_input = read_json(args.env)

#######################################
# Set up simulation
#######################################
env = get_environment(env_input)

explorer = EpsGreedy(num_actions=env_input['NUM_ACTIONS'],
    eps=config.EPS_START, eps_min=config.EPS_MIN,
        decay=config.DECAY)

agent = TabularQFunction(state_size=env_input['STATE_SIZE'][0],
    num_actions=env_input['NUM_ACTIONS'],
    mu_init=config.Q_INIT, std_init=config.Q_STD)


replay = ReplayBuffer()

actor  = ActorThread(agent, env, explorer, replay, config)
actor.start()

learner = LearnerThread(agent, replay, config)
learner.start()
