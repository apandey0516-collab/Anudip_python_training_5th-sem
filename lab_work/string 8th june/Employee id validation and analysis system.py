# The input Employee ID
emp_id = "EMP2026ANUJ458"

# 1 & 2. Initialize counters for letters and digits
upper_count = 0
digit_count = 0
digit_list = []

# Loop through every character in the ID to count and collect digits
for char in emp_id:
    if char.isupper():          # Check if the character is an uppercase letter
        upper_count += 1        # Add 1 to the uppercase counter
    elif char.isdigit():        # Check if the character is a number
        digit_count += 1        # Add 1 to the digit counter
        digit_list.append(int(char)) # Add the number to our list

# 3. Extract joining year (the 4 digits after 'EMP')
joining_year = emp_id[3:7]

# 4. Extract employee name (the letters between the year and the last 3 digits)
emp_name = emp_id[7:-3]

# 5. Validation Logic
starts_with_emp = emp_id.startswith("EMP")      # Check if it starts with 'EMP'
year_is_4_digits = joining_year.isdigit()       # Check if the year part is numeric
ends_with_3_digits = emp_id[-3:].isdigit()      # Check if the last 3 characters are digits

# 7. Calculate the sum of all digits in the list
total_sum = sum(digit_list)

# 8. Determine if the ID is valid based on the rules
is_valid = starts_with_emp and year_is_4_digits and ends_with_3_digits

# --- Displaying the Results ---
print(f"Employee ID: {emp_id}")
print(f"\nUppercase Letters: {upper_count}")
print(f"Digits: {digit_count}")
print(f"\nJoining Year: {joining_year}")
print(f"Employee Name: {emp_name}")
print(f"\nDigit List: {digit_list}")
print(f"Sum of Digits: {total_sum}")
print(f"\nID Status: {'Valid' if is_valid else 'Invalid'}")