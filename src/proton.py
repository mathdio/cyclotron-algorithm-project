import numpy as np


def proton(matrix):
    accelerating = [["p"] * matrix]

    for n in range(1, matrix):
        values = None

        if n == matrix - 1:
            values = ["p"] * (matrix - 1)
            values.append(1)
        elif n == matrix - 2:
            aux = matrix - 3
            values = [1] * aux
            values.insert(0, "p")
            values.append("p")
            values.append("p")
        else:
            values = [1] * (matrix - 2)
            values.append("p")
            values.insert(0, "p")

        accelerating = np.append(accelerating, [values], axis=0)

    return accelerating


print(proton(5))
