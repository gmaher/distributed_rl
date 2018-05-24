from src.agent import TabularQFunction
from src.agent import PreprocessedTableQFunction
from src.preprocessor import TablePreprocessor
import numpy as np

def get_agent(agent_params, env_params):
    if agent_params['TYPE'] == 'TabularQFunction':
        return get_tabular_q(agent_params, env_params)
    elif agent_params['TYPE'] == 'PreprocessedTableQFunction':
        return get_preprocessed_q(agent_params, env_params)


def get_tabular_q(agent_params, env_params):
    return TabularQFunction(state_size=env_params['STATE_SIZE'][0],
        num_actions=env_params['NUM_ACTIONS'],
        mu_init=agent_params['Q_INIT'],
        std_init=agent_params['Q_STD'])

def get_preprocessed_q(agent_params, env_params):
    ranges = np.array(env_params['STATE_RANGES'])
    bins   = agent_params['BINS']

    preprocessor = TablePreprocessor(ranges, bins)

    agent = PreprocessedTableQFunction(preprocessor,
        num_actions=env_params['NUM_ACTIONS'],
        mu_init=agent_params['Q_INIT'],
        std_init=agent_params['Q_STD'])

    return agent
