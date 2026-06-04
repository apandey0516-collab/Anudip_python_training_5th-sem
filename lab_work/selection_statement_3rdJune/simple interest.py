#program to display simple interest
pa=int(input("enter the principal amount")) 
if (pa<=0):
    exit("principal amount cantnot be negative")
r=float(input("enter the rate in percentage"))
if(r<=0):
    exit("rate cannot be negative")
t=int(input("enter the time in years"))
if(t<=0):
    exit("time cannot be negative")
else:
    print("Simple interest is: ",(pa*t*r)/100)

