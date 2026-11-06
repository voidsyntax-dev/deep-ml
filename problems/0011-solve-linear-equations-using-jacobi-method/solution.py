# Cell 1
import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = (np.zeros(len(A))).tolist()
    for _ in range(n):
        curr = x.copy()
        for i in range(len(A)):
            beta = [A[i][j] * curr[j] for j in range(len(A)) if j != i]
            x[i] = round(((b[i] - sum(beta))/A[i][i]), 4)
            
    return x