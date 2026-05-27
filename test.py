'''Mercy Song -- Library catalog database application.'''
import sqlite3

#Storing the database to a variable
DATABASE = 'Library_Catalog.db'

#functions for books table
def print_all_books():
    '''Show all the books in the library'''  
    #Connect python and database
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
    #close the database
    db.close()


def print_all_books_sort_by_columns():
    '''Show all the books in the library order by columns'''
    #Creating a list to store all the options
    options = {'1': "book_name", '2': "author", '3': "genre", '4': "published_year"}
    #Using a while loop and try except to make sure the code doesn't break
    while True:  
        columnname = input('How would you like to sort the books?\n1.book_name\n2.author\n3.genre\n4.published_year\n')
        try:
            #Connect python and database
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM books ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            #print out the table nicely
            print('book_id     book_name                     author                   genre               publish_year')
            for book in results:
                print(f'{book[0]:<12}{book[1]:<30}{book[2]:<25}{book[3]:<20}{book[4]:<20}')
                #loop finished here
            #close the database
            db.close()
            #break the loop after printing out the table
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
    #Commit all changes made in the database
    db.commit()
    #close the database
    db.close()
        

def delete_books():
    '''Deleting books from the database'''
    #Using a while loop to make sure the code doesn't break when a string is entered.
    while True:
        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #Ask which book the user want to delete
            bookid = int(input ('What book do you what to delete? Please input the id(number format) of the book: '))
            sql = f'DELETE FROM books WHERE id = {bookid}'
            cursor.execute(sql)
            cursor.fetchall()
            #Commit all changes made in the database
            db.commit()
            #close the database
            db.close()
            #break the loop when the changes are made in the database
            break
        except:
            print('Please enter a valid id.')
        
# functions for borrowers table
def print_all_borrowers():
    '''Show all borrower details''' 
    #connecting python and database  
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
    #close the database
    db.close()


def print_all_borrowers_sort_by_columns():
    '''Show all the borrowers order by column''' 
    #Creating a list to store all the options
    options = {'1': "first_name", '2': "last_name", '3': "email"}
    #Using a while loop and try except to make sure the code doesn't break
    while True:  
        columnname = input('How would you like to sort the borrowers?\n1.first_name\n2.last_name\n3.emails\n')
        try:
            #connecting python and database
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
            #close the database
            db.close()
            #break the loop after printing out the table
            break
        except:
            #If the input is not an option in the list print the option doesn't exist and ask the user again
            print("Option doesn't exist.")


def add_borrowers():
    '''add borrowers to the borrowers table'''
    #connecting python and database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking user to input the information of the borrower
    first_name = input ('Enter the first name: ')
    last_name = input('Enter the last name: ')
    email = input('Enter the email: ')
    #Use the variables that stored the inputs in sql
    sql = f'INSERT INTO borrowers (first_name, last_name, email) VALUES("{first_name}", "{last_name}", "{email}");'
    cursor.execute(sql)
    cursor.fetchall()
    #Commit all changes made in the database
    db.commit()
    #close the database
    db.close()
        

def delete_borrowers():
    '''delete borrowers from the borrowers table'''
    #Using a while loop to make sure the code doesn't break when a string is entered.
    while True:
        try:
            #connecting python and database
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #Asking which borrower the user wants to delete, converting their input into a integer, so if something else is entered the code will move on to except
            borrowerid = int(input ("Please enter borrower's id: "))
            sql = f'DELETE FROM borrowers WHERE borrower_id = {borrowerid};'
            cursor.execute(sql)
            cursor.fetchall()
            #Commit all changes made in the database 
            db.commit()
            #close the database
            db.close()
            #break the loop when the changes are made in the database
            break
        except:
            #catches any invalid inputs and made sure the code doesn't break
            print('Please enter a valid id.')
            break

# functions for loans table
def print_all_loans():
    '''Show all the loans in the library ''' 
    #connecting python and database
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
    #close the database
    db.close()


def print_all_loans_sort_by_columns():
    '''Show all the loans in the library order by column names''' 
    #Creating a list to store all the options
    options = {'1': "book_id", '2': "borrower_id", '3': "loan_date", '4': "due_date", '5': "return_date"}
    while True:  
        #Using a while loop and try except to make sure the code doesn't break
        columnname = input('How would you like to sort the borrowers?\n1.books\n2.borrowers\n3.loan_date\n4.due_date\n5.return_date\n')
        try:
            #connecting python and database
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = f'SELECT * FROM loans ORDER BY {options[columnname]} ASC;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #loop through all the results
            #print the table nicely
            print('loan_id        book_id        borrower_id    loan_date           due_date            return_date')
            for loan in results:
                print(f'{loan[0]:<15}{loan[1]:<15}{loan[2]:<15}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}')
                #loop finished here
            #close the database
            db.close()
            break
        except:
            #If the input is not an option in the list print the option doesn't exist and ask the user again
            print("Option doesn't exist.")


def add_loans():
    '''add loans to the loans table'''
    #connecting python and database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #Asking the user to input the information of the loan
    book_id = input ('Enter the book id: ')
    borrower_id = input('Enter the borrower id: ')
    loan_date = input('Enter the loan date: ')
    due_date = input('Enter the due date (loan date + 15 days): ')
    return_date = input('Enter the return date (if not returned, please enter Not returned):')
    #Use the user's inputs in the sql
    sql = f'INSERT INTO loans (book_id, borrower_id, loan_date, due_date, return_date) VALUES("{book_id}", "{borrower_id}", "{loan_date}", "{due_date}", "{return_date}");'
    cursor.execute(sql)
    cursor.fetchall() 
    #Commit all changes made in the database 
    db.commit()
    #close the database
    db.close()


def add_return_date():
    '''allows user to add the return date when a book is returned'''
    #Use a while loop to keep asking for inputs until a valid input is entered
    while True:
        try: 
            #connecting python and database
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #asking the user where they want to add the return date
            loan_id = int(input('Enter the loan id: '))
            return_date = input('Enter the return date (year-month-date): ')
            #using the user inputs in sql
            sql = f'UPDATE Loans SET return_date = "{return_date}" WHERE loan_id = {loan_id};'
            cursor.execute(sql)
            cursor.fetchall()
            #Commit the changes in database
            db.commit()
            #close the database
            db.close()
            #break the loop when the changes are made in the database
            break
        #catches any invalid inputs and made sure the code doesn't break
        except:
            print('Please enter a valid id.')


def show_a_persons_loans():
    '''allow user to check the loans for a specific person.'''
    #Use a while loop to keep asking for inputs until a valid input is entered
    while True:
        try:
            #connecting python and database
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #asking which person's loans they want to see
            borrower_id = int(input("Enter the borrower's id: "))
            #connecting all the tables by comparing the borrower id and book id in the loans table to the borrower id and book id in the borrowers and books table and put all the information together.
            sql = f'SELECT Loans.*, Borrowers.first_name, Borrowers.last_name, Books.book_name FROM Books, Borrowers, Loans WHERE Loans.borrower_id = {borrower_id} AND loans.borrower_id = Borrowers.borrower_id AND Loans.book_id = Books.id;'
            cursor.execute(sql)
            results = cursor.fetchall()
            #print the results nicely in one table
            print('loan_id   borrower_id    name           book_id   book_name      loan_date      due_date       return_date')
            for loan in results:
                print(f'{loan[0]:<10}{loan[2]:<15}{loan[6]:<6}{loan[7]:<9}{loan[1]:<10}{loan[8]:<15}{loan[3]:<15}{loan[4]:<15}{loan[5]:<10}')
                #loop finished here
            #close the database
            db.close()
            #break the loop 
            break
        #catches any invalid inputs and made sure the code doesn't break
        except:
            print('Please enter a valid id.')


#creating a while loop for the user to use the functions. 
print('Welcome to my library catalog database. In this program you will be able to check the books, borrowers and recent loans. You are also able to and make changes to these data.')
while True:
# asking what the user want to do.
    user_input = input(
"""
What would you like to do?
a. See details about books
b. See details about the borrowers
c. See details about recent loans
d. Exit\n""")
    
    #If the user wants to see details about the books, show the options
    if user_input == 'a':
        #Using another while loop to keep showing the manual for books until the user enter a valid number.
        while True:
            try:
                #Convert the input into a integer, which allows try and except statement to catch any input that is not an integer.
                user_input_for_books = int(input(
"""
What would you like to do?
1. Print all books
2. Sort all books
3. Add books
4. Delete books
5. Go back to the main manual\n"""))

                #Call different functions when different numbers are entered
                if user_input_for_books == 1:
                    print_all_books()
                elif user_input_for_books == 2:
                    print_all_books_sort_by_columns()
                elif user_input_for_books == 3:
                    add_books()
                elif user_input_for_books == 4:
                    delete_books()
                elif user_input_for_books == 5:
                    break
                #catches all the numbers out of range
                else:
                    print('That is not an option.\n')
            except:
                    #when the input doesn't meet any of the conditions above, print that is not an option.
                    print('That is not an option.\n')


    #If the user wants to see details about the borrowers, ask what they want to do
    elif user_input == 'b':
        #Using another while loop to keep showing the manual for books until the user enter a valid number.
        while True:
            try:
                #Convert the input into a integer, which allows try and except statement to catch any input that is not an integer
                user_input_for_borrowers = int(input(
"""
What would you like to do?
1. Print all borrower details
2. Sort borrower details 
3. Add borrower
4. Delete borrower
5. Go back to the main manual\n"""))
                #Call different functions when different numbers are entered
                if user_input_for_borrowers == 1:
                    print_all_borrowers()
                elif user_input_for_borrowers == 2:
                    print_all_borrowers_sort_by_columns()
                elif user_input_for_borrowers == 3:
                    add_borrowers()
                elif user_input_for_borrowers == 4:
                    delete_borrowers()
                elif user_input_for_borrowers == 5:
                    break
                #catches all the numbers out of range
                else:
                    print('That is not an option.\n')
            except:
                #when the input doesn't meet any of the conditions above, print that is not an option.
                print('That is not an option.\n')


    #If the user wants to see details about the loans, ask what they want to do      
    elif user_input == 'c':
        #Using another while loop to keep showing the manual for books until the user enter a valid number.
        while True:
            try:
                #Convert the input into a integer, which allows try and except statement to catch any input that is not an integer
                user_input_for_loans = int(input(
"""
What would you like to do?
1. Print all loans 
2. Sort recent loans
3. Add loan
4. Check a borrower's loans
5. Add return date
6. Go back to the main manual\n"""))
                #Call different functions when different numbers are entered
                if user_input_for_loans == 1:
                    print_all_loans()
                elif user_input_for_loans == 2:
                    print_all_loans_sort_by_columns()
                elif user_input_for_loans == 3:
                    add_loans()
                elif user_input_for_loans == 4:
                    show_a_persons_loans()
                elif user_input_for_loans == 5:
                    add_return_date()
                elif user_input_for_loans == 6 :
                    break
                #catches all the numbers out of range
                else:
                    print('That is not an option.\n')
            except:
                #when the input doesn't meet any of the conditions above, print that is not an option.
                print('That is not an option.\n')

    elif user_input == 'd':
        break
    else:
        print('That is not an option, please enter again.')


