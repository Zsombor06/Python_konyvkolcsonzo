import sqlite3

con = sqlite3.connect("konyvtar.db")
cur = con.cursor()

# Az adatbázis létrehozása
cur.execute("CREATE TABLE IF NOT EXISTS author (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(50))")
cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, title VARCHAR(50) NOT NULL, category VARCHAR(50) NOT NULL, author_id INT NOT NULL, FOREIGN KEY(author_id) REFERENCES author(id))")
cur.execute("CREATE TABLE IF NOT EXISTS rent (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, book_id INT NOT NULL, start_date TEXT NOT NULL, end_date TEXT, FOREIGN KEY(book_id) REFERENCES book(id))")

# # Adatok beadása
# def populate():
#     # A szerzők feltöltése adatokkal
#     cur.execute("INSERT INTO author (name) VALUES ('Drew Karpyshyn')")
#     cur.execute("INSERT INTO author (name) VALUES ('J. R. R. Tolkien')")
#     cur.execute("INSERT INTO author (name) VALUES ('Petőfi Sándor')")
#     con.commit()

#     # A könyvek feltöltése adatokkal
#     cur.execute("INSERT INTO book (title, category, author_id) VALUES ('A Gyűrűk Ura', 'fantasy', 1)")
#     cur.execute("INSERT INTO book (title, category, author_id) VALUES ('Star Wars: The Old Republic - Revan', 'sci-fi', 2)  ")
#     cur.execute("INSERT INTO book (title, category, author_id) VALUES ('János vitéz', 'mese', 3)")
#     con.commit()
# populate() # első futtatás után kommenteld ki

# Az adatmodelleket tartalmazó classok

class Author:
    def __init__(self, args):
        self.id = args[0]
        self.name = args[1]

class Book:
    def __init__(self, args):
        self.id = args[0]
        self.title = args[1]
        self.category = args[2]
        self.author_id = args[3]

class Rent:
    def __init__(self, args):
        self.id = args[0]
        self.book_id = args[1]
        self.start_date = args[2]
        self.end_date = args[3]

# Visszaadja egy author class elemekkel rendelkező listában az összes szerzőt
def getAuthors():
    authors = []
    res = con.execute("SELECT * FROM author")
    for author in res.fetchall():
        authors.append(Author(author))
    return authors

# Visszaadja egy book class elemekkel rendelkező listában az összes könyvet
def getBooks():
    books = []
    res = con.execute("SELECT * FROM book")
    for book in res.fetchall():
        books.append(Book(book))
    return books

# Visszaadja egy rent class elemekkel rendelkező listában az összes bérlést
def getRents():
    rents = []
    res = con.execute("SELECT * FROM rent")
    for rent in res.fetchall():
        rents.append(Rent(rent))
    return rents

# Visszaadja egy author class elemekkel rendelkező listában a paraméterként megadott névre hasonlító nevű szerzőket
def getAuthorsByName(name):
    authors = []
    res = con.execute(f"SELECT * FROM author WHERE name LIKE '%{name}%'") 
    for author in res.fetchall():
        authors.append(Author(author))
    return authors

def getAuthorsByID(id):
    authors = []
    res = con.execute(f"SELECT * FROM author WHERE id LIKE '%{id}%'") 
    for author in res.fetchall():
        authors.append(Author(author))
    return authors

# Visszaadja azon könyvek listáját, amit a paraméterként megadott névre hasonlító nevű szerző írt
def getBooksByAuthor(name):
    books = []
    res = con.execute(f"SELECT * FROM book INNER JOIN author ON book.author_id = author.id WHERE author.name LIKE '%{name}%'") 
    for book in res.fetchall():
        books.append(Book(book))
    return books

# Visszaadja azon könyvek listáját, amik a paraméterként átvett kategóriába tartoznak
def getBooksByCategory(category):
    books = []
    res = con.execute(f"SELECT * FROM book WHERE category = '{category}'")
    for book in res.fetchall():
        books.append(Book(book))
    return books

# Visszaadja azon könyvek listáját, amik a paraméterként átvett címre hasonlító címmel rendelkeznek
def getBooksByTitle(title):
    books = []
    res = con.execute(f"SELECT * FROM book INNER JOIN author ON book.author_id = author.id  WHERE title LIKE '%{title}%'")
    for book in res.fetchall():
        books.append(Book(book))
    return books

# Visszadja az összes létező kategóriát egy stringeket tartalmazó listában
def getCategories():
    categories = []
    res = con.execute("SELECT DISTINCT category FROM book")
    for category in res.fetchall():
        categories.append(category[0])
    return categories

# Létrehoz egy bérlési időszakot a paraméterben átadott könyv id-hoz
def startRent(book_id):
    con.execute(f"INSERT INTO rent (book_id, start_date, end_date) VALUES ({book_id}, date(), NULL)")
    con.commit()

# Lezár egy bérlési időszakot a megadott rent_id-val
def endRent(rent_id):
    con.execute(f"UPDATE rent SET end_date = date() WHERE id = {rent_id}")
    con.commit()

# Visszadja a jelenleg aktív bérléseket tartalmazó listát
def getActiveRents():
    rents = []
    res = con.execute("SELECT * FROM rent WHERE end_date IS NULL")
    for rent in res.fetchall():
        rents.append(Rent(rent))
    return rents
def getBookOfRent(rent):
    res=con.execute(f"SELECT * FROM book inner join rent on book.id=rent.book_id WHERE rent.id={rent.id}")
    return Book(res.fetchone())