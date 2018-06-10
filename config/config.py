import os

#######################################################
# Directories
#######################################################
configDir = os.path.dirname(os.path.realpath(__file__))

srcDir = os.path.abspath(configDir+'/..')

dataDir = srcDir+'/data'

resultsDir = srcDir+'/results'
#######################################################
# Simulation Inputs
#######################################################
BATCH_SIZE    = 4
NUM_EPISODES  = 50000
NUM_STEPS     = 30
LEARNING_RATE = 1e-2
RENDER_FREQUENCY = 2000
PRINT_FREQUENCY  = 1000
RENDER = False
WRITE_FREQUENCY = 1000
SLEEP_TIME      = 0.001
SLEEP_TIME_LEARNER      = 0.001
DISCOUNT = 0.99
REPLAY_SIZE = 1000

EPS_START = 1.0
EPS_MIN   = 0.01
DECAY     = 0.999
