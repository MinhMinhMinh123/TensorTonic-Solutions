import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    n = len(v)
    A = np.zeros((n,n))
    A[list(range(n)),list(range(n))] = v
    return A
