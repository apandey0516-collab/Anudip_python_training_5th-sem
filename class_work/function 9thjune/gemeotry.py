#creating and selecting menu of 2d figure and its area and perimeter containg cirle,rectangle,square
# Import the math module to use mathematical constants like pi
import math
# Define a function named calculate_geometry to hold our code
def calculate_geometry():
    # Start a loop that runs forever until we choose to stop it
    while True:
        # Print a blank line and the title of our program
        print("\n--- 2D Shape Calculator ---")
        # Print the first option for the user
        print("1. Circle")
        # Print the second option for the user
        print("2. Rectangle")
        # Print the third option for the user
        print("3. Square")
        # Print the fourth option to close the program
        print("4. Exit")

        # Ask the user to type a number from 1 to 4 and save it in 'choice'
        choice = input("Select a figure (1-4): ")

        # Check if the user typed '4' to leave the program
        if choice == "4":
            # Print a goodbye message to the user
            print("Exiting the program. Goodbye!")
            # Stop the loop and end the program
            break

        # Check if the user typed '1' to choose the circle
        if choice == "1":
            # Ask for the radius, convert it to a decimal number, and save it
            radius = float(input("Enter the radius of the circle: "))
            # Calculate and print the area, rounded to 2 decimal places
            print(f"Area: {math.pi * radius**2:.2f}")
            # Calculate and print the circumference, rounded to 2 decimal places
            print(f"Circumference: {2 * math.pi * radius:.2f}")

        # Check if the user typed '2' to choose the rectangle
        elif choice == "2":
            # Ask for the length, convert it to a decimal number, and save it
            length = float(input("Enter the length: "))
            # Ask for the width, convert it to a decimal number, and save it
            width = float(input("Enter the width: "))
            # Calculate and print the area, rounded to 2 decimal places
            print(f"Area: {length * width:.2f}")
            # Calculate and print the perimeter, rounded to 2 decimal places
            print(f"Perimeter: {2 * (length + width):.2f}")

        # Check if the user typed '3' to choose the square
        elif choice == "3":
            # Ask for the side length, convert it to a decimal number, and save it
            side = float(input("Enter the side length: "))
            # Calculate and print the area, rounded to 2 decimal places
            print(f"Area: {side**2:.2f}")
            # Calculate and print the perimeter, rounded to 2 decimal places
            print(f"Perimeter: {4 * side:.2f}")

        # Run this part if the user typed anything other than 1, 2, 3, or 4
        else:
            # Tell the user their choice was wrong and to try again
            print("Invalid selection. Please try again.")


# Check if this specific file is the one being directly run by Python
if __name__ == "__main__":
    # Call and run the calculate_geometry function we defined above
    calculate_geometry()
