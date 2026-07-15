import json
import os


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False


class Library:

    def __init__(self):
        self.books = {}
        self.load_books()

    def add_book(self):

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        if title in self.books:
            print("Book already exists.")
        else:
            self.books[title] = Book(title, author)
            print("Book added successfully.")

    def search_title(self):

        title = input("Enter Book Title: ")

        if title in self.books:
            book = self.books[title]
            print("\nBook Found")
            print("Title :", book.title)
            print("Author:", book.author)

            if book.issued:
                print("Status: Issued")
            else:
                print("Status: Available")

        else:
            print("Book not found.")

    def search_author(self):

        author = input("Enter Author Name: ")
        found = False

        for book in self.books.values():

            if book.author.lower() == author.lower():

                print("\nTitle :", book.title)

                if book.issued:
                    print("Status: Issued")
                else:
                    print("Status: Available")

                found = True

        if not found:
            print("No books found.")

    def issue_book(self):

        title = input("Enter Book Title: ")

        if title in self.books:

            if self.books[title].issued:
                print("Book is already issued.")
            else:
                self.books[title].issued = True
                print("Book issued successfully.")

        else:
            print("Book not found.")

    def return_book(self):

        title = input("Enter Book Title: ")

        if title in self.books:

            if self.books[title].issued:
                self.books[title].issued = False
                print("Book returned successfully.")
            else:
                print("Book was not issued.")

        else:
            print("Book not found.")

    def report(self):

        total = len(self.books)
        issued = 0

        for book in self.books.values():

            if book.issued:
                issued += 1

        print("\n------ Library Report ------")
        print("Total Books :", total)
        print("Issued Books:", issued)
        print("Available   :", total - issued)

    def save_books(self):

        data = []

        for book in self.books.values():

            data.append({
                "title": book.title,
                "author": book.author,
                "issued": book.issued
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_books(self):

        if os.path.exists("books.json"):

            with open("books.json", "r") as file:

                data = json.load(file)

                for item in data:

                    book = Book(item["title"], item["author"])
                    book.issued = item["issued"]

                    self.books[item["title"]] = book


library = Library()

while True:

    print("\n===== Library Book Inventory Manager =====")
    print("1. Add Book")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Library Report")
    print("7. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.search_title()

    elif choice == "3":
        library.search_author()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.report()

    elif choice == "7":
        library.save_books()
        print("Data saved successfully.")
        print("Thank you!")
        break

    else:
        print("Invalid choice.")