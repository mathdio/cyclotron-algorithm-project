from src.proton import proton

mock_matrix_six = [
    ["p", "p", "p", "p", "p", "p"],
    ["p", 1, 1, 1, 1, "p"],
    ["p", 1, 1, 1, 1, "p"],
    ["p", 1, 1, 1, 1, "p"],
    ["p", 1, 1, 1, "p", "p"],
    ["p", "p", "p", "p", "p", 1],
]

mock_matrix_four = [
    ["p", "p", "p", "p"],
    ["p", 1, 1, "p"],
    ["p", 1, "p", "p"],
    ["p", "p", "p", 1],
]


def test_proton():
    assert (proton(6) == mock_matrix_six).all()
    assert (proton(4) == mock_matrix_four).all()
