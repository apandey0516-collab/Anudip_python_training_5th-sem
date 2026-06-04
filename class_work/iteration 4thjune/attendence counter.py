#program to display student attendance
student_in_class=0#to initialize the count of students in class
while(student_in_class<30):#to check if the count of students in class is less than 30
    print("Student Entered")#to display a message indicating that a student has entered the class
    student_in_class+=1#to increment the count of students in class by 1 each time a student enters
    print("Attendace Count :", student_in_class)#to display the current attendance count after each student enters
print("All students entered")#to display a message indicating that all students have entered the class