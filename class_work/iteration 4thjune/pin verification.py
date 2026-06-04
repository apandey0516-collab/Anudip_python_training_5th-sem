#program to display pin verification
pin=1234
while True:
    user_pin=int(input("Enter your pin: "))
    if user_pin==pin:
        print("Pin verified successfully")
        break
    else:
        print("Incorrect pin, try again")