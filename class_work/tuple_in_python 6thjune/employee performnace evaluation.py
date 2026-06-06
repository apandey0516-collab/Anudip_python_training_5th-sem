#craeting employee data
employees = (
("E101", "Anuj", 92),
("E102", "Rahul", 76),
("E103", "Priya", 58),
("E104", "Neha", 88),
("E105", "Amit", 45)
)
#display employee scoring 80 above
print("employees scoring 80 or above:")
for emp in employees:
    if emp[2] >= 80:
        print(f"{emp[0]} {emp[1]} {emp[2]}")
# 2. Count employees needing improvement (score below 60)
improvement_count = sum(1 for emp in employees if emp[2] < 60)
print(f"\nEmployees Needing Improvement: {improvement_count}")

# 3. Find the employee with the highest score
highest_performer = max(employees, key=lambda x: x[2])
print(f"\nHighest Performer:\n{highest_performer[0]} {highest_performer[1]} {highest_performer[2]}")

# 4. Create a list of names for employees scoring above 75
high_performers = [emp[1] for emp in employees if emp[2] > 75]
print(f"\nHigh Performers:\n{high_performers}")

# 5. Display performance category for each employee
print("\nPerformance Categories:")
for name, score in [(e[1], e[2]) for e in employees]:
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(f"{name} -> {category}")        
        
        
        
#count the number of employee who need improvement (score below 60)
#print("count the number of employee who need improvement (score below 60)")


