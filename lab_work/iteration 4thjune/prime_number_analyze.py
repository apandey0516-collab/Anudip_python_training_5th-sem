#program to display prime number analyzer
num = int(input("enter a number:"))
if num < 2:
    print(num,"is not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
#----------------------------------------------
#if the number is not prime display all the factors
num = int(input("enter a number:"))
if num < 2:
    print(num,"is not a prime number")
else:
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
    if factors:
        print(num,"is not a prime number")
        print("factors of", num, "are:", factors)
    else:
        
        print(num,"is a prime number")
