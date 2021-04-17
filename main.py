import functions as f
import numpy as np
from horner import horner

if __name__ == '__main__':
    print("\nMetody numeryczne - zadanie 3\n")
    print("Wariant 5 - interpolacja Newtona dla nierównych odstępów argumentu")
    print("Autorzy - Oskar Kurczewski i Jakub Czarnecki")

    left, right = np.double
    number = np.uint

    print('Podaj dolna granice interpolacji:')
    input(left)
    print('Podaj dolna granice interpolacji:')
    input(right)
    print('Podaj liczbe wezlow:')
    input(number)



