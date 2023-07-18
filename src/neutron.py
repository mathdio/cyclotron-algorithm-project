import numpy as np


def neutron(matrix):
    accelerating = [["n"] * matrix]

    for _ in range(0, matrix - 1):
        values = [1] * matrix
        accelerating = np.append(accelerating, [values], axis=0)

    return accelerating
