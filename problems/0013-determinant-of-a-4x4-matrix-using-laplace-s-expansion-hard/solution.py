# Cell 1
def determinant_4x4(matrix: list[list[int|float]]) -> float:
    import numpy as np
    return np.linalg.det(matrix)