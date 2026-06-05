stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Display products that are out of stock (quantity is 0)
out_of_stock = [i for i, qty in enumerate(stock) if qty == 0]
print(f"Indices of out of stock products: {out_of_stock}")

# 2. Display products that need restocking (quantity less than 10)
restock_needed = [i for i, qty in enumerate(stock) if qty < 10]
print(f"Indices of products needing restock: {restock_needed}")

# 3. Count available products (quantity greater than 0)
available_count = len([qty for qty in stock if qty > 0])
print(f"Total available products: {available_count}")

# 4. Create a new list containing only products with stock greater than 10
high_stock_products = [qty for qty in stock if qty > 10]
print(f"Products with stock > 10: {high_stock_products}")