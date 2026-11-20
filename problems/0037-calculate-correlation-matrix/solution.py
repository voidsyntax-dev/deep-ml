import numpy as np

def calculate_correlation_matrix(X, Y=None):
    if Y is None:
        return np.corrcoef(X, rowvar=False)
    p = X.shape[1]
    full = np.corrcoef(np.hstack([X, Y]), rowvar=False)
    return full[:p, p:]