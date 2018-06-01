import json
import numpy as np

def read_json(fn):
    with open(fn,'r') as f:
        return json.load(f)

def write_json(fn,data):
    with open(fn,'w') as f:
        json.dump(data, f, indent=2)

def sma(x,n=100):
    s = np.zeros((len(x)))
    for i in range(1,n):
        s[i] = np.mean(x[:i])

    for i in range(n,len(x)):
        s[i] = np.mean(x[i-n:i])

    return s
