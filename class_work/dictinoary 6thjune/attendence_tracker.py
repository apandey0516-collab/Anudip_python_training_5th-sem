# Initialize an empty dictionary to store attendance
attendance_tracker = {}

# Loop 30 times to collect data for 30 students
for i in range(30):
    # Ask user for the student's roll number
    roll_no = input(f"Enter roll number for student {i+1}: ")
    
    # Ask user to input 'Present' or 'Absent'
    status = input(f"Enter status (Present/Absent) for {roll_no}: ")
    
    # Store data in dictionary: key is roll_no, value is status
    attendance_tracker[roll_no] = status

print("\n--- Students Present ---")

# Iterate through the dictionary items
for roll, status in attendance_tracker.items():
    # Check if the status value is 'Present'
    if status.lower() == "present":
        # Display the roll number of the present student
        print(f"Roll Number: {roll}")