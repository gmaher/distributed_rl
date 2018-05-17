import argparse

from config import config
from src.util import read_json
from src.environment import get_environment

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
