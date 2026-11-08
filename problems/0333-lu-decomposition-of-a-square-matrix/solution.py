import numpy as np

def lu_decomposition(A):
    U = np.array(A, dtype=float)   
    n = len(U)
    L = np.eye(n)

    for rc in range(n - 1):
        for i in range(rc + 1, n):
            m = U[i, rc] / U[rc, rc]
            L[i, rc] = m         
            U[i, :] = U[i, :] - m * U[rc, :]

    return L, U