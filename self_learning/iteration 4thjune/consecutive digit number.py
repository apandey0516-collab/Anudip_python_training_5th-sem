def check_consecutive(number):
    # Convert number to string to iterate through digits
    num_str = str(number)
    
    # Iterate from the second digit to the end
    for i in range(1, len(num_str)):
        # Check if current digit is exactly 1 greater than previous
        if int(num_str[i]) != int(num_str[i-1]) + 1:
            return "Not a Consecutive Number"
            
    return "Consecutive Number"

# Input
user_input = input("Enter a number: ")
print(check_consecutive(user_input))