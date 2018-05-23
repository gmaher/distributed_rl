from src.agent import TabularQFunction

def get_agent(agent_params, env_params):
    if agent_params['TYPE'] == 'TabularQFunction':
        return get_tabular_q(agent_params, env_params)

def get_tabular_q(agent_params, env_params):
    return TabularQFunction(state_size=env_params['STATE_SIZE'][0],
        num_actions=env_params['NUM_ACTIONS'],
        mu_init=agent_params['Q_INIT'],
        std_init=agent_params['Q_STD'])
