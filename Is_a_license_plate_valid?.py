# Old Style = License plates consist in 3 uppercase letters followed by 3 digits.
# New Style = 4 uppercase letters and 3 digits.


while True:
    License_plates_letters = input("Enter 3 or 4 letters of License Plates: ")
    License_plates_letters = License_plates_letters.upper()
    if type(License_plates_letters) != type(""):
        print("Enter only Letters!")
        break
    else:
        try:
            License_plates_numbers = int(input("Enter 3 numbers of License Plates: "))
        except ValueError:
            print("Enter only Numbers!")
            break
        else:
            License_plates_numbers = str(License_plates_numbers)
            if len(License_plates_letters) < 3 or len(License_plates_letters) > 4:
                print("Enter 3 or 4 characters!")
                break
            elif len(License_plates_numbers) != 3:
                print("Enter 3 Digits")
                break
            else:
                License_plates = License_plates_letters + str(License_plates_numbers)
                print("The License Plates: ", License_plates, "is:\n")
                if len(License_plates) == 6:
                    print("Old Style")
                elif len(License_plates) == 7:
                    print("New Style")
    break
