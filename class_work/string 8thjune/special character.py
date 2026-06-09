# Program to count special characters in a sentence
sentence = input("Enter a sentence: ")
special_count = 0
for char in sentence:
    if char in "!@#$%^&*( )_+-=[]{}|;':\",.<>?/":
        special_count += 1    
print("Number of special characters:", special_count)