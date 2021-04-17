from functions import *
from newton import *
import numpy as np
import matplotlib.pyplot as plt
from horner import horner
from points import point_generator

if __name__ == '__main__':
    print('\nMetody numeryczne - zadanie 3\n')
    print('Wariant 5 - interpolacja Newtona dla nierównych odstępów argumentu')
    print('Autorzy - Oskar Kurczewski i Jakub Czarnecki')

    # x = np.loadtxt('data.txt', dtype='double')
    # number = x.shape[0]

    print("Wybierz funkcję:\n");
    print("1 - f(x) = 3 * x - 1\n");
    print("2 - g(x) = |x|\n");
    print("3 - h(x) = x * x * x - 7 * x - 1\n");
    print("4 - p(x) = sin(x) + 1\n");
    print("5 - f(g(x))\n");

    left = input('Podaj dolna granice interpolacji (float64):')
    right = input('Podaj gorna granice interpolacji (float64):')
    number = input('Podaj liczbe wezlow (int):')

    # pythonowy float to float64 - czyli double znany z np. javy
    left = float(left)
    right = float(right)
    number = int(number)

    X = point_generator(left, right, number)
    Y = trigonometric(X)
    # X = [-1, 0, 1, 2, 3, 4, 5]
    # Y = [-20, -12, 1, 15, 4, 21, 41]
    print(X)
    print(Y)

    A = differences(X, Y)
    print(A)

    xs = np.linspace(np.min(X), np.max(X), 1000, endpoint=True)
    ys = []
    for x in xs:
        ys.append(newton(X, Y, x))

    xs2 = np.linspace(np.min(X), np.max(X), 1000, endpoint=True)
    ys2 = []
    for x in xs2:
        ys2.append(trigonometric(x))

    plt.title("Newton ez")
    plt.plot(X, Y, 's', label="original values")  # blue dot indicates the original value
    plt.plot(xs, ys, 'r', label='interpolation values')  # Interpolation curve
    plt.plot(xs2, ys2, 'y', label='real function values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)  #

    plt.show()




