import numpy as np

class ReplayBuffer:
    def __init__(self, max_size=10000):
        self.tuples = []
        self.max_size = max_size
        self.index = 0

    def add(self, tup):
        if self.index >= self.max_size:
            self.index = np.random.randint(self.max_size)
            self.tuples[self.index] = tup
        else:
            self.tuples.append(tup)
            self.index += 1

    def get(self, batch_size=16):
        indices = np.random.randint(self.index, size=batch_size)

        tups = [self.tuples[i] for i in indices]

        s    = np.array([t[0] for t in tups])
        a    = np.array([t[1] for t in tups])
        r    = np.array([t[2] for t in tups])
        ss   = np.array([t[3] for t in tups])
        done = np.array([t[4] for t in tups])
        return (s,a,r,ss,done)
