import numpy as np

def normalize_by_column(m: np.ndarray) -> np.ndarray:
    """
    Normalizes each column of the input matrix, returning a new matrix

        args:
            m (np.ndarray): input matrix

        returns: 
            n (np.ndarray): normalized matrix

        raises:
            ValueError: if the array is not bidimensional
            TypeError: if the input is not a NumPy array
    """

    if not isinstance(m, np.ndarray):
        raise TypeError("Input should be a NumPy array")
    if len(m.shape) != 2:
        raise ValueError("Input should be a NumPy array with 2 dimensions")
    
    mn = m.min(axis=0)
    mx = m.max(axis=0)
    diff = mx-mn

    diff_safe = np.where(diff==0, 1, diff)

    n = (m - mn) / diff_safe

    n[:, diff == 0] = 0

    return n


    
    