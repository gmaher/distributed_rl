from src.optimizer        import NaiveThompsonQ
from src.model            import TabularQFunction
from src.parameter_server import ParameterServer

############################################
# Setup
############################################
methods = {}

class ThompsonAgent(object):
    def __init__(self, model, param_server):
        self.model        = model
        self.param_server = param_server

    def finish_episode(self):
        params = self.param_server.get_params()

        self.model.set_params(params)

    def act(self, s):
        return self.model.predict(s)

def setup(agent_params, env_params, config):
    NUM_STATES  = env_params['STATE_SIZE' ][0]
    NUM_ACTIONS = env_params['NUM_ACTIONS']

    thompson = NaiveThompsonQ(agent_params['Q_INIT'], agent_params['Q_STD'],
        NUM_STATES, NUM_ACTIONS,
        agent_params['STD_EXPLORE'], config.LEARNING_RATE, config.DISCOUNT)

    param_server = ParameterServer(thompson)

    def agent():
        q_function = TabularQFunction( thompson.get_params() )

        return ThompsonAgent(q_function, param_server)

    def learner():
        return thompson

    methods['get_agent']   = agent
    methods['get_learner'] = learner
