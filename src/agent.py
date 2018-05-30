import numpy as np
from src.preprocessor import TablePreprocessor

class TabularQFunction:
    def __init__(self, state_size, num_actions,
        mu_init=10, std_init=1e-2):

        self.state_size  = state_size
        self.num_actions = num_actions

        self.q = np.random.randn(state_size,
            num_actions)*std_init + mu_init

    def act(self, state):
        return np.argmax(self.q[state])

    def update(self, state, action, reward, new_state, learning_rate, discount):
        new_q = reward + discount*np.max(self.q[new_state])

        self.q[state,action] =\
         (1-learning_rate)*self.q[state,action]+learning_rate*new_q

    def sampleParams(self):
        return self.q.copy()

    def setParams(self,q):
        self.q = q

class ThompsonTabularQFunction(TabularQFunction):
    def __init__(self,state_size, num_actions,
        mu_init=10, std_init=1e-2, std_explore=0.5):

        super(ThompsonTabularQFunction,self).__init__(state_size, num_actions,
            mu_init=mu_init, std_init=std_init)

        self.std_explore = std_explore

    def sampleParams(self):
        s = self.q.shape
        return self.q.copy() + self.std_explore*np.random.randn(*s)

class PreprocessedTableQFunction:
    def __init__(self, preprocessor, num_actions, mu_init, std_init):
        self.preprocessor = preprocessor
        self.num_states   = self.preprocessor.num_states
        self.num_actions  = num_actions

        self.q = np.random.randn(self.num_states,
            self.num_actions)*std_init + mu_init

    def act(self, state):
        index  = self.preprocessor.preprocess(state)
        return np.argmax(self.q[index,:])

    def update(self, state, action, reward, new_state, learning_rate, discount):
        index_s = self.preprocessor.preprocess(state)
        index_ss = self.preprocessor.preprocess(new_state)

        new_q = reward + discount*np.max(self.q[index_ss])

        self.q[index_s,action] =\
         (1-learning_rate)*self.q[index_s,action]+learning_rate*new_q

    def sampleParams(self):
        return self.q.copy()

    def setParams(self, q):
        self.q = q

class ThompsonPreprocessedQFunction(PreprocessedTableQFunction):
    def __init__(self,preprocessor, num_actions,
        mu_init=10, std_init=1e-2, std_explore=0.5):

        super(ThompsonPreprocessedQFunction,self).__init__(preprocessor, num_actions,
            mu_init=10, std_init=1e-2)

        self.std_explore = std_explore

    def sampleParams(self):
        s = self.q.shape
        return self.q.copy() + self.std_explore*np.random.randn(*s)
