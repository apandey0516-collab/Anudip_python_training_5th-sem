attendance = {}

for i in range(5):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")
    
    attendance[roll_no] = status

print("\nPresent Students:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print("present student:",roll_no)