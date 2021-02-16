somma = 0
n = 0
stop = False

while not stop:
    val = int(input("Enter a value (0 to exit): "))
    if val != 0:
        somma += val
        n += 1
    else:
        stop = True

media = somma / n
print("The average is {}.".format(media))

