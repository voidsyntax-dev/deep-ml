import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    n = len(y)
    indices = np.random.permutation(n)
    return X[indices, :], y[indices]