'''Mercy Song -- Library catalog database application.'''
import sqlite3

#Storing the database to a variable
DATABASE = 'Library_Catalog.db'

#functions for books table
def print_all_books():
    #Show all the books in the library  
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM books;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

def print_all_books_sort_by_book_name():
    #Show all the books in the library order by book names   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM books ORDER BY book_name;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

def print_all_books_sort_by_author():
    #Show all the books in the library sort by authors 
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM books ORDER BY author;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

def print_all_books_by_sort_publish_year():
    #Show all the books in the library sort by published years  
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM books ORDER BY published_year;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

def print_all_books_sort_by_genre():
    #Show all the books in the library sort by genre  
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM books ORDER BY genre;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

def add_books():
    #adding more books to the library database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    bookname = input ('Enter your book name: ')
    author = input('Enter the author: ')
    sql = 'SELECT * FROM books;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()

# functions for borrowers table
def print_all_borrowers():
    '''Show all borrowers details'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('fist_name                     last_name                email')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}')
        #loop finished here
    db.close()

def print_all_borrowers_sort_by_first_names():
    '''Show all borrowers details and order them by their first names'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers ORDER BY first_name;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('fist_name                     last_name                email')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}')
        #loop finished here
    db.close()

def print_all_borrowers_sort_by_last_names():
    '''Show all borrowers details and order them by their last names'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers ORDER BY last_name;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('fist_name                     last_name                email')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}')
        #loop finished here
    db.close()

def print_all_borrowers_sort_by_emails():
    '''Show all borrowers details and order them by their emails'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers ORDER BY email;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('fist_name                     last_name                email')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}')
        #loop finished here
    db.close()


 #creating a while loop for the user to use the functions. 
while True:
# asking what the user want to do.
    user_input = input(
"""
What would you like to do?
a. See details about books
b. See details about the borrowers
c. See details about recent loans
d. Exit\n""")
    
    #If the user wants to see details about the books, ask if they want to do
    if user_input == 'a':
        user_input_for_books = input(
"""
What would you like to do?
1. Print all books
2. Print all books sort by book names
3. Print all books sort by authors
4. Print all books sort by genre
5. Print all books sort by published years
6. Exit\n""")
        #Call different functions when different numbers are inputed
        if user_input_for_books == '1':
            print_all_books()
        elif user_input_for_books == '2':
            print_all_books_sort_by_book_name()
        elif user_input_for_books == '3':
            print_all_books_sort_by_author()
        elif user_input_for_books == '4':
            print_all_books_sort_by_genre()
        elif user_input_for_books == '5':
            print_all_books_by_sort_publish_year()
        elif user_input_for_books == '6':
            break
        else:
            print('That is not an option.\n')


    #If the user wants to see details about the books, ask if they want to do
    if user_input == 'b':
        user_input_for_borrowers = input(
"""
What would you like to do?
1. Print all borrower details
2. Print all borrower details order by first names
3. Print all borrower details order by last names
4. Print all borrower details order by emails
5. Exit\n""")
        if user_input_for_borrowers == '1':
            print_all_borrowers()
        elif user_input_for_borrowers == '2':
            print_all_borrowers_sort_by_first_names()
        elif user_input_for_borrowers == '3':
            print_all_borrowers_sort_by_last_names()
        elif user_input_for_borrowers == '4':
            print_all_borrowers_sort_by_emails()
        elif user_input_for_borrowers == '5':
            break
        else:
            print('That is not an option.\n')

    if user_input == 'd':
        break


