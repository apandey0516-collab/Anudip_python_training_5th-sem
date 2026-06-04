#program to display armstrong number checker
num = int(input("enter a number:")) #to get the number from the user
sum =0 #to initialize the sum variable to store the sum of the cubes of the digits
temp = num #to store the original number in a temporary variable for later comparison
digits = len(str(num))#to calculate the number of digits in the original number, which is used to determine the power to which each digit is raised (in this case, 3 for armstrong numbers)
while temp > 0: #to extract each digit and calculate the sum of the cubes of the digits
    digit = temp % 10  #to get the last digit
    sum += digit ** digits #to calculate the sum of the cubes of the digits
    temp //= 10 #to remove the last digit
if sum == num: #to check whether the sum of the cubes of the digits is equal to the original number
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")