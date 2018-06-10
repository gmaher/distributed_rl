import numpy as np

class Optimizer(object):
    def __init__(self):
        pass
    def update(self,batch):
        pass
    def get_params(self):
        pass

class QLearning(Optimizer):
    def __init__(self, mu_init, std_init, num_states, num_actions,
        learning_rate=1e-3, discount=0.99):

        self.num_state     = num_states
        self.num_actions   = num_actions
        self.learning_rate = learning_rate
        self.discount      = discount
        self.q = np.random.rand(num_states, num_actions)*std_init + mu_init

    def update(self, batch):
        batch_size = batch[0].shape[0]

        for i in range(batch_size):
            s     = batch[0][i]
            a     = batch[1][i]
            r     = batch[2][i]
            ss    = batch[3][i]
            done  = batch[4][i]

            new_q = r + int(not done)*self.discount*np.max(self.q[ss])

            self.q[s,a] =\
             (1-self.learning_rate)*self.q[s, a]+\
                self.learning_rate*new_q

    def get_params(self):
        return self.q.copy()

    def log(self):
        return "QLearning: q_min = {}, q_max = {}".format(np.amin(self.q), np.amax(self.q))

class NaiveThompsonQ(Optimizer):
    def __init__(self, mu_init, std_init, num_states, num_actions,
        std_explore, learning_rate=1e-3, discount=0.99):

        self.num_states    = num_states
        self.num_actions   = num_actions
        self.learning_rate = learning_rate
        self.discount      = discount

        self.q = np.random.rand(num_states, num_actions)*std_init + mu_init

        self.std_explore = np.ones(self.q.shape)*std_explore

    def update(self, batch):
        batch_size = batch[0].shape[0]

        for i in range(batch_size):
            s     = batch[0][i]
            a     = batch[1][i]
            r     = batch[2][i]
            ss    = batch[3][i]
            done  = batch[4][i]

            new_q = r + int(not done)*self.discount*np.max(self.q[ss])

            self.q[s,a] =\
             (1-self.learning_rate)*self.q[s, a]+\
                self.learning_rate*new_q

            self.std_explore[s,a] *= (1-self.learning_rate)

    def get_params(self):
        return self.q.copy()+np.random.randn(self.num_states,\
            self.num_actions)*self.std_explore

    def log(self):
        return "QLearning: q_min = {}, q_max = {}\n std min = {},\
            std max ={}".format(np.amin(self.q), np.amax(self.q),
                np.amin(self.std_explore), np.amax(self.std_explore)
                )

class ThompsonQMax(Optimizer):
    def __init__(self, mu_init, std_init, num_states, num_actions,
        std_explore, learning_rate=1e-3, discount=0.99):

        self.num_states    = num_states
        self.num_actions   = num_actions
        self.learning_rate = learning_rate
        self.discount      = discount

        self.q = np.random.rand(num_states, num_actions)*std_init + mu_init

        self.std_explore = np.ones(self.q.shape)*std_explore

        self.counts = np.zeros((num_states,num_actions))

        self.Qmax = np.amax(self.q)
        self.Qmin = np.amin(self.q)

    def update(self, batch):
        batch_size = batch[0].shape[0]

        for i in range(batch_size):
            s     = batch[0][i]
            a     = batch[1][i]
            r     = batch[2][i]
            ss    = batch[3][i]
            done  = batch[4][i]

            new_q = r + int(not done)*self.discount*np.max(self.q[ss])

            self.std_explore[s,a] =\
                np.sqrt((1-self.learning_rate)*self.std_explore[s,a]**2 +\
                    self.learning_rate*(new_q-self.q[s,a])**2)

            self.q[s,a] =\
             (1-self.learning_rate)*self.q[s, a]+\
                self.learning_rate*new_q

            self.counts[s,a] += 1

        self.Qmax = np.amax(self.q)
        self.Qmin = np.amin(self.q)

    def get_params(self):
        std_bound = 0.5*(self.Qmax-self.Qmin)
        c_1 = (self.learning_rate**4)**self.counts

        final_std = c_1*std_bound + (1-c_1)*self.std_explore

        return self.q.copy()+np.random.randn(self.num_states,\
            self.num_actions)*final_std

    def log(self):
        return "ThompsonQMax: q_min = {}, q_max = {}\n std min = {},\
            std max ={}\n counts min ={} counts max =\n{}"\
                .format(np.amin(self.q), np.amax(self.q),
                np.amin(self.std_explore), np.amax(self.std_explore),
                np.amin(self.counts), self.counts
                )
