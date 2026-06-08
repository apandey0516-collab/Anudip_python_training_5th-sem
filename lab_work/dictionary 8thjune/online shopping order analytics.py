# Create a dictionary containing product names and their sales numbers
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# --- Task 1: Display products sold more than 20 times ---
print("Products Sold More Than 20 Times:")
# Look at every product (key) and its sales (value) in the dictionary
for product, count in sales.items():
    # If the sales count is greater than 20, print the product name
    if count > 20:
        print(product)

# --- Task 2: Find the best-selling product ---
# Find the product name that has the maximum value in the sales dictionary
best_selling = max(sales, key=sales.get)
print(f"\nBest Selling Product: {best_selling} ({sales[best_selling]})")

# --- Task 3: Find the least-selling product ---
# Find the product name that has the minimum value in the sales dictionary
least_selling = min(sales, key=sales.get)
print(f"Least Selling Product: {least_selling} ({sales[least_selling]})")

# --- Task 4: Calculate total products sold ---
# Add up all the numbers (values) inside the dictionary
total_units = sum(sales.values())
print(f"\nTotal Units Sold: {total_units}")

# --- Task 5: Create a list of products requiring promotion (sales < 15) ---
# Make a new list of product names only if their sales are less than 15
promo_list = [product for product, count in sales.items() if count < 15]
print(f"\nProducts Requiring Promotion:\n{promo_list}")

# --- Task 6: Count products having sales between 10 and 30 ---
# Create a list of products where sales are between 10 and 30, then count how many are in that list
count_10_30 = len([product for count in sales.values() if 10 <= count <= 30])
print(f"\nProducts Having Sales Between 10 and 30: {count_10_30}")