print("""
        LISTINO PREZZI ZOO
        -Bambino <=2 anni: 0$
        -Ragazzo <=12 anni: 14$
        -Anziano 65+ anni: 18$
        -Altri: 23$
""")

bambino: float = 0
ragazzo: float = 14
anziano: float = 18
altro: float = 23

eta_bambino: int = 2
eta_ragazzo: int = 12
eta_anziano: int = 65

totale = 0

riga = input("Inserisci età del cliente(Riga vuota per terminare): ")

while riga != "":
    eta = int(riga)

    if eta <= eta_bambino:
        totale += bambino
    elif eta <= eta_ragazzo:
        totale += ragazzo
    elif eta >= eta_anziano:
        totale += anziano
    else:
        totale += altro

    riga = input("Inserisci età del cliente(Riga vuota per terminare): ")

print("Il totale del gruppo è: %.2f$" % totale)
