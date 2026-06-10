# Initialize the performance dictionary with Employee IDs and their scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# --- Tasks Implementation ---

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement (score < 60)
# We use a list comprehension to filter scores < 60 and then get the length
improvement_count = len([score for score in performance.values() if score < 60])

# 3. Find the top performer
# max() finds the key (EMP ID) associated with the highest value (score)
top_performer = max(performance, key=performance.get)
top_score = performance[top_performer]

# 4. Calculate average performance score
# sum() adds all scores, len() gets the count of employees
avg_score = sum(performance.values()) / len(performance)

# 5. Create separate lists based on performance categories
excellent = []
good = []
average = []
poor = []

# Loop through the dictionary once to categorize every employee
for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average.append(emp)
    else: # score < 60
        poor.append(emp)

# --- Sample Output Printing ---

print(f"\nTop Performer: {top_performer} ({top_score})")
print(f"Employees Needing Improvement: {improvement_count}")
print(f"Average Score: {avg_score:.1(f)}") # Formatted to 1 decimal place

print(f"\nExcellent:\n{excellent}")
print(f"\nGood:\n{good}")
print(f"\nAverage:\n{average}")
print(f"\nPoor:\n{poor}")