import numpy as np

def point_generator(left, right, n):
    points = np.random.uniform(left, right, n)

    return np.sort(points)