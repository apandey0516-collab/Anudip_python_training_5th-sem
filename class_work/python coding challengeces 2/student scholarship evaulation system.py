#Initialize the dictionary with house IDs as keys and units as values
marks = {
 "Anuj": 92,
 "Rahul": 76,
 "Priya": 88,
 "Neha": 64,
 "Amit": 58,
 "Sneha": 95,
 "Karan": 81,
 "Pooja": 73,
 "Rohit": 47,
 "Anjali": 90
}
#Display students scoring above 85 marks
print("Students scoring above 85 marks:")
for name, marks in marks.items():
    if marks > 85:
        print(name)
#find the topper
topper = max(marks, key=marks.get)
print(f"The topper is: {topper}")

#find the lowest marks
lowest = min(marks, key=marks.get)
print(f"The lowest scorer is: {lowest}")

#calculate the average marks
total_marks = sum(marks.values())
average = total_marks / len(marks)
print(f"The average marks is: {average}")

#categories of ,arks in grades
highest, lowest, average = [], [], []
for name, marks in marks.items():
    if marks >= 90:
        highest.append(name)
    elif marks >= 50:
        average.append(name)
    else:
        lowest.append(name)
print(f"Students scoring above 90 marks: {highest}")
print(f"Students scoring between 50 and 90 marks: {average}")
print(f"Students scoring below 50 marks: {lowest}")