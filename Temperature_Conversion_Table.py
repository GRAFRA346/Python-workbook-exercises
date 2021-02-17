print("""
-Temperature Conversion Table-

|  CELSIUS   |   FAHRENHEIT  |""")


for tc in range(0, 110, 10):
    tf = int((tc * 9/5) + 32)
    print("Celsius: {}°C".format(round(tc, 2)), "|", "Fahrenheit: {}°F".format(tf))

