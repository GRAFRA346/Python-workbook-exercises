from Convert_an_integer_to_Its_ordinal_number import convert


def displayVerse(n):
    print("On the", convert(n), "day of Christmas")
    print("my true love sent to me:")

    if n >= 12:
        print("Twelve drummers drumming\n")
    elif n >= 11:
        print("Eleven pipers piping\n")
    elif n >= 10:
        print("Ten lords a-leaping\n")
    elif n >= 9:
        print("Nine ladies dancing\n")
    elif n >= 8:
        print("Eight maids a-milking\n")
    elif n >= 7:
        print("Seven swans a-swimming\n")
    elif n >= 6:
        print("Six geese a-laying\n")
    elif n >= 5:
        print("Five golden rings\n")
    elif n >= 4:
        print("Four calling birds\n")
    elif n >= 3:
        print("Three french hens\n")
    elif n >= 2:
        print("Two turtle doves, and\n")
    elif n == 1:
        print("partridge in a pear tree.\n")


def main():
    for verse in range(1, 13):
        print("[ Verse", verse, "]")
        displayVerse(verse)


main()
