# Create a dictionary to store employee IDs as keys and their scores as values
performance = {
    "EMP101": 92, "EMP102": 78, "EMP103": 45, "EMP104": 88, "EMP105": 97,
    "EMP106": 56, "EMP107": 81, "EMP108": 64, "EMP109": 39, "EMP110": 73
}

# --- Task 1: Display employees scoring above 80 ---
print("Employees Scoring Above 80:")
for emp, score in performance.items():  # Look at every employee and their score
    if score > 80:                      # Check if the score is greater than 80
        print(emp)                      # If yes, print the employee ID

# --- Task 2: Count employees needing improvement (score < 60) ---
# Create a list of employees with scores under 60 and count how many are in it
needs_imp = len([emp for emp, score in performance.items() if score < 60])
print(f"\nEmployees Needing Improvement: {needs_imp}")

# --- Task 3: Find the top performer ---
# Find the key (Employee ID) that has the highest value (Score)
top_emp = max(performance, key=performance.get)
print(f"Top Performer: {top_emp} ({performance[top_emp]})")

# --- Task 4: Calculate average performance score ---
# Sum all scores and divide by the total number of employees
average = sum(performance.values()) / len(performance)
print(f"Average Score: {average}")

# --- Task 5: Create separate lists based on score categories ---
excellent = []  # >= 90
good = []       # 75-89
average_l = []  # 60-74
poor = []       # < 60

for emp, score in performance.items():  # Go through the dictionary one by one
    if score >= 90:
        excellent.append(emp)           # Add to Excellent list
    elif 75 <= score <= 89:
        good.append(emp)                # Add to Good list
    elif 60 <= score <= 74:
        average_l.append(emp)           # Add to Average list
    else:
        poor.append(emp)                # Add to Poor list (below 60)

# Print the final categorized lists
print(f"\nExcellent: {excellent}")
print(f"Good: {good}")