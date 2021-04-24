import numpy as np
from utils import *

# g(x)
def absolute(x, a, b):
    return a * abs(x) + b


# h(x)
def polynomial(x, tab):
    numOfFactors = len(tab)
    result = 0
    for i in range(numOfFactors - 1):
        if (i == (numOfFactors - 1)):
            result += tab[i]
        result += tab[i] * x ** (numOfFactors - 1 - i)

    return result


# p(x)
def trigonometric(x, a, b):
    return a * np.sin(x) + b

def choosePolynomialFactors():
    level = input("Podaj stopien wielomianu: ")
    factors = polynomialFactors(int(level))
    print("Tablica wspolczynnikow wielomianu: \n" + str(factors) + "\n")
    return factors

def chooseFactors():
    a = input('Podaj a: ')
    b = input('Podaj b: ')
    a = np.double(a)
    b = np.double(b)
    return a, b


# def chooseComposition(func, x):
#     if func == "1":
#         func = choosePolynomial(x)
#     elif func == "2":
#         func = chooseLinear(x)
#     elif func == "3":
#         func = chooseAbsolute(x)
#     elif func == "4":
#         func = chooseTrigonometric(x)
#     return func


