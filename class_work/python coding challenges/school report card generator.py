# Open the source file 'marks.txt' in read mode
with open('marks.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Initialize variables to store results
students = [] # List to store student data as dictionaries
passed_count = 0
failed_count = 0
merit_holders = []
topper = {"name": "", "marks": -1}

# Process each line from the file
for line in lines:
    # Remove whitespace and split the string by comma
    sid, name, marks = line.strip().split(',')
    marks = int(marks) # Convert marks from string to integer
    
    # Store student data in a dictionary for easy access
    student_data = {"id": sid, "name": name, "marks": marks}
    students.append(student_data)
    
    # Task 1 & 4: Logic for Passing (assuming 40 is the passing mark)
    if marks >= 40:
        passed_count += 1
    else:
        failed_count += 1
        
    # Task 3: Check if this student is the topper
    if marks > topper["marks"]:
        topper = {"name": name, "marks": marks}
        
    # Task 5: Check for Merit Certificate eligibility (marks >= 90)
    if marks >= 90:
        merit_holders.append(name)

# Task 2: Generate 'report_card.txt'
with open('report_card.txt', 'w') as report:
    for s in students:
        # Determine grade/status for the report file
        status = "Pass" if s["marks"] >= 40 else "Fail"
        # Write formatted string to the file
        report.write(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}, Status: {status}\n")

# Displaying the final Output (as per sample)
print(f"Topper:\n{topper['name']} ({topper['marks']})\n")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}\n")
print("Merit Certificate Holders:")
for name in merit_holders:
    print(name)

print("\nReport Cards Generated Successfully.")