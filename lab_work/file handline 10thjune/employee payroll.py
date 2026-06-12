import os

# Function to read employees from the file and return a list of lists
def read_employees():
    employees = [] # Initialize an empty list to store employee data
    if not os.path.exists("employees.txt"): # Check if the file exists
        return employees # Return empty list if file doesn't exist
    with open("employees.txt", "r") as file: # Open file in read mode
        for line in file: # Iterate through each line in the file
            employees.append(line.strip().split(",")) # Strip newline, split by comma, and add to list
    return employees # Return the list of employee records

# Function to save a new employee record to the file
def add_employee():
    emp_id = input("Enter Employee ID: ") # Get ID from user
    name = input("Enter Name: ") # Get Name from user
    salary = input("Enter Salary: ") # Get Salary from user
    with open("employees.txt", "a") as file: # Open file in append mode
        file.write(f"{emp_id},{name},{salary}\n") # Write formatted string to file
    print("Record added successfully!") # Confirm success to user

# Main menu-driven loop
while True:
    print("\n--- Employee Payroll Management System ---") # Menu header
    print("1. Display all records\n2. Search by ID\n3. Calculate Average Salary") # Options 1-3
    print("4. High/Low Paid\n5. Salary > 50,000\n6. Add Record\n7. Salary Categories\n8. Exit") # Options 4-8
    
    choice = input("Enter choice: ") # Get user's menu selection
    data = read_employees() # Load current data from file

    if choice == '1': # Requirement 1: Display all
        for emp in data: # Loop through records
            print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: ₹{emp[2]}") # Print formatted details
            
    elif choice == '2': # Requirement 2: Search by ID
        search_id = input("Enter ID to search: ") # Get search target
        found = [e for e in data if e[0] == search_id] # Filter list for matching ID
        print(found[0] if found else "Not Found") # Print result or error message
        
    elif choice == '3': # Requirement 3: Average Salary
        salaries = [int(e[2]) for e in data] # Extract salaries as integers
        print(f"Average Salary: ₹{sum(salaries)/len(salaries):.2/f}" if salaries else "No data") # Calc and print mean
        
    elif choice == '4': # Requirement 4: High/Low Paid
        if data: # Check if data exists
            high = max(data, key=lambda x: int(x[2])) # Find record with max salary
            low = min(data, key=lambda x: int(x[2])) # Find record with min salary
            print(f"Highest: {high[1]} (₹{high[2]})\nLowest: {low[1]} (₹{low[2]})") # Print results
            
    elif choice == '5': # Requirement 5: Salary > 50,000
        for e in data: # Iterate through employees
            if int(e[2]) > 50000: # Check if salary exceeds 50k
                print(f"{e[1]}: ₹{e[2]}") # Print name and salary
                
    elif choice == '6': # Requirement 6: Add record
        add_employee() # Call the add_employee function defined above
        
    elif choice == '7': # Requirement 7: Salary Categories
        for e in data: # Iterate through records
            sal = int(e[2]) # Convert salary string to integer
            cat = "High" if sal >= 60000 else "Medium" if sal >= 40000 else "Low" # Determine category
            print(f"{e[1]} ({e[2]}): {cat}") # Print name, salary, and category
            
    elif choice == '8': # Exit option
        break # Break the while loop to end program