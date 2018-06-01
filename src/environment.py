import importlib
import gym

def get_environment(params):
    if params['PROVIDER'] == 'GYM':
        return get_gym_environment(params)

def get_gym_environment(params):
    env = gym.make(params['ENV_NAME'])
    return env.env.__class__(**params['ENV_PARAMS'])
