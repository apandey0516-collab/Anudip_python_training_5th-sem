#program to check if a student pass the assesment  or not
while(True):#to create an infinite loop for the assessment until the student passes by entering marks greater than or equal to 40
    #accepting the marks
    marks_obtained=int(input("Enter marks ")) #to get the marks obtained by the student as input and convert it to an integer for comparison
    #condition for passing assessment
    if(marks_obtained>=40): #to check if the marks obtained by the student are greater than or equal to 40, which indicates that the student has passed the assessment
        print("Result: Pass") #to display a message indicating that the student has passed the assessment
        print("Congratulations! You have cleared the statement")#to display a congratulatory message for passing the assessment
        break #to exit the loop if the student has passed the assessment
    #condition for failing the assessment
    elif(marks_obtained<=40):#to check if the marks obtained by the student are less than or equal to 40, which indicates that the student has failed the assessment
        print("Result: Fail") #to display a message indicating that the student has failed the assessment
