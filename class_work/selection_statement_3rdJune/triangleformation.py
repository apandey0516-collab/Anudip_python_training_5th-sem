#write a program to check whether the three angle formed a tiangle or not 
angle1=int(input("enter the first angle"))
if(angle1 <= 0):
    exit("angle1 cannot be negative")
angle2=int(input("enter the second angle"))
if(angle2 <= 0):
    exit("angle2 cannot be negative")
angle3=int(input("enter the third angle"))
if(angle3<=0):
    exit("angle cannot be negative")

#check whether these three angle form a triangle or not
if((angle1 + angle2 + angle3)==180):
    print("triangle is formed")
else:
    print("triangle is not formed")