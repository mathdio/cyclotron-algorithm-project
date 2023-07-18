import numpy as np


def without_particle(matrix):
    row = [[1] * matrix] * matrix
    return np.array(row)
