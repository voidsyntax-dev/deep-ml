import numpy as np

def divide_on_feature(X, feature_i, threshold):
    required = X[:, feature_i] >= threshold
    return [X[required], X[~required]]