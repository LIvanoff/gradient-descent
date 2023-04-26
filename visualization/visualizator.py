import matplotlib.pyplot as plt
import numpy as np


def z(x, y):
    return x ** 2 - x * y + y ** 2 + 2 * x + 3 * y  # x ** 2 + 2 * y ** 2 + math.e ** (x + y)


def visualize(coord):
    x_grad = np.array([])
    y_grad = np.array([])
    for i in range(0, len(coord)):
        x_grad = np.append(x_grad, coord[i][0])
        y_grad = np.append(y_grad, coord[i][1])

    negative_bound = -20
    positive_bound = 0
    x = np.outer(np.linspace(negative_bound, positive_bound, 100), np.ones(100))
    y = x.copy().T

    fig, axes = plt.subplots(1, 2)

    cs = axes[0].contour(x, y, z(x, y))

    axes[0].clabel(cs)
    axes[0].set_title('contour')

    axes[1].contourf(x, y, z(x, y), alpha=.8)
    axes[1].set_title('contourf')

    # for i in range(len(coord)-1):
    #     axes[0].annotate('', xy=coord[i], xytext=coord[i],
    #                  arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
    #                  va='center', ha='center')
    #     print('i = '+str(i)+' coord = ('+str(coord[i])+')')
    axes[0].plot(x_grad, y_grad, 'v-r', alpha=0.7, lw=3, mec='r', mew=1, ms=6)
    axes[1].plot(x_grad, y_grad, 'v-r', alpha=0.7, lw=3, mec='r', mew=1, ms=6)

    fig.set_figwidth(14)
    fig.set_figheight(7)
    plt.grid()
    plt.show()
