import os
from src.util import write_json
import numpy as np
import datetime

def convert(x):
    if type(x) == np.ndarray:
        if x.dtype == np.int64:
            x = x.astype(int)
        if x.dtype == np.float64:
            x = x.astype(float)

        x = x.tolist()
        return x
    else:
        if type(x) == np.int64:
            return int(x)
        if type(x) == np.float64:
            return float(x)

    return x
class EpisodeWriter(object):
    def __init__(self, top_dir, id_):
        self.top_dir = top_dir
        self.id      = id_
        if not os.path.isdir(self.top_dir):
            os.mkdir(self.top_dir)

    def make_episode_dir(self, episode_id):
        d = "{}/{}".format(self.top_dir,episode_id)
        if not os.path.isdir(d):
            os.mkdir(d)

    def write(self, episode_id, step, s, a, r, ss, done):
        s  = convert(s)
        a  = convert(a)
        ss = convert(ss)

        data = {"episode_id":episode_id,
            "step":step,
            "s":s,
            "a":a,
            "r":r,
            "ss":ss,
            "done":done,
            "timestamp":str(datetime.datetime.now())}

        fn = "{}/{}/{}.json".format(self.top_dir,episode_id,step)

        write_json(fn,data)
