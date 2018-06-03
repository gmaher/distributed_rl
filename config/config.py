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
BATCH_SIZE    = 16
NUM_EPISODES  = 100000
NUM_STEPS     = 50
LEARNING_RATE = 1e-1
RENDER_FREQUENCY = 1000
PRINT_FREQUENCY  = 1000
RENDER = True
WRITE_FREQUENCY = 10
SLEEP_TIME      = 0.001
SLEEP_TIME_LEARNER      = 0.001
DISCOUNT = 0.99

EPS_START = 0.5
EPS_MIN   = 0.01
DECAY     = 0.999
