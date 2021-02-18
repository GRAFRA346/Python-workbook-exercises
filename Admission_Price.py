bambino: float = 0
ragazzo: float = 14
anziano: float = 18
altro: float = 23

eta_bambino: int = 2
eta_ragazzo: int = 14
eta_anziano: int = 23

totale = 0

riga = input("Inserisci età del cliente(Riga vuota per terminare): ")

while riga != "":
    eta = int(riga)

    if eta <= 2:
        totale += bambino
    elif 3 <= eta <= 12:
        totale += ragazzo
    elif eta >= 65:
        totale += anziano
    else:
        totale += altro

    riga = input("Inserisci età del cliente(Riga vuota per terminare): ")

print("Il totale del gruppo è: %.2f$" % totale)
