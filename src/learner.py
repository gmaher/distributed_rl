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
        #self.setDaemon(True)

    def run(self):
        count = 0
        while True:
            count+=1

            if len(self.replay_buffer.tuples) > 1:
                tup = self.replay_buffer.get(batch_size=1)

                self.agent.update(tup[0][0], tup[1][0], tup[2][0],
                    tup[3][0], self.config.LEARNING_RATE)

            logging.debug("training iteration {}".format(count))

            time.sleep(random.random())

        return
