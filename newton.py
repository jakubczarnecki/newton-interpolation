import numpy as np

def differences(x, y):
    n = len(x)
    result = np.zeros([n, n])

    for i in range(0, n):
        result[i][0] = y[i]

    for j in range(1, n):
        for i in range(j, n):
            result[i][j] = (result[i][j-1] - result[i-1][j-1])/(x[i] - x[i-j])

    return result

def newton(x, y, n):
    sum = y[0]
    temp = np.zeros((len(x), len(x)))

    for i in range(0, len(x)):
        temp[i, 0] = y[i]
    temp_sum = 1.0

    for i in range(1, len(x)):
        temp_sum = temp_sum * (n - x[i - 1])

        for j in range(i, len(x)):
            temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (x[j] - x[j - i])
        sum += temp_sum * temp[i, i]
    return sum