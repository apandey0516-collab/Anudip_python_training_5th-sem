units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, val in units.items():
    if val > 400:
        print(house)

# 2 & 3. Highest and Lowest consuming houses
highest_house = max(units, key=units.get)
lowest_house = min(units, key=units.get)

print(f"\nHighest Consumption:\n{highest_house} ({units[highest_house]} units)")
print(f"\nLowest Consumption:\n{lowest_house} ({units[lowest_house]} units)")

# 4. Total units consumed
total_units = sum(units.values())
print(f"\nTotal Units Consumed: {total_units}")

# 5. Create lists for consumption levels
low = [h for h, v in units.items() if v < 200]
medium = [h for h, v in units.items() if 200 <= v <= 400]
high = [h for h, v in units.items() if v > 400]

print(f"\nLow Consumption:\n{low}")
print(f"\nMedium Consumption:\n{medium}")
print(f"\nHigh Consumption:\n{high}")

# 6. Count houses eligible for energy-saving campaign (> 300)
eligible_count = len([h for h, v in units.items() if v > 300])
print(f"\nEligible for Energy-Saving Campaign: {eligible_count}")