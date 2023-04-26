import numpy as np
from function import func_arr


def f(parameters: np.ndarray, gradients: np.ndarray, x: float):
    return parameters - np.dot(gradients, x)


class Dichotomy(object):
    lr: float

    def __init__(self):
        self.epsilon = 1e-4
        self.delta = np.random.uniform(0, 2 * self.epsilon)

    def __call__(self, parameters: np.ndarray, gradients: np.ndarray):
        left = 1e-5
        right = 9e-1

        while right - left >= 2 * self.epsilon:
            x1 = ((right + left) / 2) - (self.delta / 2)
            x2 = ((right + left) / 2) + (self.delta / 2)
            if func_arr(f(parameters, gradients, x1)) <= func_arr(f(parameters, gradients, x2)):
                right = x2
            else:
                left = x1

        self.lr = (right + left) / 2
        return self.lr
