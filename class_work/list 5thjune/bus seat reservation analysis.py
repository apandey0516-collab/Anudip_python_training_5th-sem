seats = [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0]

# 1. Count booked and available seats
booked_count = seats.count(1)
available_count = seats.count(0)

# 2. Find the first available seat (index) and stop immediately
first_available = None
for index, status in enumerate(seats):
    if status == 0:
        first_available = index
        break

# 3. Create a list of all available seat numbers (using index)
available_seats = [i for i, status in enumerate(seats) if status == 0]

# 4. Determine whether the bus is more than 70% occupied
occupancy_rate = (booked_count / len(seats)) * 100
is_over_70 = occupancy_rate > 70

# Display Results
print(f"Booked: {booked_count}, Available: {available_count}")
print(f"First available seat index: {first_available}")
print(f"List of available seat indices: {available_seats}")
print(f"Is more than 70% occupied? {is_over_70} ({occupancy_rate:.2f}%)")