#creating a modulue for area and perimeter of 2d figures containing circle,rectangle,square
import math

# Circle

def circle_area(radius):
    return math.pi * (radius ** 2)

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Square
def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

