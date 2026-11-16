# Cell 1
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    i = 0
    results = []
    if y is not None:
        while i+batch_size < len(y):
            results.append([X[i:i+batch_size, :].tolist(), y[i:i+batch_size].tolist()])
            i += batch_size
        if i != len(y):
            results.append([X[i:, :].tolist(), y[i:].tolist()])
    else:
        while i+batch_size < len(X):
            results.append([X[i:i+batch_size, :].tolist()])
            i += batch_size
        if i != len(X):
            results.append([X[i:, :].tolist()])
    return results