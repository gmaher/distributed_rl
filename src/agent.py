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
