import numpy as np
import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG,
    format='(%(threadName)-9s) %(message)s',)

class LearnerThread(threading.Thread):
    def __init__(self, agent, replay_buffer, config, group=None, target=None, name="actor", args=(), kwargs=None, verbose=None):
        super(LearnerThread,self).__init__()

        self.group  = group
        self.target = target
        self.name   = name

        self.agent         = agent
        self.replay_buffer = replay_buffer
        self.config        = config

    def run(self):
        count = 0
        while True:
            count+=1

            if len(self.replay_buffer.tuples) > self.config.BATCH_SIZE:
                tuples = self.replay_buffer.get(batch_size=self.config.BATCH_SIZE)

                for i in range(self.config.BATCH_SIZE):
                    s = tuples[0][i]
                    a = tuples[1][i]
                    r = tuples[2][i]
                    ss = tuples[3][i]
                    done = tuples[4][i]

                    self.agent.update(s,a,r,ss, done, self.config.LEARNING_RATE,
                            self.config.DISCOUNT)

            if count%self.config.PRINT_FREQUENCY == 0:
                logging.debug("training iteration {}".format(count))

                logging.debug("min Q {}, max Q {}".format(np.amin(self.agent.q),np.amax(self.agent.q)))

            time.sleep(random.random()*self.config.SLEEP_TIME_LEARNER)

        return
