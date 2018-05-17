import os

#######################################################
# Directories
#######################################################
configDir = os.path.dirname(os.path.realpath(__file__))

srcDir = os.path.abspath(configDir+'/..')

dataDir = srcDir+'/data'

#######################################################
# Simulation Inputs
#######################################################
BATCH_SIZE    = 16
NUM_EPISODES  = 10000
NUM_STEPS     = 100
LEARNING_RATE = 1e-2

EPS_START = 0.75
EPS_MIN   = 0.05
DECAY     = 0.995

Q_INIT    = 10,
Q_STD     = 1e-2
