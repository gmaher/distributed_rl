import numpy as np

class TablePreprocessor(object):
    def __init__(self, ranges, N=20):
        self.ranges          = ranges
        self.state_dimension = ranges.shape[0]
        self.N               = N
        self.num_states      = self.N**self.state_dimension

    def preprocess(self, s):
        binned = (1.0*s-self.ranges[:,0])/(self.ranges[:,1]-self.ranges[:,0])
        binned = binned*self.N
        binned = np.ceil(binned).astype(int)-(binned>0).astype(int)
        for i in range(self.state_dimension):
            if binned[i] > self.N-1:
                binned[i] = self.N-1
            if binned[i] < 0:
                binned[i] = 0

        n = 0
        for i in range(self.state_dimension):
            n += binned[i]*( self.N**i )

        return n

    def deprocess(self, n):
        s = np.zeros((self.state_dimension))
        t = n

        for i in range(self.state_dimension-1,-1,-1):
            r = int(np.floor( (1.0*t)/(self.N**i) ))

            s[i] = (1.0*r)/self.N*(self.ranges[i,1]-self.ranges[i,0])+self.ranges[i,0]
            t = t-r*(self.N**i)

        return s
