import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.array(A)
    return (np.linalg.inv(A) if np.linalg.matrix_rank(A)==len(A) else None)
