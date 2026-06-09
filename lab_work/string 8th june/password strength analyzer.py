# Ask the user to type in their password
password = input("Enter your password: ")

# Set up counters for each type of character
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Lists to store the specific characters we find
digits_found = []
specials_found = []

# Loop through every single character in the password
for char in password:
    # If the character is uppercase, increase the upper count
    if char.isupper():
        upper_count += 1
    # If the character is lowercase, increase the lower count
    elif char.islower():
        lower_count += 1
    # If it is a number, increase digit count and add it to our list
    elif char.isdigit():
        digit_count += 1
        digits_found.append(char)
    # If it isn't any of the above, it's a special character
    else:
        special_count += 1
        specials_found.append(char)

# Check if the password meets all the "Strong" requirements
is_long_enough = len(password) >= 8
has_upper = upper_count >= 1
has_lower = lower_count >= 1
has_digit = digit_count >= 1
has_special = special_count >= 1

# Print the final counts
print(f"\nPassword: {password}")
print(f"Uppercase Letters: {upper_count}")
print(f"Lowercase Letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_count}")

# Print the lists of specific characters found
print(f"\nDigits Found: {digits_found}")
print(f"Special Characters Found: {specials_found}")

# Decide the strength based on the rules
if is_long_enough and has_upper and has_lower and has_digit and has_special:
    print("\nPassword Strength: Strong")
elif is_long_enough and (has_upper or has_lower) and has_digit:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Weak")