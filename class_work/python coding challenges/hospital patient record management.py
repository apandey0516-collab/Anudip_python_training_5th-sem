# Function to manage hospital records
def manage_hospital_records():
    # Open the input file in read mode
    with open('patients.txt', 'r') as file:
        # Read all lines from the file and store them in a list
        records = file.readlines()

    # Task 1: Display all patient records
    print("--- All Patient Records ---")
    for record in records:
        # Strip newline characters and print each line
        print(record.strip())

    # Task 2 & 5: Filter Critical Patients and Save to file
    print("\nCritical Patients:")
    # Open (or create) the output file in write mode
    with open('critical_patients.txt', 'w') as crit_file:
        for record in records:
            # Split the comma-separated line into a list [ID, Name, Status]
            data = record.strip().split(',')
            # Check if the third element (Status) is 'Critical'
            if data[2] == 'Critical':
                # Print the name to the console (Task 2)
                print(data[1])
                # Write the full record to the new file (Task 5)
                crit_file.write(record)
    print("Critical Patient Report Generated Successfully.")

    # Task 3: Count patients under each status
    # Initialize a dictionary to store counts for each category
    counts = {'Normal': 0, 'Stable': 0, 'Critical': 0}
    for record in records:
        data = record.strip().split(',')
        status = data[2]
        # Increment the count for the specific status found
        if status in counts:
            counts[status] += 1
    
    print("\nPatient Count:")
    # Loop through dictionary items to display results
    for status, count in counts.items():
        print(f"{status} : {count}")

    # Task 4: Search patient details using Patient ID
    search_id = "P104" # Example ID from sample output
    print("\nPatient Found:")
    found = False
    for record in records:
        # Check if the record starts with the target ID
        if record.startswith(search_id):
            print(record.strip())
            found = True
            break # Exit loop once found
    if not found:
        print("Patient ID not found.")

# Run the function
if __name__ == "__main__":
    manage_hospital_records()