#WAP find out input the sentence and display the frequency of vowel present in that sentence ignoring the case
sentence = input("Enter a sentence: ")
vowel_count = {}
vowels = "aeiou"
for char in sentence.lower():
    if char in vowels:
        vowel_count[char] = vowel_count.get(char, 0) + 1
print("Frequency of vowels:", vowel_count)