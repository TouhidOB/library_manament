import add_books
import view_all_books
import restore_books_file
from return_lended_book import return_book

import update_book_file, delete_book_file
import lend_book

import json


all_books = []



def lend_book_view():
    try:
        # Load lent books from the JSON file
        with open("all_lend_books.json", "r") as fp:
            all_lend_books_list = json.load(fp)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No Lend Books Found or File is Corrupted.")
        return


    if all_lend_books_list:

        for record in all_lend_books_list:
            print(
                f"Borrower Name: {record['Borrow_name']} | "
                f"Mobile: {record['Mobile']} | "
                f"Return Date: {record['Return_date']} | "
                f"Book Title: {record['book_name']} | "
                f"Author: {record['book_author']} | "
                f"ISBN: {record['book_isbn']}"
            )
    else:
        print("No Books Have Been Lent...")


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend A Book")
    print("6. View Lend List")
    print("7. Return Lended Book")

    all_books = restore_books_file.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        lend_book.lend_book(all_books)
    elif menu == "6":
        lend_book_view()
    elif menu == "7":
        return_book()
    else:
        print("Choose a valid number")