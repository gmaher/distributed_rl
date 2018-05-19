import numpy as np
import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG,
    format='(%(threadName)-9s) %(message)s',)

class ActorThread(threading.Thread):
    def __init__(self, agent, env, explorer, replay_buffer, config, group=None, target=None, name="actor", args=(), kwargs=None, verbose=None):
        super(ActorThread,self).__init__()

        self.group  = group
        self.target = target
        self.name   = name

        self.agent         = agent
        self.env           = env
        self.explorer      = explorer
        self.replay_buffer = replay_buffer
        self.config        = config
        #self.setDaemon(True)

    def run(self):
        count = 0
        while True:
            count+=1

            s = self.env.reset()

            for t in range(self.config.NUM_STEPS):

                if (count%self.config.RENDER_FREQUENCY == 0)\
                and self.config.RENDER:
                    self.env.render()

                a = self.agent.act(s)

                a = self.explorer.explore(a)

                ss,r,done,info = self.env.step(a)

                self.replay_buffer.add((s,a,r,ss,done))

                s = ss

                if done:
                    break

            logging.debug("episode {}: final state {}, reward {}".format(count, s, r))

            self.explorer.update()

            time.sleep(random.random())

        return
