"""
Author: Alvaro Salazar
Date: August 7, 2022. 

Specification:
WhatABook, a small used book store has decided to expand their presence by offering customers a solution they can install on their personal computers.
WhatABook would like to establish a console application that allows customers to browse their in-store book listing, add books to their Wishlist, 
and view store hours and locations. Right now, they only have one location, but the owner, Hugo Dopsen, is emphatic about expanding. 
Hugo would like the new applications interface to be as simplistic as possible. 
Most of their users will be middle aged customers with minimal computer experience. 
Customers will need to register for a free account by providing their email address, first, and last name. 
The program should support options for viewing a list of their in-store books, adding books to their Wishlist, and viewing store hours and locations.
Example: Interface
    Menu
        1. View Books
        2. View Store Locations
        3. My Account
            ■ Prompt the user to enter a user_id
                ● 1,2,or3
                ● Note: before a user can access their account, they must enter a valid user_id.
            ■ Wishlist Menu
                1. Wishlist
                2. Add Book
                    ○ Display the the available books
                        ■   The output will show the book_id, book_name, author, and details
                    ○ Prompt the user to select a book to add to their wishlist 
                        ■   To add a book to the users Wishlist, the insert
                            statement will need the book_id and user_id
                            
                3. Main menu
                    ○ This option takes users back to the main menu
        4. Exit Program
            ■ Exits the program
            
User Interface Guidance/Hints
    ● Create a method to for “show_menu()”
    ● Create a method for “show_books(_cursor)”
    ● Create a method for “show_locations(_cursor)”
    ● Create a method for “validate_user()”
    ● Create a method for “show_account_menu()”
    ● Create a method for “show_wishlist(_cursor, _user_id)”
    ● Create a method for “show_books_to_add(_cursor, _user_id)”
    ● Create a method for “add_book_to_wishlist(_cursor, _user_id, _book_id)”
    ● Create a method to display the account menu
    ● Use variables to capture the user’s entry for user_id
    ● User variables to capture the user’s entry for book_id

"""
# Imports

import sys
import mysql.connector 
from mysql.connector import errorcode

""" database config object """

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True,
}

# Methods

def show_menu():
    print("\n-- Main Menu --")

    print("    1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program")

    try:
        options=int(input('      <Example, Type 1 to see the list of books>: '))

        return options
    except ValueError:
        print("\nInvalid number, Try again with a valid option...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details, store_id from book")

    # get the results from the cursor
    books=_cursor.fetchall()

    print("\n--- SHOWING THE LIST OF BOOKS ---")

    # iterate over the books data, and display the results
     
    for book in books:
        print("  Book Name: {}\nAuthor: {}\nDetails: {}\nStore: {}\n".format(book[1], book[2], book[3], book[4]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations=_cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    """ validate the users ID """

    try:
        user_id=int(input('\nEnter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\nInvalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_account_menu():
    """ display the users account menu """

    try:
        print("\n-- Customer Menu --")
        print("        1. Wishlist\n2. Add Book\n3. Main Menu")
        account_option=int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author "+
                    "FROM wishlist "+
                    "INNER JOIN user ON wishlist.user_id = user.user_id "+
                    "INNER JOIN book ON wishlist.book_id = book.book_id "+
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist=_cursor.fetchall()

    print("\n-- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query=("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add=_cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ try/catch block for handling potential MySQL database errors """

    #db=mysql.connector.connect(**config) # connect to the WhatABook database 
    
    # Connect to whatabook database
    
    db = mysql.connector.connect(user='whatabook_user', password='MySQL8IsGreat!',
                              host='127.0.0.1', database='whatabook',
                              auth_plugin='mysql_native_password')
    
    

    cursor=db.cursor() # cursor for MySQL queries

    print("\nWelcome to the WhatABook Application! ")

    user_selection=show_menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id=validate_user()
            account_option=show_account_menu()

            # while account option does not equal 3
            while account_option!=3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id=int(input("\nEnter the id of the book you want to add: "))

                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\nBook id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please retry...")

                # show the account menu 
                account_option=show_account_menu()

        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")

        # show the main menu
        user_selection=show_menu()

    print("\n\nProgram terminated...")

except mysql.connector.Erroraserr:
    """ handle errors """

    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close() 
