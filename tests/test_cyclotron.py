from src.cyclotron import cyclotron
import pytest

mock_neutron = [
    ["n", "n", "n", "n"],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

mock_electron = [
    ["e", "e", "e", "e", "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
]

mock_proton = [
    ["p", "p", "p", "p"],
    ["p", 1, 1, "p"],
    ["p", 1, "p", "p"],
    ["p", "p", "p", 1],
]

mock_without_particle = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]


def test_cyclotron():
    assert (cyclotron(4, "n") == mock_neutron).all()
    assert (cyclotron(5, "e") == mock_electron).all()
    assert (cyclotron(4, "p") == mock_proton).all()
    assert (cyclotron(4) == mock_without_particle).all()

    with pytest.raises(ValueError):
        cyclotron(3, "e")
        cyclotron(4, "w")
