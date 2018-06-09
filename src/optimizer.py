import numpy as np

class Optimizer(object):
    def __init__(self):
        pass
    def update(self,batch):
        pass
    def get_params(self):
        pass

class QLearning(Optimizer):
    def __init__(self, mu_int, std_init, num_states, num_actions,
        learning_rate=1e-3, discount=0.99):

        self.num_state     = num_states
        self.num_actions   = num_actions
        self.learning_rate = learning_rate
        self.discount      = discount
        self.q = np.random.rand(num_states, num_actions)*std_init + mu_init

    def update(self, batch):
        batch_size = len(batch)

        for i in range(batch_size):
            s     = batch[0][i]
            a     = batch[1][i]
            r     = batch[2][i]
            ss    = batch[3][i]
            done  = batch[4][i]

            new_q = reward + int(not done)*discount*np.max(self.q[ss])

            self.q[s,a] =\
             (1-learning_rate)*self.q[s, a]+learning_rate*new_q

    def get_params(self):
        return self.q.copy()
