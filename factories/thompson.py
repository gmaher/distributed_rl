from src.optimizer        import NaiveThompsonQ, ThompsonQMax
from src.model            import TabularQFunction
from src.parameter_server import ParameterServer
from src.replay_buffer    import ReplayBuffer, UniformReplayBuffer
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

def setup(input_file, config):
    NUM_STATES  = input_file['STATE_SIZE' ][0]
    NUM_ACTIONS = input_file['NUM_ACTIONS']

    thompson = ThompsonQMax(input_file['Q_INIT'], input_file['Q_STD'],
        NUM_STATES, NUM_ACTIONS,
        input_file['STD_EXPLORE'], config.LEARNING_RATE, config.DISCOUNT)

    param_server = ParameterServer(thompson)

    if input_file['REPLAY_TYPE'] == "standard":
        replay_buffer = ReplayBuffer()

    elif input_file['REPLAY_TYPE'] == 'uniform':
        replay_buffer = UniformReplayBuffer()

    else:
        raise RuntimeError("Unrecognized replay type {}".format(input_file['REPLAY_TYPE']))


    def agent():
        q_function = TabularQFunction( thompson.get_params() )

        return ThompsonAgent(q_function, param_server)

    def learner():
        return thompson

    def replay():
        return replay_buffer

    methods['get_agent']   = agent
    methods['get_learner'] = learner
    methods['get_replay']  = replay
