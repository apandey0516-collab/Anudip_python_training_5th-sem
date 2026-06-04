# program to convert time in to corresponding hours, minutes and seconds
#input of time in seconds
second= int(input("enter time in seconds:"))
#check second in negative 
if(second < 0):
    exit ("time cannot be negative......exited")
#---------------------------------------------------
print("--------------------------")
hours = 0 
minute = 0
# converting number of second into hours
if(second >= 3600):
    hours = second // 3600
    second = second % 3600
#---------------------------------------------------
# converting into minutes 
if(second >= 60):
    minute = second // 60
    second = second % 60
#----------------------------------------------------
print("time in hours: ",hours,"hr")
print("time in minutes: ",minute,"min")
print("time in seconds: ",second,"sec")
print("--------------------------")
