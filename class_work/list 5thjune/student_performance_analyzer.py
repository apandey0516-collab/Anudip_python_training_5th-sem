#crate a list to store some number
marks =[76, 45, 92, 35, 88, 40, 99, 56]
# to display all the passed student
passed_students = []
for m in marks:
    if m >= 40:
        passed_students.append(m)
print("passed_students:",passed_students)

# count the number of failed student 
failed_count= 0
for m in marks:
    if m<40:
        failed_count += 1
print("number of failed students:",failed_count)
#find highest and lowest marks without using max()or min()
highest = marks[0]
lowest = marks[0]
for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

print("Highest marks:", highest)
print("Lowest marks:", lowest)

# 4. Create a new list containing marks above 75
above_75 = [m for m in marks if m > 75]
print("Marks above 75:", above_75)


