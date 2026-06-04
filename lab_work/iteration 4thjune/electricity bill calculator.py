#program to display electricity bill calculator
units = int(input("enter the number of units consumed:"))#to get the number of units consumed from the user
if units <= 100:#t o calculate the bill based on the number of units consumed using a tiered pricing structure
 bill = units * 5
 print("low consumption")
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
print("Electricity bill for", units, "units is:", bill, "currency units")   

