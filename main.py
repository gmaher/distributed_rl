import argparse

from config import config
from src.util import read_json
from src.environment import get_environment
from src.exploration import EpsGreedy
from src.agent import TabularQFunction
from src.replay_buffer import ReplayBuffer

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

for ep in range(config.NUM_EPISODES):
    s = env.reset()

    for t in range(config.NUM_STEPS):
        if (ep%config.RENDER_FREQUENCY == 0) and config.RENDER:
            env.render()

        a = agent.act(s)

        a = explorer.explore(a)

        ss,r,done,info = env.step(a)

        replay.add((s,a,r,ss,done))

        if len(replay.tuples) > 1:
            tup = replay.get(batch_size=1)

            agent.update(tup[0][0], tup[1][0], tup[2][0],
                tup[3][0], config.LEARNING_RATE)

        s = ss

        if done:
            break

    print ("episode {}: final state {}, reward {}".format(ep, s, r))


    explorer.update()
