# Cell 1
import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    indices = np.arange(n_samples)
    if shuffle == True:
        np.random.shuffle(indices)
    
    fold_sizes = np.full(k, n_samples//k)
    fold_sizes[:n_samples%k] += 1
    
    fold = []
    start = 0
    for fold_size in fold_sizes:
        fold.append(indices[start:start+fold_size].tolist())
        start += fold_size
    
    result = []
    for i in range(k):
        test = fold[i]
        train = [index for j in range(k) if j!=i for index in fold[j] ] 
        result.append((train, test))
        
    return result