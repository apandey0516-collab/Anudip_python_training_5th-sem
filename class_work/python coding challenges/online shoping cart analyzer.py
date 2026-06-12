# Initialize the list with given product prices
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Calculate the total sum of all items in the cart
total_value = sum(cart)

# 2. Identify the highest and lowest price values in the list
most_expensive = max(cart)
cheapest = min(cart)

# 3. Use a list comprehension to find items > 1000 and get the count
premium_eligible_count = len([price for price in cart if price > 1000])

# 4. Create a new list containing only products with a price above 1500
discount_list = [price for price in cart if price > 1500]

# 5. Divide the total value by the number of items to find the average
average_price = total_value / len(cart)

# Display the results formatted to match the sample output
print(f"Total Cart Value: ₹{total_value:,}")
print(f"Most Expensive Product: ₹{most_expensive:,}")
print(f"Cheapest Product: ₹{cheapest:,}")
print(f"Premium Shipping Eligible Products: {premium_eligible_count}")
print(f"Discount Eligible Products: {discount_list}")
print(f"Average Product Price: ₹{average_price:,}")