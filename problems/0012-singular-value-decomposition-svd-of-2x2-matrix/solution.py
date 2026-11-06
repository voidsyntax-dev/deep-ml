# Cell 1
import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    svd = np.linalg.svd(A)
    return svd