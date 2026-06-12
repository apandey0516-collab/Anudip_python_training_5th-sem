import os

# File name constant
FILENAME = "contacts.txt"

def load_contacts():
    """Reads the file and returns a dictionary of {name: number}."""
    contacts = {}
    # Check if the file exists before trying to open it
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                # Strip whitespace and split by comma
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, number = parts
                    contacts[name] = number
    return contacts

def save_contacts(contacts):
    """Writes the current dictionary back to the text file."""
    with open(FILENAME, "w") as file:
        for name, number in contacts.items():
            # Format as 'Name,Number' followed by a newline
            file.write(f"{name},{number}\n")
    print("Changes saved to file.")

def main():
    # Initial load of data from file
    contacts = load_contacts()

    while True:
        # Display the menu options
        print("\n--- Mobile Contact Directory ---")
        print("1. Display all contacts")
        print("2. Search a contact by name")
        print("3. Add a new contact")
        print("4. Update an existing contact number")
        print("5. Delete a contact")
        print("6. Display contacts starting with a vowel")
        print("7. Save and Exit")
        
        choice = input("Enter choice (1-7): ")

        if choice == '1':
            # Option 1: Display all
            if not contacts:
                print("Directory is empty.")
            for name, num in contacts.items():
                print(f"{name}: {num}")

        elif choice == '2':
            # Option 2: Search
            name = input("Enter name to search: ")
            print(f"Number: {contacts.get(name, 'Not found')}")

        elif choice == '3':
            # Option 3: Add new
            name = input("Enter name: ")
            number = input("Enter number: ")
            contacts[name] = number
            print("Contact added.")

        elif choice == '4':
            # Option 4: Update
            name = input("Enter name to update: ")
            if name in contacts:
                contacts[name] = input("Enter new number: ")
                print("Updated successfully.")
            else:
                print("Contact not found.")

        elif choice == '5':
            # Option 5: Delete
            name = input("Enter name to delete: ")
            if contacts.pop(name, None):
                print("Deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == '6':
            # Option 6: Filter by vowels
            vowels = "AEIOUaeiou"
            found = False
            for name in contacts:
                if name[0] in vowels:
                    print(f"{name}: {contacts[name]}")
                    found = True
            if not found:
                print("No contacts found starting with a vowel.")

        elif choice == '7':
            # Option 7: Save and Exit
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()