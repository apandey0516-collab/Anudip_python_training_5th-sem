#program to display student result management
#program for student result management system
# Take marks of 5 subjects from the user
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
# Total marks = 500 because 5 subjects and each subject is out of 100
percentage = total / 5

# Variable to count failed subjects
failed_subjects = 0

# If marks are less than 40, that subject is failed
if sub1 < 40:
    failed_subjects = failed_subjects + 1

if sub2 < 40:
    failed_subjects = failed_subjects + 1

if sub3 < 40:
    failed_subjects = failed_subjects + 1

if sub4 < 40:
    failed_subjects = failed_subjects + 1

if sub5 < 40:
    failed_subjects = failed_subjects + 1

# Decide grade according to percentage
if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display result
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)