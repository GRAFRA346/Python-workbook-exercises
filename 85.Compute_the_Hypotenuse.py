from math import sqrt


def ipotenusa():
    print("\tInserisci i cateti")
    side1 = float(input("Inserisci primo cateto: "))
    side2 = float(input("Inserisci secondo cateto: "))
    c = side1 ** 2 + side2 ** 2
    result = sqrt(c)
    return result

print("L'ipotenusa è: %.4f" % ipotenusa())