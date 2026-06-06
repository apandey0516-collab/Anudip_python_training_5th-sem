# Accept three sides from the user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check the Triangle Inequality Theorem
# Sum of any two sides must be greater than the third side
if (a + b > c) and (a + c > b) and (b + c > a):
    # If all conditions are true, it is a valid triangle
    print("Valid Triangle")
else:
    # If any condition fails, it is not a valid triangle
    print("Not a Valid Triangle")