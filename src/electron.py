import numpy as np


def electron(matrix):
    accelerating = [["e"] * matrix]

    for n in range(0, matrix - 1):
        values = [1] * (matrix - 1)
        values.append("e")
        accelerating = np.append(accelerating, [values], axis=0)

    return accelerating
