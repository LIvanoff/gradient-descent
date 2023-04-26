import numpy as np


def func(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2 + 2 * x1 + 3 * x2


def func_arr(x: np.ndarray):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2 + 2 * x[0] + 3 * x[1]
