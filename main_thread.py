import argparse
import time
from config import config
from src.util import read_json
from src.environment import get_environment
from src.replay_buffer import ReplayBuffer, UniformReplayBuffer
from src.actor import ActorThread
from src.learner import LearnerThread
from src.writer import EpisodeWriter
import numpy as np
import importlib

parser = argparse.ArgumentParser()
parser.add_argument('-input',type=str)
args = parser.parse_args()

#######################################
# Read inputs
#######################################
input_file   = read_json(args.input)

#######################################
# build agent
#######################################
factory = importlib.import_module(input_file['FACTORY'])
factory.setup(input_file, config)

learner = factory.methods['get_learner']()

replay = factory.methods['get_replay']()

for i in range(args.n_agents):
    id_ = str(i)

    env = get_environment(env_input)

    agent = factory.methods['get_agent']()

    writer = EpisodeWriter(input_file['output_dir'], id_=id_)

    actor_thread  = ActorThread(agent, env, replay,
        writer, config, name=id_)

    actor_thread.daemon = True

    actor_thread.start()

learner_thread = LearnerThread(learner, replay, config, name="learner")
learner_thread.daemon = True
learner_thread.start()

while True:
    print("checking if done: {}".format(actor_thread.out_count))
    if actor_thread.out_count >= config.NUM_EPISODES-1:
        time.sleep(10)
        exit()
    time.sleep(10)
