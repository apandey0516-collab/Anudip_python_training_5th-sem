# The input attendance string provided in the problem
attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent days using the built-in count method
present_count = attendance.count('P') # Counts every occurrence of 'P'
absent_count = attendance.count('A')  # Counts every occurrence of 'A'

# 2. Calculate attendance percentage
# Formula: (Present Days / Total Days) * 100
total_days = len(attendance)
attendance_percentage = (present_count / total_days) * 100

# 3 & 4. Find the longest consecutive streaks
# We split the string by the opposite character to isolate streaks
# Example: "PPAPP".split('A') -> ['PP', 'PP']
p_streaks = attendance.split('A')
a_streaks = attendance.split('P')

# Calculate the length of the longest string in the resulting lists
longest_p_streak = len(max(p_streaks, key=len))
longest_a_streak = len(max(a_streaks, key=len))

# 5. Determine if attendance is below 75%
status = "Below 75%" if attendance_percentage < 75 else "75% or Above"

# Displaying the output to match the sample format
print(f"Attendance Record: {attendance}")
print(f"Present Days: {present_count}")
print(f"Absent Days: {absent_count}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
print(f"Longest Present Streak: {longest_p_streak}")
print(f"Longest Absent Streak: {longest_a_streak}")
print(f"Attendance Status: {status}")