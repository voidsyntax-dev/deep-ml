# Cell 1
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    A = np.array(a)
    return A.T
    pass