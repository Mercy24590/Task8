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

'''def add_books():
    #adding more books to the library database
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
    db.close()'''

# functions for borrowers table
def print_all_borrowers():
    '''Show all borrowers details'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('borrower_id                    author                   genre               publish_year')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}{person[4]:<20}')
        #loop finished here
    db.close()

def print_all_borrowers():
    '''Show all borrowers details'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('borrower_id                    author                   genre               publish_year')
    for person in results:
        print(f'{person[1]:<30}{person[2]:<25}{person[3]:<20}{person[4]:<20}')
        #loop finished here
    db.close()
    
while True:
    user_input = input(
"""
What would you like to do.
1. Print all books
2. Print all books sort by book names
3. Print all books sort by authors
4. Print all books sort by genre
5. Print all books sort by published years
6. Print all books sort by 
7. Exit\n""")
    if user_input == '1':
        print_all_books()
    if user_input == '2':
        print_all_books_sort_by_book_name()
    if user_input == '3':
        print_all_books_sort_by_author()
    if user_input == '4':
        print_all_books_sort_by_genre()



