# program to display student attendence tracker
Total_students = 30 #to initialize the total number of students in class
Attendence_count = 1 #to initialize the attendance count
Presrent_student =0 #to initialize the count of present students
Absent_student=0 #to initialize the count of absent students
while(Attendence_count<=Total_students): #to check if the attendance count is less than or equal to the total number of students
    print("Student :",Attendence_count)#to display the current student number for which attendance is being taken
#input 
    status = input("Attendence :")#to get the attendance status (present or absent) from the user for each student
#input Checker
    if status == "present": #to check if the attendance status is "present"
        Presrent_student+=1#to increment the count of present students by 1 if the status is "present"
    elif status == "absent":#to check if the attendance status is "absent"
        Absent_student+=1 #to increment the count of absent students by 1 if the status is "absent"
    else: #to handle invalid input for attendance status
        print("Invalid input") #to display a message indicating that the input is invalid and to prompt the user to enter a valid attendance status
        Attendence_count-=1 #to decrement the attendance count by 1 to allow the user to re-enter the attendance status for the same student in case of invalid input
        #Attendence Counter
    Attendence_count+=1 #to increment the attendance count by 1 to move on to the next student after processing the attendance status for the current student
print("Present Student Count:",Presrent_student)#to display the total count of present students after processing the attendance for all students
print("Absent Student Count:",Absent_student)#to display the total count of absent students after processing the attendance for all students