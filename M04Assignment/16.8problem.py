'''
import csv
import sqlite3
import sqlalchemy
'''
# Define the data
#text = '''author,book
#    J R R Tolkien,The Hobbit
#    Cormac Mccarthy,"Blood Meridian"
# '''
'''
with open('test.csv', 'wt') as outfile:
     outfile.write(text)

with open('books.csv', 'rt') as infile:
     books = csv.DictReader(infile)
     for book in books:
         print(book)

{'book': 'The Hobbit', 'author': 'J R R Tolkien'}
{'book': 'Blood Meridian', 'author': 'Cormac Mccarthy'}

'''
#text = '''title,author,year
#    The Weirdstone of Brisingamen,Alan Garner,1960
#    Perdido Street Station,China Miéville,2000#
#    Thud!,Terry Pratchett,2005
#    The Spellman Files,Lisa Lutz,2007
#    Small Gods,Terry Pratchett,1992
#    '''
'''
with open('books2.csv', 'wt') as outfile:
     outfile.write(text)


db = sqlite3.connect("books2.db")
curs = db.cursor()
ins_str = 'insert into book values(title, author, year)'
with open('books.csv', 'rt') as infile:
     books = csv.DictReader(infile)
     for book in books:
       curs.execute(ins_str, (book['title'], book['author'], book['year']))'''
'''
<sqlite3.Cursor object at 0x1007b21f0>
<sqlite3.Cursor object at 0x1007b21f0>
<sqlite3.Cursor object at 0x1007b21f0>
<sqlite3.Cursor object at 0x1007b21f0>
<sqlite3.Cursor object at 0x1007b21f0>'''
'''db.commit()


sql = 'select title from book order by title asc'
for row in db.execute(sql):
     print(row)

('Perdido Street Station',)
('Small Gods',)
('The Spellman Files',)
('The Weirdstone of Brisingamen',)
('Thud!',)


for row in db.execute('select * from book order by year'):
    print(*row, sep = ",")

('The Weirdstone of Brisingamen', 'Alan Garner', 1960)
('Small Gods', 'Terry Pratchett', 1992)
('Perdido Street Station', 'China Miéville', 2000)
('Thud!', 'Terry Pratchett', 2005)
('The Spellman Files', 'Lisa Lutz', 2007)


conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
     print(row)

('Perdido Street Station',)
('Small Gods',)
('The Spellman Files',)
('The Weirdstone of Brisingamen',)
('Thud!',)'''