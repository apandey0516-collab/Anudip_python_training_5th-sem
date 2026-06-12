import os

# Define the filename
FILENAME = "books.txt"

def load_books():
    """Reads books from the file and returns a list of dictionaries."""
    books = []
    # Open the file in read mode ('r')
    if not os.path.exists(FILENAME):
        return books
    
    with open(FILENAME, 'r') as file:
        # Read each line from the file one by one
        for line in file:
            # Strip whitespace and split the line by commas into a list
            parts = line.strip().split(',')
            if len(parts) == 3:
                # Store data in a dictionary for easy access
                books.append({
                    "id": parts[0],
                    "title": parts[1],
                    "quantity": int(parts[2])
                })
    return books

def save_books(books):
    """Writes the current book list back to the text file."""
    # Open the file in write mode ('w') which overwrites the existing content
    with open(FILENAME, 'w') as file:
        for b in books:
            # Format the data back into a comma-separated string
            line = f"{b['id']},{b['title']},{b['quantity']}\n"
            # Write the formatted string to the file
            file.write(line)

def display_books(book_list):
    print(f"{'ID':<6} | {'Title':<20} | {'Qty'}")
    print("-" * 35)
    for b in book_list:
        print(f"{b['id']:<6} | {b['title']:<20} | {b['quantity']}")

def search_book(books, book_id):
    for b in books:
        if b['id'] == book_id:
            return b
    return None

def update_quantity(book_id, amount):
    books = load_books() # Read latest data
    book = search_book(books, book_id)
    if book:
        if book['quantity'] + amount < 0:
            print("Error: Book is currently unavailable.")
        else:
            book['quantity'] += amount
            save_books(books) # Update the file immediately
            print(f"Success! Updated quantity for {book['title']}.")
    else:
        print("Book ID not found.")

# --- Requirements Implementation ---

def main():
    while True:
        books = load_books()
        print("\n1. Display All | 2. Search | 3. Issue | 4. Return | 5. Unavailable | 6. Restock | 7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            bid = input("Enter Book ID: ")
            res = search_book(books, bid)
            display_books([res]) if res else print("Not found.")
        elif choice == '3':
            update_quantity(input("Enter ID to issue: "), -1)
        elif choice == '4':
            update_quantity(input("Enter ID to return: "), 1)
        elif choice == '5':
            display_books([b for b in books if b['quantity'] == 0])
        elif choice == '6':
            display_books([b for b in books if b['quantity'] < 2])
        elif choice == '7':
            break

if __name__ == "__main__":
    main()