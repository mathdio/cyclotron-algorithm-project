from src.without_particle import without_particle
from src.electron import electron
from src.neutron import neutron
from src.proton import proton


def cyclotron(matrix, particle=None):
    if matrix < 4:
        raise ValueError("Matrix value must be at least 4")

    if particle == "e":
        return electron(matrix)
    elif particle == "n":
        return neutron(matrix)
    elif particle == "p":
        return proton(matrix)
    elif particle is None:
        return without_particle(matrix)
    else:
        raise ValueError("Invalid particle!")
