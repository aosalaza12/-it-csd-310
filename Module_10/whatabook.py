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

from ast import Break
import sys
from xmlrpc.client import boolean
import mysql.connector 
from mysql.connector import errorcode

# global variables.
valid = False 

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
    #print("\n-- Main Menu --")
    print()
    print('\33[34m' + '   --  Main Menu  -- '+ '\33[34m')
    print('\33[0m')
    print("")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        print()
        options=int(input('      <Option : '))

        return options
    except ValueError:
        print()
        print("\nOption Invalid, Try again with a valid option...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details, store_id from book")

    # get the results from the cursor
    books=_cursor.fetchall()

    print("\n--- SHOWING THE LIST OF BOOKS ---")

    # iterate over the books data, and display the results
     
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n  Store: {}\n".format(book[1], book[2], book[3], book[4]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale, hour_open, hour_closed from store")

    locations=_cursor.fetchall()

    print("\n-- SHOWING STORE LOCATIONS --")
    print()

    for location in locations:
        print("  Locale   : {}\n  Opens at : {} am\n  Closes at: {} pm".format(location[1], location[2], location[3]))

def validate_user():
    """ validate the users ID """

    try:
        valid = True        
        user_id=int(input('\nEnter a User id : '))

        if user_id < 0 or user_id > 3:
            print("\n     Invalid User id...\n")
            #sys.exit(0)
            valid = False
        return (user_id, valid)
    
    except ValueError:
        print("\nInvalid User, \n")
    
        sys.exit()
        
def get_user(my_user_id):
    cursor.execute("SELECT first_name FROM user"+ " WHERE user_id = {}".format(my_user_id))
    fname = cursor.fetchone()
    
    cursor.execute("SELECT last_name FROM user"+ " WHERE user_id = {}".format(my_user_id))
    lname = cursor.fetchone()
        
    name = fname + lname 
                
    return name
    
        
def show_account_menu():
    """ display the users account menu """
    try:
        user_name = get_user(my_user_id)
        user_n = user_name[0]+ " " + user_name[1]
                     
        #print("\n-- User Menu -- ", user_n)
        print('\33[41m' + '               User Menu  - ', user_n + '\33[40m')
        print()
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option=int(input('        <Enter your option: >: '))
        print('\33[0m')

        return account_option
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, store.locale "+
                    "FROM wishlist "+
                    "INNER JOIN user ON wishlist.user_id = user.user_id "+
                    "INNER JOIN book ON wishlist.book_id = book.book_id "+
                    "INNER JOIN store ON store.store_id = book.store_id "+
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist=_cursor.fetchall()

    print("\n    -- SHOWING WISHLIST  --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n        Locale: {}\n".format(book[4], book[5], book[6]))

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query=("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

#    print(query)

    _cursor.execute(query)

    books_to_add=_cursor.fetchall()

    print("\n-- SHOWING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ try/catch block for handling potential MySQL database errors """

        # Connect to whatabook database
    
    db = mysql.connector.connect(user='whatabook_user', password='MySQL8IsGreat!',
                              host='127.0.0.1', database='whatabook',
                              auth_plugin='mysql_native_password')
    
    

    cursor=db.cursor() # cursor for MySQL queries
    print()
    #print('\033[1m' + '               WELCOME TO THE WHATABOOK APPLICATION' + '\033[0m')
    print('\33[41m' + '               WELCOME TO THE WHATABOOK APPLICATION' + '\33[40m')

    user_selection=show_menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method  
        # call the show_account_menu() to show the account menu
        if user_selection == 3:
            my_user =validate_user()
            
            
            if my_user[1] == True:
                my_user_id = my_user[0]
                account_option=show_account_menu()

            # while account option does not equal 3
                while account_option!=3:

                # Call the show_wishlist() method to display the current users 
                # 
                    if account_option == 1:
                        show_wishlist(cursor, my_user_id)
                        

                # Call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                    if account_option == 2:

                    # show the books not currently configured in the users wishlist
                        show_books_to_add(cursor, my_user_id)

                    # get the book_id 
                        book_id=int(input("\nEnter the id of the book to be included in the list: "))

                    # add the selected book the users wishlist
                        add_book_to_wishlist(cursor, my_user_id, book_id)

                        db.commit() # commit the changes to the database 

                        print("\nBook id: {} was added to your wishlist!".format(book_id))
                        

                    # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                    if account_option < 0 or account_option > 3:
                        print("\nInvalid option, please retry...")

                    # show the account menu 
                    account_option=show_account_menu()
            else:
                pass
                
            

        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")

        # show the main menu
        user_selection=show_menu()

    print("\n\nProgram terminated...")

except mysql.connector.Error as err:
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
