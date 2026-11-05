# Cell 1
import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    A = np.array(a)
    try:
        reshaped = A.reshape(new_shape)
    except ValueError:
        return []
    return reshaped.tolist()