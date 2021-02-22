

def taxi_fare():
    base = 4
    km = float(input("Inserisci km percorsi: "))
    # Converto chilometri in metri e calcolo tariffa aggiuntiva
    plus = int((km * 1000) / 140) * 0.25
    total = plus + base
    return total

print(taxi_fare())