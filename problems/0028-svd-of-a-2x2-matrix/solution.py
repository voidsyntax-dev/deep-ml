# Cell 1
import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    U, s, Vt = np.linalg.svd(A)
    return U, s, Vt