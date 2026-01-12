import numpy as np

from numpy_better import normalize_by_column

def test_normalize_by_column_basic():
    m = np.array([
        [10,  0,  5],
        [20,  0, 15],
        [30,  0, 25],
    ], dtype=float)

    expected = np.array([
        [0.0, 0.0, 0.0],
        [0.5, 0.0, 0.5],
        [1.0, 0.0, 1.0],
    ])

    result = normalize_by_column(m)

    assert result.shape == expected.shape
    assert np.allclose(result, expected)


def test_normalize_by_column_constant_column():
    m = np.array([
        [5,  1],
        [5,  2],
        [5,  3],
    ], dtype=float)

    result = normalize_by_column(m)

    # First column is constant → all zeros
    assert np.all(result[:, 0] == 0)

    # Second column normalized 1 → 0, 2 → 0.5, 3 → 1
    assert np.allclose(result[:, 1], np.array([0.0, 0.5, 1.0]))

if __name__ == "__main__":

    test_normalize_by_column_basic()
    test_normalize_by_column_constant_column()