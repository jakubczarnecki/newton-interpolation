def horner(x, wsp):
    result = wsp[0]

    for i in wsp:
        result = result * x + i
        return result