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
    self.db.commit()

  def fetch_all_data(self, query, data=None):
    self.cursor.execute(query, data)
    return self.cursor.fetchall()
  
  def close(self):
    self.cursor.close()
    self.db.close()

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

  @staticmethod # Is the method belong to the class but not depend on instance. Can not modify class state or instance state. Dont need to access to instances attribute. Call directly from class
  def remove_book(db, book_id):
    query='DELETE from books WHERE book_id = %s'
    db.execute(query, (book_id,))

  @staticmethod
  def update_book(db, book_id, title=None, author=None, genre=None):
    query='UPDATE books SET title=%s, author=%s, genre=%s WHERE book_id=%s'
    db.execute(query, (title, author, genre, book_id))

  @staticmethod
  def check_availability(db, book_id):
    query='SELECT availability FROM books WHERE book_id=%s'
    result = db.fetch_all_data(query, (book_id,))
    return result
  

# Member Class 
class Member:
  def __init__(self, name, email, phone) -> None:
    self.name = name
    self.email = email
    self.phone = phone 

  def add_member(self, db):
    query = 'INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)'
    db.execute(query, (self.name, self.email, self.phone))

  @staticmethod # Is the method belong to the class but not depend on instance. Can not modify class state or instance state. Dont need to access to instances attribute. Call directly from class
  def remove_member(db, member_id):
    query = 'DELETE FROM members WHERE member_id=%s'
    db.execute(query, (member_id,))

  @staticmethod
  def update_member(db, member_id, name=None, email=None, phone=None):
    query='UPDATE members SET name=%s, email=%s, phone=%s WHERE member_id=%s'
    db.execute(query, (name, email, phone, member_id))

    

db = Database()

# Adding a new book
new_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
new_book.add_book(db)

# Adding a new member
new_member = Member("John Doe", "johndoe@example.com", "123-456-7890")
new_member.update_member(db, 1, 'Tim', 'tim@gmail.com','5713318824')


