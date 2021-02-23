def main():
    a = int(input("Enter a integer to convert, between 1 and 12: "))
    print("The ordinal number of this integer is: ", convert(a))


def convert(ordinal):
    # Dictionary 
    d = {1: "First", 2: "Second", 3: "Third", 4: "Fourth",
         5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth",
         9: "Ninth", 10: "Tenth", 11: "Eleventh", 12: "Twelfth"}
    
    if ordinal in d:
        return d[ordinal]
    else:
        return ""


main()
