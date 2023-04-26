from function import func
import autograd.variable as av
import numpy as np
from visualization.visualizator import visualize
from dichotomy import Dichotomy


class FGD(object):
    lr: float

    def __init__(self, parameters: np.ndarray, epochs: int):
        self.value = None
        self.parameters = parameters
        self.epochs = epochs
        self.param_history = []
        self.optimize_lr = Dichotomy()

    def step(self):
        gradients = self.value.compute_gradients()[0]
        self.lr = self.optimize_lr(self.parameters, gradients)
        self.parameters -= np.dot(gradients, self.lr)
        self.param_history.append(list(self.parameters))

    def optimize(self):
        self.param_history.append(list(self.parameters))

        for epoch in range(self.epochs):
            big_variable = av.Variable([self.parameters[0], self.parameters[1]])
            w1, w2 = big_variable[0], big_variable[1]

            self.value = func(w1, w2)
            self.step()


parameters = np.array([-17.7, -12.])
gd = FGD(parameters=parameters, epochs=3)
gd.optimize()
print(gd.param_history)
visualize(gd.param_history)
