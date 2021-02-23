

def main():
    a = int(input("Enter a integer to convert, between 1 and 12: "))
    print("The ordinal number of this integer is: ", convert(a))


def convert(ordinal):
    if 1 < ordinal <= 12:
        if ordinal == 1:
            return "First"
        elif ordinal == 2:
            return "Second"
        elif ordinal == 3:
            return "Third"
        elif ordinal == 4:
            return "Fourth"
        elif ordinal == 5:
            return "Fifth"
        elif ordinal == 6:
            return "Sixth"
        elif ordinal == 7:
            return "Seventh"
        elif ordinal == 8:
            return "Eighth"
        elif ordinal == 9:
            return "Ninth"
        elif ordinal == 10:
            return "Tenth"
        elif ordinal == 11:
            return "Eleventh"
        elif ordinal == 12:
            return "Twelfth"
        else:
            return ""

main()