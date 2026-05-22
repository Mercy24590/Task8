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
    print('book_id     book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[0]:<12}{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
        #loop finished here
    db.close()


def print_all_books_sort_by_columns():
    #Show all the books in the library order by book names 
    options = {'1': "book_name", '2': "author", '3': "genre", '4': "published_year"}
    while True:  
        columnname = input('How would you like to sort the books?\nBy 1.book_name\n2.author\n3.genre\n4.published_year\n')
        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM books ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            print('book_id     book_name                     author                   genre               publish_year')
            for book in results:
                print(f'{book[0]:<12}{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
                #loop finished here
            db.close()
            break
        except:
            print("Option doesn't exist.")


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
    print('book_id     book_name                     author                   genre               publish_year')
    for book in results:
        print(f'{book[0]:<12}{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
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


def print_all_borrowers_sort_by_columns():
    #Show all the books in the library order by book names 
    options = {'1': "book_name", '2': "author", '3': "genre", '4': "published_year"}
    while True:  
        columnname = input('How would you like to sort the books?\nBy 1.book_name\n2.author\n3.genre\n4.published_year\n')
        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM books ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            print('book_name                     author                   genre               publish_year')
            for book in results:
                print(f'{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
                #loop finished here
            db.close()
            break
        except:
            print("Option doesn't exist.")

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


# functions for loans tablec
def print_all_loans():
    #Show all the loans in the library  
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
        #loop finished here
    db.close()


def print_all_loans_order_by_book_id():
    #Show all the loans sort by books  
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans ORDER BY book_id;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
        #loop finished here
    db.close()


def print_all_loans_order_by_borrower_id():
    #Show all the loans sort by borrowers
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans ORDER BY borrower_id;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
        #loop finished here
    db.close()


def print_all_loans_order_by_loan_dates():
    #Show all the loans sort by loan dates
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans ORDER BY loan_date;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('loan_id       book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[0]:<15}{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
        #loop finished here
    db.close()


def print_all_loans_order_by_due_dates():
    #Show all the loans sort by due dates
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans ORDER BY due_date;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
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
2. Print sort all books
3. add books
4. Exit\n""")
        #Call different functions when different numbers are inputed
        if user_input_for_books == '1':
            print_all_books()
        elif user_input_for_books == '2':
            print_all_books_sort_by_columns()
        elif user_input_for_books == '3':
            add_books()
        elif user_input_for_books == '4':
            break
        else:
            print('That is not an option.\n')


    #If the user wants to see details about the books, ask if they want to do
    elif user_input == 'b':
        user_input_for_borrowers = input(
"""
What would you like to do?
1. Print all borrower details
2. Print all borrower details order by first names
3. Print all borrower details order by last names
4. Print all borrower details order by emails
5. Exit\n""")
        #Call different functions when different numbers are inputed
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
    elif user_input == 'c':
        user_input_for_loans = input(
"""
What would you like to do?
1. Print all loans 
2. Print all loans sort by books
3. Print all loans sort by borrowers
4. Print all loans sort by loan dates
5. Print all loans sort by due dates
6. Print all loans sort by return dates
7. Exit\n""")
        if user_input_for_loans == '1':
            print_all_loans()
        elif user_input_for_loans == '2':
            print_all_loans_order_by_book_id()
        elif user_input_for_loans == '3':
            print_all_borrowers_sort_by_last_names()
        elif user_input_for_loans == '4':
            print_all_borrowers_sort_by_emails()
        elif user_input_for_borrowers == '5':
            print_all_borrowers_sort_by_emails()
        elif user_input_for_borrowers == '6':
            print_all_borrowers_sort_by_emails()
        elif user_input_for_borrowers == '7':
            break
        
    else:
        if user_input == 'd':
            break


