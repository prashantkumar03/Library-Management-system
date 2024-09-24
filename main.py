from booklibrary import bookDB

# Starting index for ISBN generation
index = 5

LIBRARIAN_ID = "Prashant123"
LIBRARIAN_PASSWORD = "8055"

def generate_isbn(index):
    # Simple ISBN format: "978-3-16-148410-0" with unique index
    return f"978-3-16-148410-{index:02d}"

def librarianLogin():
    print("Librarian Login")
    librarian_id = input("Enter librarian ID: ")
    librarian_password = input("Enter password: ")
    if librarian_id == LIBRARIAN_ID and librarian_password == LIBRARIAN_PASSWORD:
        print("Librarian login successful!")
        return True
    else:
        print("Invalid ID or password. Access denied.")
        return False

def userLogin():
    print("User Login")
    user_name = input("Enter your name: ")
    print(f"User login successful! Welcome, {user_name}.")
    return user_name

def addBook():
    global index
    index += 1
    title = input("Enter Your Book Name: ")
    author = input("Enter author name: ")
    status = input("Enter the status (e.g., available, checked out): ")
    isbn = generate_isbn(index)
    booksInfo = {
        "title": title,
        "author": author,
        "ISBN": isbn,
        "status": status,
        "borrower": None
    }
    bookDB.append(booksInfo)
    print("Book added successfully.")
    print(bookDB)
    while True:
        moreBookadding = input("Do you want to add more books (yes/no): ").lower()
        if moreBookadding == "yes":
            addBook()
            break
        elif moreBookadding == "no":
            main()
            break
        else:
            print("Invalid Input! Enter Again")

def deleteBook():
    while True:
        gettingISBN = input("Enter the Book ISBN to delete: ")
        if len(gettingISBN) > 0:
            bookISBN = gettingISBN
            break
        else:
            print("Please enter a valid ISBN.")

    book_to_delete = None
    for book in bookDB:
        if book["ISBN"] == bookISBN:
            book_to_delete = book
            break

    if book_to_delete:
        bookDB.remove(book_to_delete)
        print("Book deleted successfully.")
    else:
        print("No book found with the given ISBN.")
    print(bookDB)

def listBooks():
    print(bookDB)

def searchBookBy():
    search_book = input("Enter the title, author, or ISBN you want to search for: ").lower()
    found_book = []
    for book in bookDB:
        if (search_book in book['title'].lower() or
                search_book in book['author'].lower() or
                search_book in book['ISBN'].lower()):
            found_book.append(book)
    if found_book:
        for found_books in found_book:
            print("Title:", found_books['title'])
            print("Author:", found_books['author'])
            print("ISBN:", found_books['ISBN'])
            print("Status:", found_books['status'])
            if found_books['borrower']:
                print("Borrower:", found_books['borrower'])
    else:
        print("No books found matching the search.")

def borrowBook():
    while True:
        isbn = input("Enter the ISBN of the book you want to borrow: ")
        if len(isbn) > 0:
            break
        else:
            print("Please enter a valid ISBN.")

    for book in bookDB:
        if book['ISBN'] == isbn:
            if book['status'] == 'available':
                borrower = input("Enter your name: ")
                book['status'] = 'checked out'
                book['borrower'] = borrower
                print(f"You have borrowed '{book['title']}'.")
            else:
                print(f"Sorry, '{book['title']}' is already checked out.")
            return

    print("No book found with the given ISBN.")

def returnBook():
    while True:
        isbn = input("Enter the ISBN of the book you want to return: ")
        if len(isbn) > 0:
            break
        else:
            print("Please enter a valid ISBN.")

    for book in bookDB:
        if book['ISBN'] == isbn:
            if book['status'] == 'checked out':
                book['status'] = 'available'
                book['borrower'] = None
                print(f"Thank you for returning '{book['title']}'.")
            else:
                print(f"'{book['title']}' was not checked out.")
            return

    print("No book found with the given ISBN.")

def showBorrowedBooks():
    borrowed_books = [book for book in bookDB if book['status'] == 'checked out']
    if borrowed_books:
        print("Borrowed Books:")
        for book in borrowed_books:
            print(
                f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Borrower: {book['borrower']}")
    else:
        print("No books are currently borrowed.")

def trackBorrowedBooks():
    borrowed_books = [book for book in bookDB if book['status'] == 'checked out']
    if borrowed_books:
        print("Tracking Borrowed Books:")
        for book in borrowed_books:
            print(
                f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Borrower: {book['borrower']}")
    else:
        print("No books are currently borrowed.")

def librarianMenu():
    while True:
        try:
            print("\nLibrarian Menu:")
            print("1. Add a book")
            print("2. Delete a book")
            print("3. List all books")
            print("4. Search for a book")
            print("5. Show borrowed books")
            print("6. Track borrowed books")
            print("7. Exit")
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                print("Add the book to your DB:")
                addBook()
            elif choice == 2:
                print("To delete a book: ")
                deleteBook()
            elif choice == 3:
                print("Showing all books:")
                listBooks()
            elif choice == 4:
                print("Search your book: ")
                searchBookBy()
            elif choice == 5:
                print("Showing borrowed books:")
                showBorrowedBooks()
            elif choice == 6:
                print("Tracking borrowed books:")
                trackBorrowedBooks()
            elif choice == 7:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def userMenu(user_name):
    while True:
        try:
            print("\nUser Menu:")
            print("1. List all books")
            print("2. Search for a book")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. Exit")
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                print("Showing all books:")
                listBooks()
            elif choice == 2:
                print("Search your book: ")
                searchBookBy()
            elif choice == 3:
                print("Borrow a book:")
                borrowBook()
            elif choice == 4:
                print("Return a book:")
                returnBook()
            elif choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nWelcome to the Library System")
        print("1. Librarian Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            if librarianLogin():
                librarianMenu()
        elif choice == '2':
            user_name = userLogin()
            userMenu(user_name)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
