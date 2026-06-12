# Function to determine grade based on marks
def get_grade(marks):
    if marks >= 90: return 'A'
    elif marks >= 75: return 'B'
    elif marks >= 40: return 'C'
    else: return 'F'

# --- 1. Display all student records ---
print("--- Student Records ---")
# Open results.txt in read mode
with open('results.txt', 'r') as file:
    # Read each line one by one
    lines = file.readlines()
    records = [] # List to store data for further processing
    
    for line in lines:
        # Remove newline and split by comma
        data = line.strip().split(',')
        sid, name, marks = data[0], data[1], int(data[2])
        records.append([sid, name, marks])
        print(f"ID: {sid}, Name: {name}, Marks: {marks}")

# --- 2. Search a student using Student ID ---
search_id = input("\nEnter Student ID to search: ")
found = False
for r in records:
    if r[0] == search_id:
        print(f"Student Found: {r[1]}, Marks: {r[2]}")
        found = True
        break
if not found: print("Student not found.")

# --- 3. Find topper and lowest scorer ---
# Use max and min functions with a lambda key to look at marks
topper = max(records, key=lambda x: x[2])
lowest = min(records, key=lambda x: x[2])
print(f"\nTopper: {topper[1]} ({topper[2]})")
print(f"Lowest Scorer: {lowest[1]} ({lowest[2]})")

# --- 4. Calculate class average ---
# Sum all marks and divide by the number of students
total_marks = sum(r[2] for r in records)
average = total_marks / len(records)
print(f"\nClass Average: {average:.2/f}")

# --- 5. Count pass and fail students ---
# Based on the grade scale, <40 is a fail (F)
pass_count = sum(1 for r in records if r[2] >= 40)
fail_count = len(records) - pass_count
print(f"Pass: {pass_count}, Fail: {fail_count}")

# --- 6 & 7. Generate grades and write to grades.txt ---
# Open a new file in write mode
with open('grades.txt', 'w') as outfile:
    for r in records:
        grade = get_grade(r[2])
        # Format the string for the new file
        report = f"{r[0]},{r[1]},{r[2]},{grade}\n"
        outfile.write(report)

print("\nGrade report successfully generated in 'grades.txt'.")