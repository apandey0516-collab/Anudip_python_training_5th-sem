# The input message to be analyzed
text = "AAABBBCCCDDDAAA"

# 1. Count occurrences & 2. Create a dictionary of frequencies
# We use a dictionary where keys are characters and values are counts
freq = {}
for char in text:
    # Get current count or default to 0, then add 1
    freq[char] = freq.get(char, 0) + 1

# 3. Display unique characters (the keys of our frequency dictionary)
unique_chars = list(freq.keys())

# 4. Find the most frequent character
# We find the key with the maximum value in the dictionary
most_frequent = max(freq, key=freq.get)

# 5. Create a compressed output (Run-Length Encoding style)
# We iterate through the string and group consecutive identical characters
compressed = ""
if text:
    count = 1
    for i in range(1, len(text)):
        # If current char matches the previous one, increment count
        if text[i] == text[i-1]:
            count += 1
        else:
            # If it differs, append the previous char and its count
            compressed += f"{text[i-1]}{count}"
            count = 1
    # Append the last character group
    compressed += f"{text[-1]}{count}"

# 6. Calculate compression ratio
# Ratio = (Compressed Length / Original Length)
original_len = len(text)
compressed_len = len(compressed)
ratio = compressed_len / original_len

# --- Displaying Results ---
print(f"Original Text: {text}")
print("\nCharacter Frequencies:")
for char, count in freq.items():
    print(f"{char} -> {count}")

print(f"\nUnique Characters: {unique_chars}")
print(f"Most Frequent Character: {most_frequent}")
print(f"Compressed Output: {compressed}")
print(f"Original Length: {original_len}")
print(f"Compressed Length: {compressed_len}")
print(f"Compression Ratio: {ratio:.2f}")