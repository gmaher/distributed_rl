import numpy as np
import random

class ReplayBuffer:
    def __init__(self, max_size=10000):
        self.tuples = []
        self.max_size = max_size
        self.index = 0
        self.count = 0

    def add(self, tup):
        if self.index >= self.max_size:
            index = np.random.randint(self.max_size)
            self.tuples[index] = tup
        else:
            self.tuples.append(tup)
            self.index += 1
            self.count += 1

    def get(self, batch_size=16):
        indices = np.random.randint(self.index, size=batch_size)

        tups = [self.tuples[i] for i in indices]

        s    = np.array([t[0] for t in tups])
        a    = np.array([t[1] for t in tups])
        r    = np.array([t[2] for t in tups])
        ss   = np.array([t[3] for t in tups])
        done = np.array([t[4] for t in tups])
        return (s,a,r,ss,done)

class UniformReplayBuffer:
    def __init__(self, max_size=10000):
        self.data = {}
        self.max_size = max_size
        self.indexes = {}
        self.count = 0

    def add(self, tup):
        key = (tup[0],tup[1])

        if key not in self.data:
            self.data[key] = []

        if len(self.data[key]) < self.max_size:
            self.data[key].append(tup)
            self.count += 1
            return

        index = np.random.randint(self.max_size)
        self.data[key][index] = tup
        return

    def get(self, batch_size=16):
        keys = random.choices(list(self.data.keys()), k=batch_size)

        tups = []
        for k in keys:
            t = random.choice(self.data[k])
            tups.append(t)

        s    = np.array([t[0] for t in tups])
        a    = np.array([t[1] for t in tups])
        r    = np.array([t[2] for t in tups])
        ss   = np.array([t[3] for t in tups])
        done = np.array([t[4] for t in tups])

        return (s,a,r,ss,done)
