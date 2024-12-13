import save_all_books
from datetime import datetime
import save_all_lend_book
lend_lists = []

def lend_book(all_lend_book):
    find_book = input("Search for lend using book title: ")
    is_find = False

    for book in all_lend_book:
        if book["title"].lower() == find_book.lower() and book["quantity"] > 0:
            is_find = True
            borrow_name = input("Book Lended By (Name): ")
            borrow_mobile = input("Enter Mobile Number: ")

            while True:
                try:
                    user_input = input("Enter Return Date (YYYY-MM-DD): ")
                    return_date = datetime.strptime(user_input, "%Y-%m-%d").strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format! Please use YYYY-MM-DD.")


            book["quantity"] -= 1


            book_lend = {
                "Borrow_name": borrow_name,
                "Mobile": borrow_mobile,
                "Return_date": return_date,
                "book_name": book['title'],
                "book_author": book['author'],
                "book_isbn": book['isbn']
            }

            lend_lists.append(book_lend)
            print(f"Successfully Lend A Book to {borrow_name}")
            break

    if not is_find:
        print("Book is Not in Store")

    save_all_books.save_all_books(all_lend_book)
    save_all_lend_book.save_all_lend_books(lend_lists)

    return lend_lists