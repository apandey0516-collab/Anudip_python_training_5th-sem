# Initialize the list with the given parking status data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# Task 1: Display vacant parking slot numbers
print("Vacant Parking Slots:")
# Use a loop with enumerate starting at 1 to get slot numbers
for index, status in enumerate(parking_slots, start=1):
    if status == "Vacant":
        # Print the slot number followed by a space
        print(index, end=" ")
print("\n") # Print a newline for better formatting

# Task 2: Count occupied and vacant slots
occupied_count = parking_slots.count("Occupied") # Count occurrences of "Occupied"
vacant_count = parking_slots.count("Vacant")     # Count occurrences of "Vacant"
print(f"Occupied Slots: {occupied_count}")
print(f"Vacant Slots: {vacant_count}\n")

# Task 3: Allocate the first vacant slot to a new vehicle
# Find the index of the first "Vacant" slot
first_vacant_index = parking_slots.index("Vacant")
# Update the status at that index to "Occupied"
parking_slots[first_vacant_index] = "Occupied"
# Print the slot number (index + 1) where the vehicle was parked
print(f"Vehicle Allocated to Slot {first_vacant_index + 1}\n")

# Task 4: Calculate parking occupancy percentage
# Recalculate the number of occupied slots after the new allocation
current_occupied = parking_slots.count("Occupied")
# Calculate percentage: (Occupied / Total) * 100
occupancy_percentage = (current_occupied / len(parking_slots)) * 100
print(f"Occupancy Percentage: {occupancy_percentage}%\n")

# Task 5: Store updated parking information in parking.txt
try:
    # Open the file in write mode ('w')
    with open("parking.txt", "w") as file:
        # Write each status from the list into the file
        for status in parking_slots:
            file.write(status + "\n")
    print("Parking Details Saved Successfully.")
except Exception as e:
    # Handle potential errors during file writing
    print(f"An error occurred: {e}")