import functions as f
import numpy as np
from horner import horner
from functions import *
from points import point_generator

if __name__ == '__main__':
    print('\nMetody numeryczne - zadanie 3\n')
    print('Wariant 5 - interpolacja Newtona dla nierównych odstępów argumentu')
    print('Autorzy - Oskar Kurczewski i Jakub Czarnecki')

    # x = np.loadtxt('data.txt', dtype='double')
    # number = x.shape[0]

    print('Podaj funkcję: ')
    print('1) f(x) = 3x - 1')
    print('2) g(x) = |x|')
    print('3) h(x) = x^3 - 7x - 1')
    print('4) p(x) = sin(x) + 1')
    print('5) q(x) = f(h(x))')
    choice = input()

    left = input('Podaj dolna granice interpolacji (float64):')
    right = input('Podaj gorna granice interpolacji (float64):')
    number = input('Podaj liczbe wezlow (int):')

    # pythonowy float to float64 - czyli double znany z np. javy
    left = float(left)
    right = float(right)
    number = int(number)

    print(point_generator(left, right, number))

