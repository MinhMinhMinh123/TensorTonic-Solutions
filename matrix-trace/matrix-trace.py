import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    return sum(np.array(A)[list(range(len(A))),list(range(len(A)))])
