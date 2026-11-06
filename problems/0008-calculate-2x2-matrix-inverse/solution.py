# Cell 1
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    import numpy as np
    return (np.linalg.inv(np.array(matrix))).tolist() if np.linalg.det(matrix) != 0 else None