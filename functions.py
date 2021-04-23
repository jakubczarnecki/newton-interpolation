import numpy as np


# f(x)
def linear(x, a, b):
    return a * x + b


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

# # q(x) = f(h(x))
# def comp_lin_poly(x, a, b):
#     return a * linear(polynomial(x)) + b




