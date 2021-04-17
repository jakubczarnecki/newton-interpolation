# wartosc argumentu, tablica wspolczynnikow, dlugosc tablicy

def horner(x, wsp, n):
    result = wsp[0]

    for i in n:
        result = result * x + wsp[i]
        return result