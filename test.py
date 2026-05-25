'''Mercy Song -- Library catalog database application.'''
import sqlite3

#Storing the database to a variable
DATABASE = 'Library_Catalog.db'

#functions for books table
def print_all_books():
    '''Show all the books in the library'''  
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
    '''Show all the books in the library order by columns'''
    options = {'1': "book_name", '2': "author", '3': "genre", '4': "published_year"}
    #Using a while loop and try except to make sure the code doesn't break
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
            #If the input is not an option in the list print the option doesn't exist and ask the user again
            print("Option doesn't exist.")


def add_books():
    '''adding more books to the library database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking user to enter something for each column
    bookname = input ('Enter your book name: ')
    author = input('Enter the author: ')
    genre = input('Enter the genre: ')
    publishyear = input('Enter the published year: ')
    #Put them into the database
    sql = f'INSERT INTO books (book_name, author, genre, published_year) VALUES("{bookname}", "{author}", "{genre}", "{publishyear}");'
    cursor.execute(sql)
    cursor.fetchall()
        #loop finished here
    db.commit()
    db.close()
        

def delete_books():
    '''Deleting books from the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Ask which book the user want to delete
    bookid = input ('What book do you what to delete? Please input the id of the book: ')
    sql = f'DELETE FROM books WHERE id = {bookid}'
    cursor.execute(sql)
    cursor.fetchall()
    db.commit()
    db.close()
    
# functions for borrowers table
def print_all_borrowers():
    '''Show all borrower details'''   
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM borrowers;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('borrower_id      first_name           last_name                email')
    for person in results:
        print(f'{person[0]:<17}{person[1]:<20}{person[2]:<25}{person[3]:<20}')
        #loop finished here
    db.close()


def print_all_borrowers_sort_by_columns():
    '''Show all the borrowers order by column''' 
    options = {'1': "first_name", '2': "last_name", '3': "email"}
    #Using a while loop and try except to make sure the code doesn't break
    while True:  
        columnname = input('How would you like to sort the borrowers?\n1.first_name\n2.last_name\n3.emails\n')
        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM borrowers ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            print('borrower_id      first_name          last_name                email')
            for person in results:
                print(f'{person[0]:<17}{person[1]:<20}{person[2]:<25}{person[3]:<20}')
                #loop finished here
            db.close()
            break
        except:
            #If the input is not an option in the list print the option doesn't exist and ask the user again
            print("Option doesn't exist.")


def add_borrowers():
    '''add borrowers to the borrowers table'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking user to input the information of the borrower
    first_name = input ('Enter the first name: ')
    last_name = input('Enter the last name: ')
    email = input('Enter the email: ')
    sql = f'INSERT INTO borrowers (first_name, last_name, email) VALUES("{first_name}", "{last_name}", "{email}");'
    cursor.execute(sql)
    cursor.fetchall()
        #loop finished here
    db.commit()
    db.close()
        

def delete_borrowers():
    '''delete borrowers from the borrowers table'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking which borrower the user wants to delete
    borrowerid = input ("Please enter borrower's id: ")
    sql = f'DELETE FROM borrowers WHERE id = {borrowerid}'
    cursor.execute(sql)
    cursor.fetchall()
    db.commit()
    db.close()

# functions for loans table
def print_all_loans():
    '''Show all the loans in the library ''' 
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM loans;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print('loan_id        book_id        borrower_id    loan_date           due_date            return_date')
    for loan in results:
        print(f'{loan[0]:<15}{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
        #loop finished here
    db.close()


def print_all_loans_sort_by_columns():
    '''Show all the loans in the library order by column names''' 
    options = {'1': "book_id", '2': "borrower_id", '3': "loan_date", '4': "due_date", '5': "return_date"}
    while True:  
        #Using a while loop and try except to make sure the code doesn't break
        columnname = input('How would you like to sort the borrowers?\n1.books\n2.borrowers\n3.loan_date\n4.due_date\n5.return_date\n')
        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM loans ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            print('loan_id        book_id        borrower_id    loan_date           due_date            return_date')
            for loan in results:
                print(f'{loan[0]:<15}{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
                #loop finished here
            db.close()
            break
        except:
            #If the input is not an option in the list print the option doesn't exist and ask the user again
            print("Option doesn't exist.")


def add_loans():
    '''add loans to the loans table'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking the user to input the information of the loan
    book_id = input ('Enter the book id: ')
    borrower_id = input('Enter the borrower id: ')
    loan_date = input('Enter the loan date: ')
    due_date = input('Enter the due date: \n(loan date + 15 days)')
    return_date = input('Enter the return date: \n(if not returned, please enter Not returned)')
    sql = f'INSERT INTO borrowers (book_id, borrower_id, loan_date, due_date, return_date) VALUES("{book_id}", "{borrower_id}", "{loan_date}", "{due_date}", "{return_date}");'
    cursor.execute(sql)
    cursor.fetchall()
        #loop finished here
    db.commit()
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
2. Sort all books
3. Add books
4. Delete books
5. Exit\n""")
        #Call different functions when different numbers are inputed
        if user_input_for_books == '1':
            print_all_books()
        elif user_input_for_books == '2':
            print_all_books_sort_by_columns()
        elif user_input_for_books == '3':
            add_books()
        elif user_input_for_books == '4':
            delete_books()
        elif user_input_for_books == '5':
            break
        else:
            print('That is not an option.\n')


    #If the user wants to see details about the books, ask if they want to do
    elif user_input == 'b':
        user_input_for_borrowers = input(
"""
What would you like to do?
1. Print all borrower details
2. Sort borrower details 
3. Add borrower
4. Delete borrower
5. Exit\n""")
        #Call different functions when different numbers are inputed
        if user_input_for_borrowers == '1':
            print_all_borrowers()
        elif user_input_for_borrowers == '2':
            print_all_borrowers_sort_by_columns()
        elif user_input_for_borrowers == '3':
            add_borrowers()
        elif user_input_for_borrowers == '4':
            delete_borrowers()
        elif user_input_for_borrowers == '5':
            break
        else:
            print('That is not an option.\n')
    elif user_input == 'c':
        user_input_for_loans = input(
"""
What would you like to do?
1. Print all loans 
2. Sort recent loans
3. Exit\n""")
        if user_input_for_loans == '1':
            print_all_loans()
        elif user_input_for_loans == '2':
            print_all_loans_sort_by_columns()
        elif user_input_for_borrowers == '3':
            break    
    else:
        if user_input == 'd':
            break


