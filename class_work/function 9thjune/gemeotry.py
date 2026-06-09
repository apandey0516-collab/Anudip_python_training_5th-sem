#creating and selecting menu of 2d figure and its area and perimeter containg cirle,rectangle,square
import math

def calculate_geometry():
    while True:
        print("\n--- 2D Shape Calculator ---")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Exit")
        
        choice = input("Select a figure (1-4): ")

        if choice == '4':
            print("Exiting the program. Goodbye!")
            break

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            print(f"Area: {math.pi * radius**2:.2f}")
            print(f"Circumference: {2 * math.pi * radius:.2f}")

        elif choice == '2':
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f"Area: {length * width:.2f}")
            print(f"Perimeter: {2 * (length + width):.2f}")

        elif choice == '3':
            side = float(input("Enter the side length: "))
            print(f"Area: {side**2:.2f}")
            print(f"Perimeter: {4 * side:.2f}")

        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    calculate_geometry()

