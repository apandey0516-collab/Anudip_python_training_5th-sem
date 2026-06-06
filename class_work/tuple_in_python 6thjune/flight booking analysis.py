#craeting flight booking
bookings = (
("P101", "Delhi", "Confirmed"),
("P102", "Mumbai", "Waiting"),
("P103", "Delhi", "Confirmed"),
("P104", "Chennai", "Cancelled"),
("P105", "Mumbai", "Confirmed"),
("P106", "Delhi", "Waiting")
)
# 1. Display all passengers whose booking status is Confirmed
print("Confirmed Passengers:")
for pid, dest, status in bookings:
    if status == "Confirmed":
        print(f"{pid} {dest}")

# 2. Count the number of passengers travelling to Delhi
delhi_count = sum(1 for _, dest, _ in bookings if dest == "Delhi")
print(f"\nPassengers Travelling to Delhi: {delhi_count}")

# 3. Count Confirmed, Waiting, and Cancelled bookings separately
counts = {"Confirmed": 0, "Waiting": 0, "Cancelled": 0}
for _, _, status in bookings:
    counts[status] += 1

print(f"\nConfirmed: {counts['Confirmed']}")
print(f"Waiting: {counts['Waiting']}")
print(f"Cancelled: {counts['Cancelled']}")

# 4. Create a list containing passenger IDs with Waiting status
waiting_list = [pid for pid, _, status in bookings if status == "Waiting"]
print(f"\nWaiting List:\n{waiting_list}")

# 5. Determine which destination has the highest number of bookings
dest_counts = {}
for _, dest, _ in bookings:
    dest_counts[dest] = dest_counts.get(dest, 0) + 1

most_booked = max(dest_counts, key=dest_counts.get)
print(f"\nMost Booked Destination:\n{most_booked}")