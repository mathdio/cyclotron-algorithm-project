from src.neutron import neutron

mock_matrix_five = [
    ["n", "n", "n", "n", "n"],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

mock_matrix_four = [
    ["n", "n", "n", "n"],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]


def test_neutron():
    assert (neutron(5) == mock_matrix_five).all()
    assert (neutron(4) == mock_matrix_four).all()
