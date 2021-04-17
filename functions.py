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

# q(x) = f(h(x))
def comp_lin_poly(x):
    return linear(polynomial(x))

# silnia

def factorial(x):
    result = x
    if x > 1:
        for i in range (1, x):
            result += x - i
        return result
    elif x == 1 or x ==0:
        return 1
    else:
        print("Z tej liczby nie da sie obliczyc silni.")
        return None