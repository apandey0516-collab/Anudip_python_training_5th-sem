# The input text from the customer review
text = "This product is excellent excellent excellent and very useful"

# 1. Split the text into a list of individual words
words = text.split()
print(f"Total Words: {len(words)}")

# 2. Create a dictionary to count how many times each word appears
frequencies = {}
for word in words:
    # If the word is already in the dictionary, add 1 to its count
    # If not, start the count at 1
    frequencies[word] = frequencies.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in frequencies.items():
    print(f"{word} -> {count}")

# 3. Find the word that appears the most
# This looks at the dictionary and finds the key with the highest value
most_frequent = max(frequencies, key=frequencies.get)
print(f"\nMost Frequent Word: {most_frequent}")

# 4. Find words that appear exactly one time
once_words = [word for word, count in frequencies.items() if count == 1]
print(f"\nWords Appearing Once: {once_words}")

# 5. Count words that are longer than 5 characters
long_words_count = len([word for word in words if len(word) > 5])
print(f"Words with more than 5 characters: {long_words_count}")

# 6. Show the list of words in reverse order
reversed_words = words[::-1]
print(f"Words in reverse: {reversed_words}")

# 7. Create a list of words where each word appears only once (no duplicates)
unique_words = list(frequencies.keys())
print(f"Unique Words: {unique_words}")
