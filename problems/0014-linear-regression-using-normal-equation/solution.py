# Cell 1
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).ravel()
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    return [round(float(v), 4) for v in beta]