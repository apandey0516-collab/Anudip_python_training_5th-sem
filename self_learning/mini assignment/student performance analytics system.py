#1. Student Performance Analytics System
#Problem Statement
#A coaching institute wants to analyze student performance.
#Store details of at least 30 students in a dictionary.
#Example Structure
#students = {
 "S101": {"name": "Anuj", "marks": 85},
 "S102": {"name": "Rahul", "marks": 72}
}
#Requirements
#1. Display all student records. 
#2. Search a student using Student ID. 
#3. Add a new student. 
#4. Update marks of an existing student. 
#5. Delete a student. 
#6. Find topper and lowest scorer. 
#7. Calculate class average. 
#8. Count pass and fail students. 
#9. Generate grades: 
#o A (90+) 
#o B (75–89) 
#o C (50–74) 
#o F (<50) 
#10. Display students scoring above average. 
#11. Display top 5 performers. 
#12. Create a separate dictionary for scholarship students (marks > 85). 
#Expected Learning
#• Nested Dictionaries 
#• Dictionary Traversal 
#• Searching 
#• Aggregation 
#• Report Generation
# Initialize a dictionary with 30 mock students for demonstration
# 1. Initialize the dictionary with 30 students (Example data)



students = {}
for i in range(1, 31):
    sid = "S" + str(100 + i) # Creates IDs like S101, S102...
    # Adding sample names and marks (marks vary from 40 to 95)
    students[sid] = {"name": "Student_" + str(i), "marks": 40 + (i * 2) % 60}

# --- Requirement 1: Display all student records ---
print("--- All Student Records ---")
for sid, info in students.items():
    print(f"ID: {sid}, Name: {info['name']}, Marks: {info['marks']}")

# --- Requirement 2: Search a student using Student ID ---
search_id = "S105"
if search_id in students:
    print(f"\nFound: {students[search_id]}")
else:
    print("\nStudent not found.")

# --- Requirement 3: Add a new student ---
students["S131"] = {"name": "Amit", "marks": 88}

# --- Requirement 4: Update marks of an existing student ---
if "S101" in students:
    students["S101"]["marks"] = 92

# --- Requirement 5: Delete a student ---
if "S102" in students:
    del students["S102"]

# --- Requirement 6: Find topper and lowest scorer ---
topper_id = ""
lowest_id = ""
max_marks = -1
min_marks = 101

for sid, info in students.items():
    if info["marks"] > max_marks:
        max_marks = info["marks"]
        topper_id = sid
    if info["marks"] < min_marks:
        min_marks = info["marks"]
        lowest_id = sid

print(f"\nTopper: {students[topper_id]['name']} ({max_marks})")
print(f"Lowest: {students[lowest_id]['name']} ({min_marks})")

# --- Requirement 7: Calculate class average ---
total_marks = 0
for info in students.values():
    total_marks += info["marks"]
average = total_marks / len(students)
print(f"Class Average: {average:.2 f}")

# --- Requirement 8: Count pass and fail students ---
pass_count = 0
fail_count = 0
for info in students.values():
    if info["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1
print(f"Passed: {pass_count}, Failed: {fail_count}")

# --- Requirement 9: Generate grades ---
print("\n--- Student Grades ---")
for sid, info in students.items():
    m = info["marks"]
    if m >= 90: grade = "A"
    elif m >= 75: grade = "B"
    elif m >= 50: grade = "C"
    else: grade = "F"
    print(f"{info['name']}: {grade}")

# --- Requirement 10: Display students scoring above average ---
print("\n--- Students Above Average ---")
for sid, info in students.items():
    if info["marks"] > average:
        print(info["name"])

# --- Requirement 11: Display top 5 performers (No Lambda) ---
# First, convert dictionary to a list to sort
student_list = []
for sid, info in students.items():
    student_list.append([info["marks"], info["name"]])

# Simple Bubble Sort to sort list by marks in descending order
for i in range(len(student_list)):
    for j in range(len(student_list) - 1):
        if student_list[j][0] < student_list[j+1][0]:
            student_list[j], student_list[j+1] = student_list[j+1], student_list[j]

print("\n--- Top 5 Performers ---")
for i in range(5):
    print(f"{i+1}. {student_list[i][1]} - {student_list[i][0]}")

# --- Requirement 12: Scholarship dictionary (marks > 85) ---
scholarship_students = {}
for sid, info in students.items():
    if info["marks"] > 85:
        scholarship_students[sid] = info

print(f"\nScholarship Students Count: {len(scholarship_students)}")