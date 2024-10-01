import mysql.connector
from datetime import date 
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection 
class Database:
  def __init__(self) -> None:
    self.db = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host='localhost', database='library')
    self.cursor = self.db.cursor()

  def execute(self, query, data=None):
    self.cursor.execute(query, data)
    self.cursor.commit()

  def fetch_all_data(self, query, data=None):
    self.cursor.execute(query, data)
    return self.cursor.fetchall()
  
  def close(self):
    self.cursor.close()
    self.db.close

db = Database()

# Book Class 
class Book:
  def __init__(self, title, author, genre) -> None:
    self.title = title
    self.author = author
    self.genere = genre

  def add_book(self, db):
    query = 'INSERT INTO books (title, author, genre) VALUES(%s, %s, %s)'
    db.execute(query, (self.title, self.author, self.genere))

  @staticmethod # Static method don't have self at the first arg . Mean this method will not run the insances itself as the first arg. (It is like isolated function)
  def remove_book(db, book_id):
    query='DELETE from books WHERE book_id = %s'
    db.execute(query, (book_id))

  @staticmethod
  def update_book(db, book_id, title=None, author=None, genre=None):
    query='UPDATE books SET title=%s, author=%s, genre=%s WHERE book_id=%s'
    db.execute(query, (title, author, genre, book_id))

  @staticmethod
  def check_availability(db, book_id):
    query='SELECT availability FROM books WHERE book_id=%s'
    result = db.fetch_all_data(query, (book_id))
    return result
    


