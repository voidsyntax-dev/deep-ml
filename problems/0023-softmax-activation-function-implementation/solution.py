# Cell 1
import math

def softmax(scores: list[float]) -> list[float]:
    z_max = max(scores)
    scores = [score-z_max for score in scores]
    e_z = [pow(math.e, score) for score in scores]
    e_z_sum = sum(e_z)
    return [x/e_z_sum for x in e_z]