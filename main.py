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
    print("2 - g(x) = a * |x| + b\n")
    print("3 - h(x) = a * sin(x) + b\n")
    print("4 - złożenie dwóch funkcji\n")
    func = input()

    print('Chcesz podac wezly (p) czy je wylosowac (l)?\n')
    isRandom = input()

    if isRandom == 'l':

        left = input('Podaj dolna granice interpolacji (float64):')
        left = np.double(left)
        right = input('Podaj gorna granice interpolacji (float64):')
        right = np.double(right)
        number = input('Podaj liczbe wezlow (int):')

        left = np.double(left)
        right = np.double(right)
        number = int(number)

        X = point_generator(left, right, number)

    else:
        number = input('Podaj liczbe wezlow (int):')
        X = np.empty(int(number), dtype = 'double')
        left = input('Podaj dolna granice rysowania wykresu:')
        left = np.double(left)
        right = input('Podaj gorna granice rysowania wykresu:')
        right = np.double(right)
        for i in range(int(number)):
            X[i] = input('Węzeł ' + str(i) + ' (double):')

    # X = np.array([-2, 0, 1, 2, 3, 4, 6, 8], dtype='double') #to np. z pliku bedzie wczytane
    # X = np.array([-5, -2, 0, 3.5, 7]) # imo tam na gorze za rowne odstepy byly XD

    if func == "1":
        factors = choosePolynomialFactors()
        Y = polynomial(X, factors)

    elif func == "2":
        a, b = chooseFactors()
        Y = absolute(X, a, b)

    elif func == "3":
        a, b = chooseFactors()
        Y = trigonometric(X, a, b)

    elif func == "4":
        print("Podaj funkcję 1: ")
        print("1 - wielomian n-tego stopnia\n")
        print("2 - g(x) = a * |x| + b\n")
        print("3 - h(x) = a * sin(x) + b\n")
        f1 = input()
        if f1 == "1":
            factors1 = choosePolynomialFactors()

        elif f1 == "2" or f1 == "3":

            a1, b1 = chooseFactors()

        print("Podaj funkcję 2: ")
        print("1 - wielomian n-tego stopnia\n")
        print("2 - g(x) = a * |x| + b\n")
        print("3 - h(x) = a * sin(x) + b\n")
        f2 = input()
        if f2 == "1":
            factors2 = choosePolynomialFactors()

        elif f2 == "2" or f2 == "3":
            a2, b2 = chooseFactors()
        if f1 == "1" and f2 == "1":
            Y = polynomial(polynomial(X, factors2), factors1)
        elif f1 == "1" and f2 == "2":
            Y = polynomial(absolute(X, a2, b2), factors1)
        elif f1 == "1" and f2 == "3":
            Y = polynomial(trigonometric(X, a2, b2), factors1)
        elif f1 == "2" and f2 == "1":
            Y = absolute(polynomial(X, factors2), a1, b1)
        elif f1 == "2" and f2 == "2":
            Y = absolute(absolute(X, a2, b2), a1, b1)
        elif f1 == "2" and f2 == "3":
            Y = absolute(trigonometric(X, a2, b2), a1, b1)
        elif f1 == "3" and f2 == "1":
            Y = trigonometric(polynomial(X, factors2), a1, b1)
        elif f1 == "3" and f2 == "2":
            Y = trigonometric(absolute(X, a2, b2), a1, b1)
        elif f1 == "3" and f2 == "3":
            Y = trigonometric(trigonometric(X, a2, b2), a1, b1)

    # Nasza interpolacja
    xs = np.linspace(left, right, 1000, endpoint = True)
    ys = []
    for x in xs:
        ys.append(newton(X, Y, x))

    # Rzeczywisty wykres funkcji
    xs2 = np.linspace(left, right, 1000, endpoint = True)
    ys2 = []
    for x in xs2:
        if (func == "1"):
            ys2.append(horner(x, factors))
        if (func == "2"):
            ys2.append(absolute(x, a, b))
        if (func == "3"):
            ys2.append(trigonometric(x, a, b))
        if (func == "4"):
            if f1 == "1" and f2 == "1":
                ys2.append(polynomial(polynomial(x, factors2), factors1))
            elif f1 == "1" and f2 == "2":
                ys2.append(polynomial(absolute(x, a2, b2), factors1))
            elif f1 == "1" and f2 == "3":
                ys2.append(polynomial(trigonometric(x, a2, b2), factors1))
            elif f1 == "2" and f2 == "1":
                ys2.append(absolute(polynomial(X, factors2), a1, b1))
            elif f1 == "2" and f2 == "2":
                ys2.append(absolute(absolute(x, a2, b2), a1, b1))
            elif f1 == "2" and f2 == "3":
                ys2.append(absolute(trigonometric(x, a2, b2), a1, b1))
            elif f1 == "3" and f2 == "1":
                ys2.append(trigonometric(polynomial(x, factors2), a1, b1))
            elif f1 == "3" and f2 == "2":
                ys2.append(trigonometric(absolute(x, a2, b2), a1, b1))
            elif f1 == "3" and f2 == "3":
                ys2.append(trigonometric(trigonometric(x, a2, b2), a1, b1))


    #Rysowanie
    plt.plot(X, Y, 's', label = "węzły interpolacyjne")  # blue dot indicates the original value
    plt.plot(xs, ys, 'r', label = 'wielomian interpolacyjny')  # Interpolation curve
    plt.plot(xs2, ys2, 'y', label = 'wielomian interpolowany')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(title='Legenda', loc='best', fontsize='xx-small')
    plt.grid(b = True, axis = 'both')
    plt.show()




