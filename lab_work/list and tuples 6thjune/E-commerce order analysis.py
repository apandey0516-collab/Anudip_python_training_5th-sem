orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display all products costing more than ₹1000
print("Products costing more than ₹1000:")
for item, price in orders:
    if price > 1000:
        print(f"- {item}: ₹{price}")

# 2. Find the most expensive product
most_expensive = max(orders, key=lambda x: x[1])
print(f"\nMost expensive product: {most_expensive[0]} (₹{most_expensive[1]})")

# 3. Calculate the total order value
total_value = sum(price for item, price in orders)
print(f"Total order value: ₹{total_value}")

# 4. Count products costing below ₹1000
count_below_1000 = sum(1 for item, price in orders if price < 1000)
print(f"Count of products costing below ₹1000: {count_below_1000}")