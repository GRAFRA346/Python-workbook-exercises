def main():
    x = float(input("Inserisci primo numero: "))
    y = float(input("Inserisci secondo numero: "))
    z = float(input("Inserisci terzo numero: "))
    print("Il valore medio è: ", mediana(x, y, z))
    print("Il valore della mediana con metodo alternativo è: ", mediana(x, y, z))


def mediana(a, b, c):
    if a < b < c or a > b > c:
        return b
    elif b < a < c or b > a > c:
        return a
    else:
        return c


def MedAlternativa(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

print(main())

