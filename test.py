'''Mercy Song -- Library catalog database application.'''
import sqlite3

#Storing the database to a variable
DATABASE = 'Library_Catalog.db'

#Connecting python to my database
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
