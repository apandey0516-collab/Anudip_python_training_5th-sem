#import module numeric calculations
from numeric_calculations import add, subtract
#----------------------------------
#main program
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
#to calculate addition
add = 0
subtract = 0
print("Addition : ",add(num1, num2))
#to calculate subtraction
print("Difference between",num1," and ",num2,"is : ",subtract(num1, num2))