#program to display palindrome and reverse number
#program to check a number is palindrome and reverse number
num = int(input("Enter a number: "))

original = num
reverse = 0
#condition for non-negative
while num > 0:
    #for extracting last digit
    digit = num % 10
    #reversed number updation
    reverse = reverse * 10 + digit
    #number updation after extracting last digit
    num = num // 10
#printing obtained reversed number
print("Reverse:", reverse)
#checking palindrome condition
if reverse == original:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")