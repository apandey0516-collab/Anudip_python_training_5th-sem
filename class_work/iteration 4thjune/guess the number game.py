#program to display gueess the number game
while(True): #to create an infinite loop for the guessing game until the user guesses the correct number
    number=int(input("Guess the number")) #to get the user's guess as input and convert it to an integer for comparison
    if(number==7): #to check if the user's guess is correct by comparing it to the predefined correct number (7 in this case)
        print("Congratulations! You guessed the correct number") #to display a congratulatory message if the user's guess is correct
        break #to exit the loop if the user has guessed the correct number
    else: #to handle the case where the user's guess is incorrect
        print("Wrong guess. Try again") #to display a message indicating that the user's guess is incorrect and to prompt them to try again
