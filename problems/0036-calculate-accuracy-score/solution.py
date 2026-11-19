import numpy as np

def accuracy_score(y_true, y_pred):
    case = y_pred == y_true
    return np.sum(case)/len(case)