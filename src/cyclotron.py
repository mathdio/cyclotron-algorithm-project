from without_particle import without_particle
from electron import electron
from neutron import neutron


def circulate_cyclotron(matrix, particle=None):
    if particle == "e":
        return electron(matrix)
    elif particle == "n":
        return neutron(matrix)
    elif particle is None:
        return without_particle(matrix)
    else:
        return "Invalid particle!"


print(circulate_cyclotron(7, "n"))
