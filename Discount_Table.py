#  This program print a table discount for 5 prices


for i in range(5):
    original = 5 * i + 4.95
    discounted = original * 0.6
    total = original - discounted
    print("Original price: ${} \t Discounted: ${} \t Total: ${}".format(round(original, 2),
                                                                        round(discounted, 2),
                                                                        round(total, 2)))

