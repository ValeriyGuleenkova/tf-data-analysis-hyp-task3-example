import pandas as pd
import numpy as np
from scipy.stats import permutation_test

chat_id = 215606022  # Ваш chat ID, не меняйте название переменной

SGN_LVL = 0.09

def solution(x: np.array, y: np.array) -> bool:
    pval = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis),
                                            vectorized=True,
                                            n_resamples=5000,
                                            alternative='less').pvalue
    if pval < SGN_LVL:
        return True
    # true: выборки не равны
    return False
