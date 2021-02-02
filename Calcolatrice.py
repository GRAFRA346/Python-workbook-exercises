from math import sqrt

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
        -Per calcolare Radice Quadrata seleziona 6;
        -Per uscire dal programma puoi digitare ESC;
        ''')
    def Addizzione():
        print("\nHai scelto: Addizione")
        print('''
        -INSERISCI DEI NUMERI
        -INSERISCI 0 PER TERMINARE!''')
        n = float(input("Inserisci numero:"))
        somma = n
        while n != 0:
            n = float(input("Inserisci il numero:"))
            somma += n
        print("La somma è:", somma)
    def Sottrazione():
        print("\nHai scelto: Sottrazione")
        print('''
        -INSERISCI DEI NUMERI
        -INSERISCI 0 PER TERMINARE!''')
        n = float(input("Inserisci numero:"))
        sottrai = n
        while n != 0:
            n = float(input("Inserisci il numero:"))
            sottrai -= n
        print("Il risultato è:", sottrai)
    def Moltiplicazione():
        print("\nHai scelto: Moltiplicazione\n")
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato della somma è: " + str(a * b))
    def Divisione():
        try:
            print("\nHai scelto: Divisione\n")
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            print("Il risultato della somma è: " + str(a / b))
        except ZeroDivisionError:
            print("Non puoi dividere per Zero!! Riprova")
    def Calcolo_Esponenziale():
        print("\nHai scelto: Calcolo Esponenziale\n")
        a = float(input("Inserisci la base: "))
        b = float(input("Inserisci l\'esponente: "))
        print("Il risultato della somma è: " + str(a ** b))
    def Radice_Quadrata():
        print("\nHai scelto: Calcolo Radice Quadrata\n")
        a = float(input("Inserisci numero: "))
        print("La radice quadrata di " + str(a), "è: " + str(sqrt(a)))

    scelta = input("Inserisci il numero corrispondete all\'azione desiderata -->")

    if scelta == "1":
        Addizzione()
    elif scelta == "2":
        Sottrazione()
    elif scelta == "3":
        Moltiplicazione()
    elif scelta == "4":
        Divisione()
    elif scelta == "5":
        Calcolo_Esponenziale()
    elif scelta == "6":
        Radice_Quadrata()
    elif scelta == "ESC" or scelta == "esc":
        print('''L\'apllicazione verrà chiusa!
        
+++++++++++++++++++++++++++++++++++++++++''')
        break
    elif scelta != "1" or "2" or "3" or "4" or "5" or "6":
        print("Opzione Errata")

    loop = input("\nDesideri continuare ad usare l\'applicazione? S/N")
    if loop == "S" or loop == "s":
        print('''Torno al menù principale

+++++++++++++++++++++++++++++++++++++++++''')
        continue
    elif loop == "N" or "n":
        print('''Buon proseguimento

+++++++++++++++++++++++++++++++++++++++++''')
        break
