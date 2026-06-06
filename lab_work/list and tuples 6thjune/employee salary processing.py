# Initialize the parking slots
slots = [1, 0, 1, 1, 1, 0, 0, 1, 0]

# 1. Count occupied and available slots
occupied_count = slots.count(1)
available_count = slots.count(0)

print(f"Occupied slots: {occupied_count}")
print(f"Available slots: {available_count}")

# 2. Find the first available slot (index)
try:
    first_available = slots.index(0)
    print(f"First available slot index: {first_available}")
except ValueError:
    print("No available slots found.")

# 3. Display all available slot numbers (indices)
available_indices = [i for i, val in enumerate(slots) if val == 0]
print(f"All available slot numbers: {available_indices}")

# 4. Check whether parking occupancy exceeds 75%
occupancy_rate = (occupied_count / len(slots)) * 100
if occupancy_rate > 75:
    print(f"Occupancy is {occupancy_rate:.2f}%: Occupancy exceeds 75%.")
else:
    print(f"Occupancy is {occupancy_rate:.2f}%: Occupancy does not exceed 75%.")