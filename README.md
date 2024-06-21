Library Management System
This Library Management System is a Python-based application with a GUI that allows users to manage books, borrowers, and borrowing details. It uses MySQL for data storage and management.

Features
    User Management:
        Add, edit, and delete borrower details including name, address, and mobile number.
    Book Management:
        Add, edit, and delete book details such as title, author, price, etc.
    Borrowing Management:
        Track borrowing details including which borrower borrowed which book, borrowing date, and expected return date.
        Calculate late return fines based on the number of days past the expected return date.
    Fine Calculation:
        Automatically calculates fines for late returns based on pre-defined rules (e.g. per-day fine).

Requirements
    1. Python 3.x
    2. MySQL (with required Python libraries like mysql-connector-python)
    3. Tkinter (Python's de-facto standard GUI library)

Installation and Setup
    1. Clone the repository:
        git clone https://github.com/Samimeel/Library-Management-System.git
        cd repository

    2. Install dependencies:
        pip install mysql-connector-python

    3. Database setup:
        Create a MySQL database and import the schema from mydata.sql.

    4. Configuration:
        Modify config.py file to set up MySQL connection details.

    5.  Run the application:
        python main.py

Usage : 
    Upon launching the application (main.py), the GUI interface will be displayed.
    Use the various buttons and forms to add, edit, or delete books and borrowers.
    Manage borrowings and track fines from the respective interfaces.
