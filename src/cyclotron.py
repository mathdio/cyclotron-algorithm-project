from without_particle import without_particle
from electron import electron


def circulate_cyclotron(matrix, particle=None):
    if particle == "e":
        return electron(matrix)
    elif particle is None:
        return without_particle(matrix)
    else:
        return "Invalid particle!"


print(circulate_cyclotron(7, "e"))
