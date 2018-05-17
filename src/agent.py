import numpy as np

class TabularQFunction:
    def __init__(self, state_size, num_actions,
        mu_init=10, std_init=1e-2):

        self.state_size  = state_size
        self.num_actions = num_actions

        self.q = np.random.randn(state_size,
            num_actions)*std_init + mu_init

    def act(self, state):
        return np.argmax(self.q[state])
