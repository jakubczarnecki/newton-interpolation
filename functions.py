import numpy as np

# f(x)
def linear(x, a, b):
    return a * x + b

# g(x)
def absolute(x, a, b):
    return a * abs(x) + b

# h(x)
def polynomial(x, tab):
    return tab[0] * x ** 4 + \
           tab[1] * x ** 3 + \
           tab[2] * x ** 2 + \
           tab[3] * x + \
           tab[4]

# p(x)
def trigonometric(x, a, b):
    return a * np.sin(x) + b

# q(x) = f(h(x))
def comp_lin_poly(x, a, b):
    return a * linear(polynomial(x)) + b




