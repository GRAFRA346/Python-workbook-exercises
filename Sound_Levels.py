print("""
       NOISE            DECIBEL LEVELS
    Jackhammer              130db
    Gas Lawnmower           106db
    Alarm Clock             70db
    Quiet Room              40db
""")

Jackhammer = 130
Gas_Lawnmower = 106
Alarm_Clock = 70
Quiet_Room = 40

sl = int(input("Enter a sound level in decibel: "))

if Gas_Lawnmower < sl < Jackhammer:
    print("The sound level is between Gas Lawnmower and Jackhammer")
elif Alarm_Clock < sl < Gas_Lawnmower:
    print("The sound level is between Gas Lawnmower and Alarm Clock")
elif Quiet_Room < sl < Alarm_Clock:
    print("The sound level is between Quiet Room and Alarm Clock")