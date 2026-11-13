# Cell 1
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int],
                        weights: list[float], bias: float) -> tuple[list[float], float]:
    X = np.array(features, dtype=float)    
    w = np.array(weights, dtype=float)    
    y = np.array(labels, dtype=float)   

    z = X @ w + bias                     
    pred = 1 / (1 + np.exp(-z))        

    mse = np.mean((pred - y) ** 2)
    return pred.tolist(), float(mse)