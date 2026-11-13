# Cell 1
import math

def sigmoid(z: float) -> float:
    return round(1/(1+pow(math.e, -z)), 4)