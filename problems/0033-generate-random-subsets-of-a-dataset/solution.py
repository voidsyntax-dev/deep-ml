import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    n = len(X)
    rows = n if replacements==True else int(np.floor(n/2))
    result = []

    for _ in range(n_subsets):
        s = np.random.choice(np.arange(n), rows, replace = replacements)
        result.append((X[s, :].tolist(), y[s].tolist()))
    
    return result
