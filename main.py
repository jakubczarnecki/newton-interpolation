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

    left = np.double(left)
    right = np.double(right)
    number = int(number)

    X = np.array([-2, 0, 1, 2, 3, 4, 6, 8], dtype='double') #to np. z pliku bedzie wczytane

    if func == "1":
        level = input("Podaj stopien wielomianu: ")
        factors = polynomialFactors(int(level))
        print("Tablica wspolczynnikow wielomianu: \n" + str(factors) + "\n")
        Y = polynomial(X, factors)

    elif func == "2":
        a = input('Podaj a: ')
        b = input('Podaj b: ')
        a = np.double(a)
        b = np.double(b)
        Y = linear(X, a, b)

    elif func == "3":
        a = input('Podaj a: ')
        b = input('Podaj b: ')
        a = np.double(a)
        b = np.double(b)
        Y = linear(X, a, b)

    elif func == "4":
        a = input('Podaj a: ')
        b = input('Podaj b: ')
        a = np.double(a)
        b = np.double(b)
        Y = linear(X, a, b)

    # Nasza interpolacja
    xs = np.linspace(left, right, 1000, endpoint = True)
    ys = []
    for x in xs:
        if(func == "1"):
            ys.append(newton(X, Y, x))
        if (func == "2"):
            ys.append(newton(X, Y, x))
        if (func == "3"):
            ys.append(newton(X, Y, x))
        if (func == "4"):
            ys.append(newton(X, Y, x))

    # Rzeczywisty wykres funkcji
    xs2 = np.linspace(left, right, 1000, endpoint = True)
    ys2 = []
    for x in xs2:
        # if (func == "1"):
            # tutaj horner chyba
        if (func == "2"):
            ys2.append(linear(x, a, b))
        if (func == "3"):
            ys2.append(absolute(x, a, b))
        if (func == "4"):
            ys2.append(trigonometric(X, a, b))


    #Rysowanie
    plt.plot(X, Y, 's', label = "węzły")  # blue dot indicates the original value
    plt.plot(xs, ys, 'r', label = 'interpolation values')  # Interpolation curve
    plt.plot(xs2, ys2, 'y', label = 'real function values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc = 4)
    plt.show()




