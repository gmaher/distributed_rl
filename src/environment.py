import importlib
import gym

def get_environment(params):
    if params['PROVIDER'] == 'gym':
        return get_gym_environment(params['ENV_NAME'])
        
def get_gym_environment(name):
    return gym.make(name)
