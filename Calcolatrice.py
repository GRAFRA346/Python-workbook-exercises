while True:
    print('''
        Benvenuto al programma calcolatrice!
        Creata da: Francesco
        Di seguito un elenco delle varie funzioni disponibili:

        -Per effettuare una Addizione seleziona 1;
        -Per effettuare una Sottrazione seleziona 2;
        -Per effettuare una Moltiplicazione seleziona 3;
        -Per effettuare una Divisione seleziona 4;
        -Per effettuare un Calcolo Esponenziale seleziona 5;
        -Per uscire dal programma puoi digitare ESC;
        ''')

    scelta = input("Inserisci il numero corrispondete all\'azione desiderata -->")

    if scelta == "1":
        print("\nHai scelto: Addizione\n")
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato della somma è: " + str(a + b))
    elif scelta == "2":
        print("\nHai scelto: Sottrazione\n")
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato della somma è: " + str(a - b))
    elif scelta == "3":
        print("\nHai scelto: Moltiplicazione\n")
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato della somma è: " + str(a * b))
    elif scelta == "4":
        print("\nHai scelto: Divisione\n")
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato della somma è: " + str(a / b))
    elif scelta == "5":
        print("\nHai scelto: Calcolo Esponenziale\n")
        a = float(input("Inserisci la base: "))
        b = float(input("Inserisci l\'esponente: "))
        print("Il risultato della somma è: " + str(a ** b))
    elif scelta == "ESC" or scelta == "esc":
        print('''L\'apllicazione verrà chiusa!

        +++++++++++++++++++++++++++++++++++++++++''')
        break
    elif scelta != "1" or "2" or "3" or "4" or "5":
        print("Inserimento errato")

    loop = input("\nDesideri continuare ad usare l\'applicazione? S/N")
    if loop == "S" or loop == "s":
        print('''Torno al menù principale

                +++++++++++++++++++++++++++++++++++++++++''')
        continue
    elif loop == "N" or "n":
        print('''Buon proseguimento

                +++++++++++++++++++++++++++++++++++++++++''')
        break