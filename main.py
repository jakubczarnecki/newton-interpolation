from functions import *
from newton import *
import numpy as np
import matplotlib.pyplot as plt
from horner import horner
from functions import *
from points import point_generator
from utils import *

if __name__ == '__main__':
    print('\nMetody numeryczne - zadanie 3\n')
    print('Wariant 5 - interpolacja Newtona dla nierównych odstępów argumentu')
    print('Autorzy - Oskar Kurczewski i Jakub Czarnecki')

    # x = np.loadtxt('data.txt', dtype='double')
    # number = x.shape[0]

    print('Wybierz funkcję:\n')
    print("1 - wielomian n-tego stopnia\n")
    print("2 - f(x) = a * x + b\n")
    print("3 - g(x) = a * |x| + b\n")
    print("4 - h(x) = a * sin(x) + b\n")
    print("5 - złożenie dwóch funkcji\n")

    func = input()

    left = input('Podaj dolna granice interpolacji (float64):')
    left = np.double(left)
    right = input('Podaj gorna granice interpolacji (float64):')
    right = np.double(right)
    number = input('Podaj liczbe wezlow (int):')
    number = int(number)

    if func == "1":
        level = input("Podaj stopien wielomianu: ")
        factors = polynomialFactors(int(level))
        print("Tablica wspolczynnikow wielomianu: \n" + str(factors) + "\n")
        X = point_generator(left, right, number)
        Y = horner(X, factors)

        xs = np.linspace(np.min(X), np.max(X), 1000, endpoint = True)
        ys = []
        for x in xs:
            ys.append(newton(X, Y, x))

        xs2 = np.linspace(np.min(X), np.max(X), 1000, endpoint = True)
        ys2 = []
        for x in xs2:
            ys2.append(horner(x, factors))

    plt.plot(X, Y, 's', label = "original values")  # blue dot indicates the original value
    plt.plot(xs, ys, 'r', label = 'interpolation values')  # Interpolation curve
    plt.plot(xs2, ys2, 'y', label = 'real function values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc = 4)

    plt.show()




