# This program compute the order's shipping cost.
# It compute first item like 10.95$ and the other items like 2.95$

def Shipping():
    first = 10.95
    other = 2.95
    total = 0
    order = int(input("Inserisci numero di ordini: "))
    if order == 1:
        total += first
        return total
    else:
        total = first + (other * (order - 1))
        return total


print("Il totale è: %.2f$" % Shipping())