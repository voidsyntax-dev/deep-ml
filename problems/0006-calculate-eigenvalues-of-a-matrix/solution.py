# Cell 1
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    import numpy as np
    (eigvals, eigvectors) = np.linalg.eig(np.array(matrix))
    return (np.sort(eigvals.real))[::-1].tolist()