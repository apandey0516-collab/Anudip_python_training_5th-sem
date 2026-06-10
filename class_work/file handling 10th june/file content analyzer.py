# Open the file 'article.txt' in read mode ('r')
with open('article.txt', 'r') as file:
    # Read the entire content of the file into a single string variable
    content = file.read()
    
    # Reset the file pointer to the beginning to count lines accurately
    file.seek(0)
    # Read all lines into a list and get the length of that list for the line count
    num_lines = len(file.readlines())

# Define a string containing all vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Use a list comprehension to find every character in content that is a vowel, then get its length
num_vowels = len([char for char in content if char in vowels])

# Get the total number of characters in the file using the len() function on the content string
num_chars = len(content)

# Print the header of the report
print("File Analysis Report")
# Print a blank line for formatting
print()
# Print the total count of vowels
print(f"Total Number of Vowels : {num_vowels}")
# Print the total count of characters
print(f"Total Number of Characters: {num_chars}")
# Print the total count of lines
print(f"Total Number of Lines : {num_lines}")