import stdpopsim
import msprime
import numpy as np


def params_extractor(model):
    t_div = model.demographic_events[5].time
    params = np.array([[7300, 12300, 3517.113, t_div]])
    return params
