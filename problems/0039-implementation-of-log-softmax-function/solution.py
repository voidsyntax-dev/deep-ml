import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    m = np.max(scores)
    log_sum = np.log(np.sum(np.exp(scores - m)))
    return scores - m - log_sum