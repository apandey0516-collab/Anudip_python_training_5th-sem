#creating a modulue for railway reservation seat analyzer
seats = [     "Booked", "Available", "Booked", "Booked",     "Available", "Available", "Booked", "Available",     "Booked", "Booked", "Available", "Booked" ]  
# task 1 function to counts and available seats and create the the following funtions
def count_seat(seats):
    #how many times the word "Booked" appears in the list
    booked_count = seats.count("Booked")
    #how many times the word "Available" appears in the list
    available_count = seats.count("Available")
    #return the both vakue in tuple
    return booked_count, available_count
#task 2 function to find the index of the first available seat
def find_first_available_seat(seats):
    #index. finds the first occurence of "Available"
    #adding 1 converts the o based index to a human radable index seat number
    return seats.index("Available") + 1
# 3. Function to calculate the percentage of seats that are occupied
def occupancy_percentage(seats):
    # Get the number of booked seats
    booked = seats.count("Booked")
    # Calculate percentage: (booked / total seats) * 100
    return (booked / len(seats)) * 100

# 4. Function to display all seat numbers that are available
def display_available_seats(seats):
    # Use a list comprehension to find indices where seat is "Available"
    # i + 1 converts the index to a seat number
    available_indices = [i + 1 for i, status in enumerate(seats) if status == "Available"]
    # Join the numbers into a single string separated by spaces and print
    print(" ".join(map(str, available_indices)))

# --- Execution and Output ---

# Call count_seats and unpack the results into two variables
booked_count, available_count = count_seat(seats)
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}\n")

# Call first_available and print the result
print(f"First Available Seat: {find_first_available_seat(seats)}\n")

# Call occupancy_percentage and format it to 2 decimal places
print(f"Occupancy Percentage: {occupancy_percentage(seats):.2f}%\n")

# Call display_available_seats
print("Available Seat Numbers:")
display_available_seats(seats) 


    
