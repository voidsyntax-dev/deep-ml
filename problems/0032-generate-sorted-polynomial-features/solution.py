import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    n_samples, n_features = X.shape
    cols = [np.ones(n_samples)]
    for d in range(1, degree + 1):
        for combo in combinations_with_replacement(range(n_features), d):
            col = np.ones(n_samples)
            for i in combo:
                col = col * X[:, i]
            cols.append(col)
    result = np.column_stack(cols)
    return np.sort(result, axis=1)