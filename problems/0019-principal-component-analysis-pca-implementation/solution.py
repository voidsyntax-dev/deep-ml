# Cell 1
import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    d = (data - mu) / sigma

    covar = np.cov(d, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(covar)

    idx = np.argsort(eigvals)[::-1][:k]
    components = eigvecs[:, idx]              # columns are components, shape (n_features, k)

    for i in range(components.shape[1]):
        v = components[:, i]
        j = np.argmax(np.abs(v) > 1e-10)
        if v[j] < 0:
            components[:, i] = -v

    return components