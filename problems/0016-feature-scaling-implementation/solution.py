# Cell 1
import numpy as np

def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    def standard(x):
        mu = np.mean(x, axis=0)
        sigma = np.std(x, axis=0)
        return np.round((x - mu) / sigma, 4)

    def minmax(x):
        x_max = np.max(x, axis=0)
        x_min = np.min(x, axis=0)
        return np.round((x - x_min) / (x_max - x_min), 4)

    return standard(data), minmax(data)