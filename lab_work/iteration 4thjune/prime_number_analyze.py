#program to display prime number analyzer
num = int(input("enter a number:"))#to get the number from the user
if num < 2:#to check if the number is less than 2, which is not a prime number
    print(num,"is not a prime number")
else:
    for i in range(2,num):#to check if the number is divisible by any integer from 2 to num-1
        if num % i == 0:#if the number is divisible by any of these integers, it is not a prime number
            print(num,"is not a prime number")#to display a message indicating that the number is not a prime number
            break #to exit the loop if a divisor is found
    else: #if the loop completes without finding any divisors, the number is a prime number
        print(num,"is a prime number")
#----------------------------------------------
#if the number is not prime display all the factors
num = int(input("enter a number:"))#to get the number from the user
if num < 2:#to check if the number is less than 2, which is not a prime number
    print(num,"is not a prime number")
else:
    factors = []#to initialize an empty list to store the factors of the number
    for i in range(1,num//2 + 1):#to check for factors from 1 to num//2 (inclusive), since a number cannot have factors greater than its half
     if num % i == 0:
            factors.append(i)
    if factors:
        print(num,"is not a prime number")
        print("factors of", num, "are:", factors)
    else:
        
        print(num,"is a prime number")
