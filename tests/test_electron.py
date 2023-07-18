from src.electron import electron

mock_matrix_five = [
    ["e", "e", "e", "e", "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
    [1, 1, 1, 1, "e"],
]

mock_matrix_four = [
    ["e", "e", "e", "e"],
    [1, 1, 1, "e"],
    [1, 1, 1, "e"],
    [1, 1, 1, "e"],
]


def test_electron():
    assert (electron(5) == mock_matrix_five).all()
    assert (electron(4) == mock_matrix_four).all()
