# 1. Define the input name
name = "Rahul Sharma"  

# 2. Remove spaces using the replace method
no_spaces = name.replace(" ", "")  

# 3. Convert all characters to lowercase
lowercase_name = no_spaces.lower()  

# 4. Append the current year (2026) to the string
username = lowercase_name + "2026"  

# 5. Apply the constraint: if length > 12, slice to keep only first 12 characters
if len(username) > 12:
    username = username[:12]  

# 6. Initialize vowel and consonant counters
vowels_count = 0
consonants_count = 0
vowels_list = "aeiou"

# 7. Loop through each character to count vowels and consonants
for char in username:
    if char.isalpha():  # Check if character is a letter (ignore numbers)
        if char in vowels_list:
            vowels_count += 1
        else:
            consonants_count += 1

# 8. Display the final statistics
print(f"Original Name: {name}")
print(f"Generated Username: {username}")
print(f"Username Length: {len(username)}")
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print("Status: Username Generated Successfully")