scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries (50-99) and centuries (100+)
half_centuries = len([s for s in scores if 50 <= s < 100])
centuries = len([s for s in scores if s >= 100])

# 2. Find the highest score
highest_score = max(scores)

# 3. Display all scores below 20
scores_below_20 = [s for s in scores if s < 20]

# 4. Calculate the average score
average_score = sum(scores) / len(scores)

# Display Results
print(f"Half-centuries: {half_centuries}")
print(f"Centuries: {centuries}")
print(f"Highest Score: {highest_score}")
print(f"Scores below 20: {scores_below_20}")
print(f"Average Score: {average_score}")