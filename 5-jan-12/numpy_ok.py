import numpy as np

def _normalize_column(m: np.ndarray) -> np.ndarray:
    """
    Normalizes a 1D numpy array using min-max normalization

        args:
            m (np.ndarray): input 1D array

        returns: 
            n (np.ndarray): normalized array with values in [0, 1]
                           Returns array of zeros if all values are equal

        raises:
            ValueError: if the array is not 1-dimensional
            TypeError: if the input is not a NumPy array
    """

    if not isinstance(m, np.ndarray):
        raise TypeError("Input should be a NumPy array")
    if len(m.shape) != 1:
        raise ValueError

    mn = m.min()
    mx = m.max()

    if mx == mn:
        return np.full_like(m, 0)
    
    return (m-mn)/(mx-mn)

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
    
    return np.apply_along_axis(_normalize_column, axis=0, arr=m)
    