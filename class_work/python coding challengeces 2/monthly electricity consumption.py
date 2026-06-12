#Problem Statement
#Monthly electricity consumption (units) of different houses in a residential society is stored as follows:
#Sample Data
#units = {
 #"House101": 320,
 #"House102": 180,
 #"House103": 510,
 #"House104": 275,
 #"House105": 150,
 #"House106": 430,
 #"House107": 220,
 #"House108": 390,
 #"House109": 145,
 #"House110": 600
#}
#Tasks
#1. Display houses consuming more than 400 units. 
#2. Find the highest-consuming house. 
#3. Find the lowest-consuming house. 
#4. Calculate the total units consumed. 
#5. Create separate lists for: 
#o Low Consumption (< 200) 
#o Medium Consumption (200–400) 
#o High Consumption (> 400) 
#6. Count houses eligible for an energy-saving campaign (consumption > 300)

# Initialize the dictionary with house IDs as keys and units as values
units = {
    "House101": 320, "House102": 180, "House103": 510, "House104": 275, "House105": 150,
    "House106": 430, "House107": 220, "House108": 390, "House109": 145, "House110": 600
}

# Task 1: Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, val in units.items():
    if val > 400:
        print(house)

# Task 2: Find the highest-consuming house using the max function on dictionary values
highest_house = max(units, key=units.get)
print(f"\nHighest Consumption: {highest_house} ({units[highest_house]} units)")

# Task 3: Find the lowest-consuming house using the min function on dictionary values
lowest_house = min(units, key=units.get)
print(f"Lowest Consumption: {lowest_house} ({units[lowest_house]} units)")

# Task 4: Calculate the sum of all values in the dictionary
total_units = sum(units.values())
print(f"\nTotal Units Consumed: {total_units}")

# Task 5:categorice the houses based on their consumption
low, medium, high = [], [], []
for house, val in units.items():
    if val < 200:
        low.append(house)
    elif 200 <= val <= 400:
        medium.append(house)
    else:
        high.append(house)

print(f"\nLow Consumption: {low}")
print(f"Medium Consumption: {medium}")
print(f"High Consumption: {high}")

# Task 6: Count houses where consumption is strictly greater than 300
campaign_count = sum(1 for val in units.values() if val > 300)
print(f"\nEligible for Energy-Saving Campaign: {campaign_count}")