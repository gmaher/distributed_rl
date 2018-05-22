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
NUM_EPISODES  = 60000
NUM_STEPS     = 30
LEARNING_RATE = 1e-2
RENDER_FREQUENCY = 100
PRINT_FREQUENCY  = 100
RENDER = False
WRITE_FREQUENCY = 100
SLEEP_TIME      = 0.001

EPS_START = 1.0
EPS_MIN   = 0.01
DECAY     = 0.9997

Q_INIT    = 0.5,
Q_STD     = 1e-2
