import json



def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []



def return_book():

    lend_books = load_data("all_lend_books.json")
    all_books = load_data("all_books.json")


    if not lend_books:
        print("No books have been lent out.")
        return


    search = input("Enter Book Title: ").lower()

    for lend in lend_books:
        if search in lend['book_name'].lower():
            print("\nBook Found!")
            print(f"Borrower Name: {lend['Borrow_name']}")
            print(f"Book Title: {lend['book_name']}")
            print(f"Return Date: {lend['Return_date']}")

            confirm = input("Do you want to return this book? (yes/no): ").lower()
            if confirm == "yes":
                # Update quantity in all_books
                for book in all_books:
                    if book["title"].lower() == lend["book_name"].lower():
                        book["quantity"] = int(book["quantity"]) + 1
                        break

                lend_books.remove(lend)

                with open("all_lend_books.json", "w") as lend_file:
                    json.dump(lend_books, lend_file, indent=4)

                with open("all_books.json", "w") as books_file:
                    json.dump(all_books, books_file, indent=4)

                print("\nBook has been successfully returned!")
                return
            else:
                print("Return cancelled.")
                return

    print("No matching book found in the lend list.")