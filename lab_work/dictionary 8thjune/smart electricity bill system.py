# Initialize the dictionary containing house IDs as keys and units as values
units = {
    "House101": 320, "House102": 180, "House103": 510, "House104": 275, "House105": 150,
    "House106": 430, "House107": 220, "House108": 390, "House109": 145, "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, val in units.items():
    if val > 400:
        print(house)

# 2. & 3. Find highest and lowest consuming houses using the max/min functions on dictionary keys based on values
highest_house = max(units, key=units.get)
lowest_house = min(units, key=units.get)

print(f"\nHighest Consumption:\n{highest_house} ({units[highest_house]} units)")
print(f"\nLowest Consumption:\n{lowest_house} ({units[lowest_house]} units)")

# 4. Calculate total units consumed using the sum() function on dictionary values
total_units = sum(units.values())
print(f"\nTotal Units Consumed: {total_units}")

# 5. Create lists for different consumption categories using list comprehension
low_cons = [h for h, v in units.items() if v < 200]           # Units < 200
med_cons = [h for h, v in units.items() if 200 <= v <= 400]  # Units between 200 and 400
high_cons = [h for h, v in units.items() if v > 400]         # Units > 400

print(f"\nLow Consumption: {low_cons}")
print(f"Medium Consumption: {med_cons}")
print(f"High Consumption: {high_cons}")

# 6. Count houses eligible for energy-saving campaign (consumption > 300)
eligible_count = len([h for h, v in units.items() if v > 300])
print(f"\nEligible for Energy-Saving Campaign: {eligible_count}")