import numpy as np

# f(x)
def linear(x):
    return 3 * x - 1

# g(x)
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

# h(x)
def polynomial(x):
    return x * x * x - 7 * x - 1

# p(x)
def trigonometric(x):
    return np.sin(x) + 1

# q(x) = f(g(x))
def comp_lin_poly(x):
    return linear(polynomial(x))
