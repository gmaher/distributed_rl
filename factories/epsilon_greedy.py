from src.exploration import EpsilonGreedy
from src.optimizer   import QLearning
from src.model       import TabularQFunction
from src.parameter_server import ParameterServer

############################################
# Setup
############################################
global get_agent
global get_learner

class EpsGreedyAgent(object):
    def __init(self, model, explorer, param_server):
        self.model        = model
        self.explorer     = explorer
        self.param_server = param_server

    def finish_episode(self):
        self.explorer.update()

        params = self.param_server.get_params()

        self.model.set_params(params)

    def act(self, s):
        a = self.model.predict(s)
        return self.explorer.explore(a)

def setup(agent_params, env_params, config):

    NUM_STATES  = env_params['STATE_SIZE' ][0]
    NUM_ACTIONS = env_params['NUM_ACTIONS']

    q_learning = QLearning(agent_params['Q_INIT'], agent_params['Q_STD'],
        NUM_STATES, NUM_ACTIONS,
        config.LEARNING_RATE, config.DISCOUNT)

    param_server = ParameterServer(q_learning)

    def get_agent():
        q_function = TabularQFunction( q_learning.get_params() )

        explorer   = EpsilonGreedy(NUM_ACTIONS, config.EPS_START, config.EPS_MIN,
            config.DECAY)

        return EpsGreedyAgent(q_function, explorer, param_server)

    def get_learner():
        return q_learning
