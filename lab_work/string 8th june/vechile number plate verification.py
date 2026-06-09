# Store the input number plate in a variable
plate = "MH12AB4589"

# 1. Extract state code (first two characters)
state_code = plate[0:2]
# 2. Extract district code (next two characters)
district_code = plate[2:4]
# 3. Extract vehicle series (next two characters)
series = plate[4:6]
# 4. Extract vehicle number (last four characters)
number = plate[6:10]

# 5. Count letters and digits separately
letters = 0
digits = 0
for char in plate:
    if char.isalpha(): # Check if character is a letter
        letters += 1
    elif char.isdigit(): # Check if character is a digit
        digits += 1

# 6. Verify the format requirements
is_valid = (
    state_code.isalpha() and     # First 2 are alphabets
    district_code.isdigit() and  # Next 2 are digits
    series.isalpha() and         # Next 2 are alphabets
    number.isdigit()             # Last 4 are digits
)

# Display extracted information
print("State Code:", state_code)
print("District Code:", district_code)
print("Vehicle Series:", series)
print("Vehicle Number:", number)
print("Total Letters:", letters)
print("Total Digits:", digits)

# 7. Display whether the number plate is valid
if is_valid:
    print("Verification Result: The number plate is valid.")
else:
    print("Verification Result: The number plate is invalid.")