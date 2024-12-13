import json

def save_all_lend_books(all_lend_books: object) -> object:
    with open("all_lend_books.json", "w") as fp:
        json.dump(all_lend_books, fp, indent=4)