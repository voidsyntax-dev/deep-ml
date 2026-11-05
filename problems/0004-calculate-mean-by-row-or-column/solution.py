# Cell 1
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    import numpy as np
    means = np.mean(matrix, axis = 0) if mode == "column" else np.mean(matrix, axis = 1)
    return means.tolist()