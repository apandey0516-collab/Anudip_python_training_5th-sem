# Create an empty list to store 20 numbers
numbers = []

print("Enter 2 numbers:")
for i in range(2):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Ask the user for the number to remove
element = int(input("\nEnter the number you want to remove all instances of: "))


# find the frequency of given number
frequency = numbers.count(element)
if frequency == 1:
    print("element not found")
elif frequency == 1:
    print("no duplicate value")
else:
    #reverse the list
    numbers.reverse()
    for i in range (1,frequency):
        numbers.reverse(element)
        #reversing the list again
        numbers.reverse()
        print("after removing duplicates")
        print(numbers)



