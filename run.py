import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-env', type=str)
parser.add_argument('-agent', type=str)
parser.add_argument('--n_agents', type=int, default=1)
parser.add_argument('--trials', type=int, default=20)

args = parser.parse_args()

command = "py3 main_thread.py -env {} -agent {} --n_agents {}".format(
args.env, args.agent, args.n_agents
)

for i in range(args.trials):
    print(command)
    os.system(command)
