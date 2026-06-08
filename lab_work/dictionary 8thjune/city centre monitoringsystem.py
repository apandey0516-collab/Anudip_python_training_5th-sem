temperature = {
    "Delhi": 41, "Mumbai": 33, "Chennai": 37, "Kolkata": 39, "Bengaluru": 28,
    "Pune": 30, "Jaipur": 42, "Lucknow": 40, "Hyderabad": 35, "Ahmedabad": 43
}

# 1. Cities Above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2. Hottest City
hottest = max(temperature, key=temperature.get)
print(f"\nHottest City: {hottest} ({temperature[hottest]}°C)")

# 3. Coolest City
coolest = min(temperature, key=temperature.get)
print(f"Coolest City: {coolest} ({temperature[coolest]}°C)")

# 4. Average Temperature
avg_temp = sum(temperature.values()) / len(temperature)
print(f"Average Temperature: {avg_temp}°C")

# 5. Pleasant Cities (temp < 35)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]
print(f"Pleasant Cities: {pleasant_cities}")

# 6. Count cities between 35 and 40
count = sum(1 for temp in temperature.values() if 35 <= temp <= 40)
print(f"Cities Between 35°C and 40°C: {count}")