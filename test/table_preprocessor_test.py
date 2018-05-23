import os
import sys
sys.path.append(os.path.abspath('..'))

import numpy as np

from src.preprocessor import TablePreprocessor

N = 4
ranges = np.array([[0,1],[-1,1],[1,2]])

P = TablePreprocessor(ranges,N)

#######################################
# Preprocessing
#######################################
s = np.array([0,-1,1])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

s = np.array([1,1,2])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

s = np.array([0.4,-1,1])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

s = np.array([0.4,-0.24,1])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

s = np.array([0.4,-0.24,1.3])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

s = np.array([0.4,-0.24,1.74])
n = P.preprocess(s)

print("{} processed to {}".format(s,n))

########################################
# Deprocessing
########################################
n = 0
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))

n = 63
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))

n = 1
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))

n = 5
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))

n = 21
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))

n = 37
s = P.deprocess(n)

print("{} deprocessed to {}".format(n,s))
