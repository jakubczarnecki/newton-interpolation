import numpy as np

# f(x)
def linear(x):
    return 3 * x - 1

# g(x)
def absolute(x):
    return abs(x)

# h(x)
def polynomial(x):
    return x * x * x - 7 * x - 1

# p(x)
def trigonometric(x):
    return np.sin(x) + 1

# q(x) = f(h(x))
def comp_lin_poly(x):
    return linear(polynomial(x))


def merge(arr1, arr2):
    return np.array([arr1, arr2])


