import math # Import math module to use the value of pi

# Functions for Circle
def circle_area(radius):
    return math.pi * radius ** 2 # Calculate area: π * r^2

def circle_perimeter(radius):
    return 2 * math.pi * radius # Calculate circumference: 2 * π * r

# Functions for Square
def square_area(side):
    return side ** 2 # Calculate area: side * side

def square_perimeter(side):
    return 4 * side # Calculate perimeter: 4 * side

# Functions for Rectangle
def rectangle_area(length, width):
    return length * width # Calculate area: length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width) # Calculate perimeter: 2 * (length + width)

import geometry # Import the custom geometry module

def get_positive_input(prompt):
    # Loop until the user provides a valid positive number
    while True:
        try:
            value = float(input(prompt)) # Convert input to a float
            if value > 0: # Check if the number is positive
                return value # Return valid number
            print("Error: Please enter a positive number.") # Handle non-positive input
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.") # Handle non-numeric input

def main():
    while True: # Outer loop for selecting the figure
        print("\nSelect the Figure:\n1. Circle\n2. Square\n3. Rectangle\n4. Exit")
        choice = input("Enter your choice: ") # Get user selection

        if choice == '4': # Exit the entire program
            print("Exiting application. Goodbye!")
            break
        
        if choice not in ['1', '2', '3']: # Validate menu choice
            print("Invalid choice. Please try again.")
            continue

        # Step 2: Accept Inputs based on selection
        if choice == '1':
            r = get_positive_input("Enter radius: ")
        elif choice == '2':
            s = get_positive_input("Enter side: ")
        elif choice == '3':
            l = get_positive_input("Enter length: ")
            w = get_positive_input("Enter width: ")

        # Step 4: Loop for repeating operations on the same figure
        while True:
            print("\nSelect Operation:\n1. Area\n2. Perimeter\n3. Change Figure")
            op_choice = input("Enter your choice: ")

            if op_choice == '1': # Calculate Area
                if choice == '1': print(f"Area of Circle = {geometry.circle_area(r):.2f}")
                elif choice == '2': print(f"Area of Square = {geometry.square_area(s):.2f}")
                elif choice == '3': print(f"Area of Rectangle = {geometry.rectangle_area(l, w):.2f}")
            
            elif op_choice == '2': # Calculate Perimeter
                if choice == '1': print(f"Perimeter of Circle = {geometry.circle_perimeter(r):.2f}")
                elif choice == '2': print(f"Perimeter of Square = {geometry.square_perimeter(s):.2f}")
                elif choice == '3': print(f"Perimeter of Rectangle = {geometry.rectangle_perimeter(l, w):.2f}")

            elif op_choice == '3': # Go back to the main figure menu
                break
            else:
                print("Invalid choice.")

            # Ask user if they want another operation on the same figure
            repeat = input("Do you want to perform another operation on the same figure? (Y/N): ").upper()
            if repeat != 'Y':
                break

        # Step 5: Ask user if they want to continue with the application
        cont = input("Do you want to continue using the application? (Y/N): ").upper()
        if cont != 'Y':
            print("Terminating program...")
            return # Exit the main function

if __name__ == "__main__":
    main() # Execute the main function