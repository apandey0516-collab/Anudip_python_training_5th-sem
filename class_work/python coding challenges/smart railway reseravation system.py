# Initialize the seat reservation data using a dictionary
seats = {
    1: "Booked", 2: "Available", 3: "Booked", 4: "Available", 5: "Booked",
    6: "Booked", 7: "Available", 8: "Booked", 9: "Available", 10: "Booked"
}

# Task 1: Display all available seat numbers
print("Available Seats:")
# Iterate through the dictionary and print the key if the status is "Available"
for seat, status in seats.items():
    if status == "Available":
        print(seat, end=" ")
print("\n") # Print a newline for formatting

# Task 2: Count booked and available seats
# Use list comprehension and len() to count occurrences of each status
booked_count = list(seats.values()).count("Booked")
available_count = list(seats.values()).count("Available")
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}\n")

# Task 3: Reserve the first available seat
# Loop through the dictionary to find the first "Available" seat
for seat in seats:
    if seats[seat] == "Available":
        seats[seat] = "Booked" # Update status to Booked
        print(f"Seat {seat} Reserved Successfully.\n")
        break # Exit the loop after reserving the first one

# Task 4: Cancel booking for a given seat number (Example: Seat 1)
def cancel_booking(seat_number):
    if seat_number in seats:
        seats[seat_number] = "Available" # Change status back to Available

# Task 6: Display occupancy percentage
# Formula: (Total Booked / Total Seats) * 100
total_seats = len(seats)
current_booked = list(seats.values()).count("Booked")
occupancy = (current_booked / total_seats) * 100
print(f"Occupancy Percentage: {occupancy:.1f}%")

# Task 5: Store the updated reservation status in reservations.txt
try:
    with open("reservations.txt", "w") as file:
        # Write each seat and its status into the text file
        for seat, status in seats.items():
            file.write(f"Seat {seat}: {status}\n")
    print("\nReservation Details Saved Successfully.")
except Exception as e:
    print(f"Error saving file: {e}")