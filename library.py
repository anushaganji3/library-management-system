import json
import os

FILE = "library.json"

# Load data
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add book
def add_book(data):
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")

    if book_id in data:
        print("Book already exists!")
    else:
        data[book_id] = {"name": name, "issued": False}
        print("Book added successfully!")

# View books
def view_books(data):
    if not data:
        print("No books available.")
        return

    for bid, info in data.items():
        status = "Issued" if info["issued"] else "Available"
        print(f"{bid} - {info['name']} ({status})")

# Issue book
def issue_book(data):
    book_id = input("Enter Book ID to issue: ")

    if book_id in data and not data[book_id]["issued"]:
        data[book_id]["issued"] = True
        print("Book issued successfully!")
    else:
        print("Book not available!")

# Return book
def return_book(data):
    book_id = input("Enter Book ID to return: ")

    if book_id in data and data[book_id]["issued"]:
        data[book_id]["issued"] = False
        print("Book returned successfully!")
    else:
        print("Invalid book ID or not issued!")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book(data)
        elif choice == "2":
            view_books(data)
        elif choice == "3":
            issue_book(data)
        elif choice == "4":
            return_book(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")

        save_data(data)

if __name__ == "__main__":
    main()