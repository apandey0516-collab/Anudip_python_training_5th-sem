#program to display to mini employee payroll 
# Mini Employee Payroll System
employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculations
#hra calculation
hra = basic_salary * 0.20
#da calculation
da = basic_salary * 0.10
#pf calculation
pf = basic_salary * 0.12

#gross salary calculation
gross_salary = basic_salary + hra + da
#net salary calculation
net_salary = gross_salary - pf

# Grade Determination
#senior grade
if net_salary > 50000:
    grade = "Senior Grade"
#mid grade
elif net_salary > 30000:
    grade = "Mid Grade"
#junior grade
else:
    grade = "Junior Grade"

#printing all details
print("\n--- Employee Payroll Details ---")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("PF Deduction:", pf)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary) 
print("Grade:", grade) 