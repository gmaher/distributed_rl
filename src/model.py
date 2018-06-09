class Model(object):
    def __init__(self):
        pass
    def predict(self,s):
        pass
    def set_params(self,params):
        pass

class TabularQFunction(Model):
    def __init__(self, q_init):
        self.q = q_init.copy()

    def predict(self, s):
        return np.argmax(self.q[s])

    def set_params(self, q):
        self.q = q.copy()
