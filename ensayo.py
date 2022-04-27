import numpy as np


def l2_dist(a, b):
    result = ((a - b) * (a - b)).np.sum()
    result = result ** 0.5
    return result 

l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1)))