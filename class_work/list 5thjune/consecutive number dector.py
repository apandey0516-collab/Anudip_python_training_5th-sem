numbers = [4, 5, 6, 10, 11, 15, 16, 17]
consecutive_pairs = []

for i in range(len(numbers) - 1):
    # Check if the next number is exactly 1 greater than the current
    if numbers[i+1] == numbers[i] + 1:
        print(f"{numbers[i]} and {numbers[i+1]} are consecutive")
        # Store as a tuple for the additional challenge
        consecutive_pairs.append((numbers[i], numbers[i+1]))

print("\nConsecutive Pairs List:")
print(consecutive_pairs)