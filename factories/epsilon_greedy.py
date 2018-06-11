from src.exploration      import EpsilonGreedy
from src.optimizer        import QLearning
from src.model            import TabularQFunction
from src.parameter_server import ParameterServer
from src.replay_buffer    import ReplayBuffer, UniformReplayBuffer

############################################
# Setup
############################################
methods = {}

class EpsGreedyAgent(object):
    def __init__(self, model, explorer, param_server):
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

def setup(input_file, config):
    NUM_STATES  = input_file['STATE_SIZE' ][0]
    NUM_ACTIONS = input_file['NUM_ACTIONS']

    q_learning = QLearning(input_file['Q_INIT'], input_file['Q_STD'],
        NUM_STATES, NUM_ACTIONS,
        config.LEARNING_RATE, config.DISCOUNT)

    param_server = ParameterServer(q_learning)

    if input_file['REPLAY_TYPE'] == "standard":
        replay_buffer = ReplayBuffer()

    elif input_file['REPLAY_TYPE'] == 'uniform':
        replay_buffer = UniformReplayBuffer()

    else:
        raise RuntimeError("Unrecognized replay type {}".format(input_file['REPLAY_TYPE']))

    def agent():
        q_function = TabularQFunction( q_learning.get_params() )

        explorer   = EpsilonGreedy(NUM_ACTIONS, config.EPS_START, config.EPS_MIN,
            config.DECAY)

        return EpsGreedyAgent(q_function, explorer, param_server)

    def learner():
        return q_learning

    def replay():
        return replay_buffer

    methods['get_agent']   = agent
    methods['get_learner'] = learner
    methods['get_replay']  = replay
