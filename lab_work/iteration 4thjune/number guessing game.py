#program to number guessing game
import random
number_to_guess = random.randint(1, 100) #to generate a random number between 1 and 100 for the user to guess   
attempts = 0#to initialize the attempts variable to keep track of the number of guesses the user has made
max_attempts = 10 #to set a maximum number of attempts to prevent infinite guessing and to add a challenge to the game9
print("Welcome to the Number Guessing Game!") 
print("I have selected a number between 1 and 100. Can you guess it?")
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
if attempts == max_attempts and guess != number_to_guess:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!")  



    
    