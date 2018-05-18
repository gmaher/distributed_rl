import argparse

from config import config
from src.util import read_json
from src.environment import get_environment
from src.exploration import EpsGreedy
from src.agent import TabularQFunction

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

for ep in range(config.NUM_EPISODES):
    s = env.reset()

    for t in range(config.NUM_STEPS):
        if ep%config.RENDER_FREQUENCY == 0:
            env.render()

        a = agent.act(s)

        a = explorer.explore(a)

        ss,r,done,info = env.step(a)

        agent.update(s, a, r, ss, config.LEARNING_RATE)

        s = ss

        if done:
            print ("episode {}: final state {}, reward {}".format(ep, s, r))
            break

    explorer.update()
