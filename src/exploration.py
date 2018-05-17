import numpy as np

class EpsGreedy(object):
    def __init__(self,num_actions,eps=0.5,eps_min=0.05,decay=0.995):
        self.num_actions = num_actions
        self.eps         = eps
        self.eps_mint    = eps_min
        self.decay       = decay

    def explore(self, action):
        r = np.random.rand()
        if r > self.eps:
            return action
        else:
            return np.random.randint(self.num_actions)

    def update(self):
        if self.eps > self.eps_min:
            self.eps *= self.decay
