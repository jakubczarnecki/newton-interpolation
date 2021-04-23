import numpy as np

def polynomialFactors(n):
    tab = np.empty(shape = n, dtype = 'double')
    for i in range(int(n)):
        print("Podaj wspolczynnik " + str(i) + ":\n")
        factor = input()
        tab[i] = np.double(factor)

    return tab

def merge(arr1, arr2):
    return np.array([arr1, arr2])
