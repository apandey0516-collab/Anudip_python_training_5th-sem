# List of delivery times provided in the problem
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Function to find the shortest delivery time
def fastest_delivery(times):
    # Use the built-in min() function to find the smallest number in the list
    return min(times)

# 2. Function to find orders taking strictly more than 45 minutes
def delayed_orders(times):
    # Use a list comprehension to filter values greater than 45
    return [t for t in times if t > 45]

# 3. Function to calculate the mean delivery time
def average_delivery_time(times):
    # Divide the total sum of times by the number of elements in the list
    return sum(times) / len(times)

# 4. Function to categorize and display each delivery time
def delivery_category(times):
    # Iterate through each time in the list
    for t in times:
        # Check if the time is 30 minutes or less
        if t <= 30:
            print(f"{t} -> Fast")
        # Check if the time is between 31 and 45 minutes
        elif 31 <= t <= 45:
            print(f"{t} -> Normal")
        # For times greater than 45 minutes
        else:
            print(f"{t} -> Delayed")

# --- Executing the functions to match Sample Output ---

print(f"Fastest Delivery: {fastest_delivery(delivery_time)} minutes")

print(f"\nDelayed Orders:\n{delayed_orders(delivery_time)}")

print(f"\nAverage Delivery Time:\n{average_delivery_time(delivery_time)} minutes")

print("\nCategories:")
delivery_category(delivery_time)