from scipy.stats import t
import numpy as np


chat_id = 356550601 # Ваш chat ID, не меняйте название переменной

def solution(X) -> bool:
    n = len(X)
    mean = np.mean(X)
    std = np.std(X, ddof=1)
    threshold = 500
    alpha = 0.1
    t_stat = (mean - threshold) / (std / np.sqrt(n))
    t_crit = t.ppf(1 - alpha, n - 1)
    return t_stat > t_crit
