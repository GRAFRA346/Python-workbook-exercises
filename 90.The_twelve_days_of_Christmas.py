from Convert_an_integer_to_Its_ordinal_number import convert


def displayVerse(n):
    print("On the", convert(n), "day of Christmas")
    print("my true love sent to me:")

    if n >= 12:
        print("Twelve drummers drumming")
    elif n >= 11:
        print("Eleven pipers piping")
    elif n >= 10:
        print("Ten lords a-leaping")
    elif n >= 9:
        print("Nine ladies dancing")
    elif n >= 8:
        print("Eight maids a-milking")
    elif n >= 7:
        print("Seven swans a-swimming")
    elif n >= 6:
        print("Six geese a-laying")
    elif n >= 5:
        print("Five golden rings")
    elif n >= 4:
        print("Four calling birds")
    elif n >= 3:
        print("Three french hens")
    elif n >= 2:
        print("Two turtle doves, and")
    elif n == 1:
        print("partridge in a pear tree.")


def main():
    for verse in range(1, 13):
        print("\n[ Verse", verse, "]")
        displayVerse(verse)


main()
