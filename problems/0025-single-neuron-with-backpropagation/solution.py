import numpy as np

def train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs):
    X = np.asarray(features, dtype=float)
    y = np.asarray(labels, dtype=float)
    w = np.asarray(initial_weights, dtype=float).copy()
    b = float(initial_bias)
    n = X.shape[0]
    mse_values = []

    for _ in range(epochs):
        z = X @ w + b
        p = 1.0 / (1.0 + np.exp(-z))
        error = p - y
        mse_values.append(np.mean(error ** 2))
        dz = (2.0 / n) * error * p * (1.0 - p)
        w = w - learning_rate * (X.T @ dz)
        b = b - learning_rate * np.sum(dz)

    return (np.round(w, 4).tolist(), round(b, 4), [round(float(m), 4) for m in mse_values])