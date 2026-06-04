#program to verify strong number
num = int(input("enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum += factorial
    temp //= 10
#check the weather the sum of factorial of digits is equal to the original number or not
if sum == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")