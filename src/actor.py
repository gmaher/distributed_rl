import numpy as np
import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG,
    format='(%(threadName)-9s) %(message)s',)

class ActorThread(threading.Thread):
    def __init__(self, agent, env, replay_buffer, parameter_server,
        writer, config, explorer=None, group=None, target=None, name="actor",
        args=(), kwargs=None, verbose=None):

        super(ActorThread,self).__init__()

        self.group  = group
        self.target = target
        self.name   = name

        self.agent            = agent
        self.env              = env
        self.explorer         = explorer
        self.replay_buffer    = replay_buffer
        self.parameter_server = parameter_server
        self.writer           = writer
        self.config           = config
        self.out_count        = 0
        #self.setDaemon(True)

    def run(self):
        count = -1
        for i in range(self.config.NUM_EPISODES):
            count+=1

            if count%self.config.WRITE_FREQUENCY == 0:
                self.writer.make_episode_dir(count)

            s = self.env.reset()

            for t in range(self.config.NUM_STEPS):

                if (count%self.config.RENDER_FREQUENCY == 0)\
                and self.config.RENDER:
                    self.env.render()
                    time.sleep(1.0/60)

                a = self.agent.act(s)

                if not self.explorer == None:
                    a = self.explorer.explore(a)

                ss,r,done,info = self.env.step(a)

                self.replay_buffer.add((s,a,r,ss,done))

                if count%self.config.WRITE_FREQUENCY == 0:
                    self.writer.write(count, t, s, a, r, ss, done)

                s = ss

                if done:
                    a = self.agent.act(ss)
                    self.replay_buffer.add((ss,a,r,ss,done))
                    break

            if count%self.config.PRINT_FREQUENCY == 0:
                logging.debug("episode {}: final state {}, reward {}".format(count, s, r))

            if not self.explorer == None:
                self.explorer.update()

            new_params = self.parameter_server.getParams()

            self.agent.setParams(new_params)
            self.out_count = count
            time.sleep(random.random()*self.config.SLEEP_TIME)

        return
