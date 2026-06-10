# Initialize the sales dictionary with product names as keys and units sold as values
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

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
# Iterate through the dictionary items (key-value pairs)
for product, count in sales.items():
    # Check if the sales count is strictly greater than 20
    if count > 20:
        print(product)

# 2. Find the best-selling product
# Use max() on dictionary keys, using the dictionary values (sales.get) as the comparison criteria
best_seller = max(sales, key=sales.get)
print(f"\nBest Selling Product: {best_seller} ({sales[best_seller]})")

# 3. Find the least-selling product
# Use min() on dictionary keys, using the dictionary values (sales.get) as the comparison criteria
least_seller = min(sales, key=sales.get)
print(f"Least Selling Product: {least_seller} ({sales[least_seller]})")

# 4. Calculate total products sold
# Use the sum() function on all the values in the dictionary
total_units = sum(sales.values())
print(f"\nTotal Units Sold: {total_units}")

# 5. Create a list of products requiring promotion (sales < 15)
# Use list comprehension to collect product names where the value is less than 15
promo_list = [product for product, count in sales.items() if count < 15]
print(f"\nProducts Requiring Promotion:\n{promo_list}")

# 6. Count products having sales between 10 and 30
# Filter the counts that are >= 10 and <= 30, then find the length of that list
mid_range_count = len([count for count in sales.values() if 10 <= count <= 30])
print(f"\nProducts Having Sales Between 10 and 30: {mid_range_count}")