# Store the message in a variable
message = "Python is awesome and Python is easy to learn"

# 1. Count total characters (including spaces)
total_chars = len(message)

# 2. Split the message into a list of individual words
words = message.split()
total_words = len(words)

# 3. Find the longest word in the list
longest_word = max(words, key=len)

# 4. Find the shortest word in the list
shortest_word = min(words, key=len)

# 5. Count how many times the specific word "Python" appears
python_count = words.count("Python")

# 6. Create a list of words that have more than 4 letters
long_words = [word for word in words if len(word) > 4]

# 7. Create a list of words that start with a vowel (a, e, i, o, u)
vowel_start_words = [word for word in words if word[0].lower() in "aeiou"]

# 8. Count vowels and consonants
vowels_count = 0
consonants_count = 0
vowels_list = "aeiouAEIOU"

# Go through every character in the message
for char in message:
    # Check if the character is a letter
    if char.isalpha():
        # If it is a vowel, add 1 to vowel count
        if char in vowels_list:
            vowels_count += 1
        # If it is a letter but not a vowel, it is a consonant
        else:
            consonants_count += 1

# --- Displaying the Results ---
print(f"Message: {message}")
print(f"Total Characters: {total_chars}")
print(f"Total Words: {total_words}")
print(f"Longest Word: {longest_word}")
print(f"Shortest Word: {shortest_word}")
print(f"Occurrences of Python: {python_count}")
print(f"Words Longer Than 4 Characters: {long_words}")
print(f"Words Starting With a Vowel: {vowel_start_words}")
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")