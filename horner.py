def horner(x, wsp):
    result = wsp[0]

    for i in range(len(wsp) - 1):
        result = result * x + wsp[i+1]

    return result