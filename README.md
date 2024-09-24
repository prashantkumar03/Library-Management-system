Library Management System


This project implements a simple library management system that allows librarians and users to manage books in a library.
It includes functionalities for adding, deleting, listing, searching, borrowing, and returning books.

Features
Librarian Login: Authenticate librarians with an ID and password.
User Login: Authenticate users with their name.
Add a Book: Add new books with details including title, author, status, and ISBN.
Delete a Book: Remove books from the library using their ISBN.
List All Books: Display all books available in the library.
Search for a Book: Search for books by title, author, or ISBN.
Borrow a Book: Check out books from the library.
Return a Book: Return borrowed books to the library.
Show Borrowed Books: List all currently borrowed books.
Track Borrowed Books: Track the status and details of borrowed books.


Main Menu
Upon running the program, you will be presented with the following options:

Librarian Login: Access the librarian functionalities.
User Login: Access the user functionalities.
Exit: Exit the program.
Librarian Menu
After logging in as a librarian, you can choose from the following options:

Add a Book: Enter details to add a new book to the library.
Delete a Book: Remove a book using its ISBN.
List All Books: View all books in the library.
Search for a Book: Search for a book by title, author, or ISBN.
Show Borrowed Books: View all currently borrowed books.
Track Borrowed Books: Track borrowed books and their details.
Exit: Exit the librarian menu.
User Menu
After logging in as a user, you can choose from the following options:

List All Books: View all books in the library.
Search for a Book: Search for a book by title, author, or ISBN.
Borrow a Book: Borrow a book from the library.
Return a Book: Return a borrowed book.
Exit: Exit the user menu.
Code Details
ISBN Generation: The generate_isbn function creates a unique ISBN based on a simple format with an incremented index.
Librarian and User Authentication: The librarianLogin and userLogin functions handle login procedures.
Book Management: Functions such as addBook, deleteBook, listBooks, searchBookBy, borrowBook, and returnBook manage book operations.
Borrowing and Tracking: Functions like showBorrowedBooks and trackBorrowedBooks provide details on borrowed books.
