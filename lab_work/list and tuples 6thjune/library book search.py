attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# 1. Count present and absent days
present_days = attendance.count('P')
absent_days = attendance.count('A')
total_days = len(attendance)

# 2. Calculate attendance percentage
percentage = (present_days / total_days) * 100

# 3. Determine eligibility (minimum 75%)
eligible = percentage >= 75

# 4. Display positions where the student was absent (1-based indexing)
absent_positions = [i + 1 for i, status in enumerate(attendance) if status == 'A']

# Displaying Results
print(f"Present Days: {present_days}")
print(f"Absent Days: {absent_days}")
print(f"Attendance Percentage: {percentage:.2f}%")
print(f"Eligible for exams: {'Yes' if eligible else 'No'}")
print(f"Absent on days: {absent_positions}")