#program to display login system
username="admin123" #to set a predefined username for login
password="password123" #to set a predefined password for login
while True: #to create an infinite loop for login attempts until the correct credentials are entered
    user_name=input("Enter your username: ") #to get the username input from the user
    user_password=input("Enter your password: ") #to get the password input from the user
    if user_name==username and user_password==password: #to check if the entered username and password match the predefined credentials
        print("Login successful") #to display a message indicating that the login was successful
        break #to exit the loop if the login is successful
    else: #to handle incorrect login attempts
        print("Incorrect username or password, try again") #to display a message indicating that the entered credentials are incorrect and to prompt the user to try again