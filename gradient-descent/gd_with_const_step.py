from function import func
import autograd as ad
import autograd.variable as av
import numpy as np
from visualization.visualizator import visualize


class GD(object):
    param_buff = np.ndarray

    def __init__(self, parameters: np.ndarray, lr: float, epochs: int):
        self.value = None
        self.parameters = parameters
        self.param_buff = parameters
        self.lr = lr
        self.epochs = epochs
        self.param_history = []

    def step(self):
        changed = True
        while changed:
            gradient = self.value.compute_gradients()
            self.param_buff = self.parameters - np.dot(gradient[0], self.lr)

            if func(self.parameters[0], self.parameters[1]) <= func(self.param_buff[0], self.param_buff[1]):
                self.lr /= 2
            else:
                changed = False

        self.parameters = self.param_buff
        self.param_history.append(self.parameters)

    def optimize(self):
        self.param_history.append(self.parameters)

        for epoch in range(self.epochs):
            big_variable = av.Variable([self.parameters[0], self.parameters[1]])
            w1, w2 = big_variable[0], big_variable[1]

            self.value = func(w1, w2)
            self.step()


parameters = np.array([-15., -15.])
gd = GD(parameters=parameters, lr=0.2, epochs=8)
gd.optimize()
visualize(gd.param_history)