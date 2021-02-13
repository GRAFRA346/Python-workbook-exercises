OddLetter = ["a", "c", "e", "g"]
EvenLetter = ["b", "d", "f", "h"]
OddNumber = [1, 3, 5, 7]
EvenNumber = [2, 4, 6, 8]

print("""Welcome, compute the square color:
   - Enter 0 to close the program -
""")
while True:
    letter = input("Enter the letter: ")
    if letter == "0":
        print("!!!Program Closing!!!")
        break
    else:
        try:
            number = int(input("Enter the number: "))
        except ValueError:
            print("Enter an integer!")
            break
        if letter not in OddLetter and EvenLetter:
            print("Accepted letters go up to H")
            break
        elif number not in OddNumber and EvenNumber:
            print("Accepted numbers go up to 8")
            break
        else:
            if letter.lower() in OddLetter and number in OddNumber:
                print("Square color is black")
            elif letter.lower() in EvenLetter and number in OddNumber:
                print("Square color is white")
            elif letter.lower() in OddLetter and number in EvenNumber:
                print("Square color is white")
            elif letter.lower() in EvenLetter and number in EvenNumber:
                print("Square color is black")
