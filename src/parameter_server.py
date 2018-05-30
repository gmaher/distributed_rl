class ParameterServer(object):
    def __init__(self, learner_agent):
        self.learner_agent = learner_agent

    def getParams(self):
        return self.learner_agent.sampleParams()
