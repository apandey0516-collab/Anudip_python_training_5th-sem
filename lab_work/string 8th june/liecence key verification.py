# Define the input license key string
license_key = "ABCD-EFGH-IJKL-MNOP"

# Split the string into a list using the hyphen '-' as a separator
groups = license_key.split('-')

# Task 1: Count the number of groups in the list
num_groups = len(groups)

# Task 2: Check if every group in the list has exactly 4 characters
# It returns True only if all groups meet the condition
all_four_chars = all(len(group) == 4 for group in groups)

# Task 5 & 6: Join the list of groups back together without hyphens
merged_key = "".join(groups)

# Task 3: Count total letters by calculating the length of the merged string
total_letters = len(merged_key)

# Task 4: Count vowels by checking each character against a set of vowels
vowels = "AEIOUaeiou"
total_vowels = sum(1 for char in merged_key if char in vowels)

# Task 7: Determine if the format is valid (4 groups AND each group has 4 chars)
is_valid = num_groups == 4 and all_four_chars

# --- Display Output ---

# Print the original license key
print(f"License Key:\n{license_key}\n")

# Print the list containing all groups (Task 6)
print(f"Groups:\n{groups}\n")

# Print the total number of groups (Task 1)
print(f"Number of Groups: {num_groups}\n")

# Print the total letter count (Task 3)
print(f"Total Letters: {total_letters}")

# Print the total vowel count (Task 4)
print(f"Total Vowels: {total_vowels}\n")

# Print the key without hyphens (Task 5)
print(f"Merged Key:\n{merged_key}\n")

# Print whether the key format is valid (Task 7)
status = "Valid" if is_valid else "Invalid"
print(f"License Key Status: {status}")