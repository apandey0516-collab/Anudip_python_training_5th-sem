# 1. & 2. Function to read and display expenses and calculate total
def process_expenses(filename):
    expenses = {} # Dictionary to store category: amount
    total_expenditure = 0 # Variable to track the sum
    
    with open(filename, 'r') as file: # Open file in read mode
        print("--- All Expenses ---")
        for line in file: # Iterate through each line in the file
            category, amount = line.strip().split(',') # Split line by comma
            amount = int(amount) # Convert string amount to integer
            expenses[category] = amount # Store in dictionary
            total_expenditure += amount # Add to running total
            print(f"{category}: ₹{amount}") # Requirement 1: Display all
            
    print(f"\nTotal Expenditure: ₹{total_expenditure}") # Requirement 2: Display total
    return expenses, total_expenditure

# 3. & 4. Function for analysis
def analyze_expenses(expenses):
    # Requirement 3: Find highest and lowest
    highest_cat = max(expenses, key=expenses.get)
    lowest_cat = min(expenses, key=expenses.get)
    
    print(f"Highest Spending: {highest_cat} (₹{expenses[highest_cat]})")
    print(f"Lowest Spending: {lowest_cat} (₹{expenses[lowest_cat]})")
    
    # Requirement 4: Display expenses > 800
    print("\nExpenses greater than ₹800:")
    for cat, amt in expenses.items():
        if amt > 800:
            print(f"- {cat}: ₹{amt}")
            
    return highest_cat, lowest_cat

# 5. Add a new expense
def add_expense(filename, category, amount):
    with open(filename, 'a') as file: # Open in append mode
        file.write(f"\n{category},{amount}") # Add new line to file

# 6. Update an existing expense
def update_expense(filename, target_category, new_amount):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines() # Read all lines into a list
        
    with open(filename, 'w') as file: # Open in write mode to overwrite
        for line in lines:
            category, amount = line.strip().split(',')
            if category == target_category: # If match found
                file.write(f"{category},{new_amount}\n") # Write updated value
            else:
                file.write(line) # Write original value

# 7. Generate Summary Report
def generate_report(total, highest, lowest):
    with open('report.txt', 'w') as file: # Open report file
        file.write("--- Summary Report ---\n")
        file.write(f"Total Expenses: ₹{total}\n")
        file.write(f"Highest Expense Category: {highest}\n")
        file.write(f"Lowest Expense Category: {lowest}\n")

# Main Execution Flow
expenses_dict, total = process_expenses('expenses.txt')
high, low = analyze_expenses(expenses_dict)
generate_report(total, high, low)