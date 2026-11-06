# Cell 1
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    import numpy as np
    try:
        c = np.array(a) @ np.array(b)
    except (ValueError):
        return -1
    return c.tolist()