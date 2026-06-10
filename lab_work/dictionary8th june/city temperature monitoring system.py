# Initialize the dictionary with city names and their temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# --- Task 1: Display cities having temperature above 40°C ---
print("Cities Above 40°C:")
# Loop through the dictionary items (city and temp)
for city, temp in temperature.items():
    # Check if the temperature is greater than 40
    if temp > 40:
        # Print the city name if the condition is met
        print(city)

# --- Task 2: Find the hottest city ---
# Use max() with a key to find the city name with the highest temperature value
hottest_city = max(temperature, key=temperature.get)
# Print the hottest city and its corresponding temperature
print(f"\nHottest City: {hottest_city} ({temperature[hottest_city]}°C)")

# --- Task 3: Find the coolest city ---
# Use min() with a key to find the city name with the lowest temperature value
coolest_city = min(temperature, key=temperature.get)
# Print the coolest city and its corresponding temperature
print(f"Coolest City: {coolest_city} ({temperature[coolest_city]}°C)")

# --- Task 4: Calculate average temperature ---
# Calculate the sum of all temperatures and divide by the number of cities
avg_temp = sum(temperature.values()) / len(temperature)
# Print the result formatted to one decimal place
print(f"Average Temperature: {avg_temp:.1f}°C")

# --- Task 5: Create a list of pleasant cities (temperature < 35°C) ---
# Use list comprehension to collect cities where temperature is below 35
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]
# Print the resulting list of pleasant cities
print(f"\nPleasant Cities: {pleasant_cities}")

# --- Task 6: Count cities with temperature between 35°C and 40°C ---
# Use a generator expression to count cities within the range [35, 40]
count = sum(1 for temp in temperature.values() if 35 <= temp <= 40)
# Print the total count of cities in that range
print(f"Cities Between 35°C and 40°C: {count}")