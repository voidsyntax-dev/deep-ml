# Cell 1
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    import numpy as np
    A = np.cov(np.array(vectors))
    return A.tolist()