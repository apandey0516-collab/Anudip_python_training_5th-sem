#program to display pin verification
pin=1234 #to set a predefined pin for verification 
while True: #to create an infinite loop for pin verification until the correct pin is entered
    user_pin=int(input("Enter your pin: ")) #to get the pin input from the user and convert it to an integer for comparison
    if user_pin==pin:#to check if the entered pin matches the predefined pin
        print("Pin verified successfully")#to display a message indicating that the pin has been verified successfully
        break #to exit the loop if the pin is verified successfully
    else: #to handle incorrect pin input
        print("Incorrect pin, try again") #to display a message indicating that the entered pin is incorrect and to prompt the user to try again