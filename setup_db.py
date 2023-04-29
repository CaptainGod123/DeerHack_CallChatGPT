import sqlite3

def setup_db():
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()

  # Create user table
  cursor.execute('''CREATE TABLE users
                  (phone_number TEXT PRIMARY KEY,
                    password TEXT,
                    conversation TEXT)''')

  conn.commit()
  conn.close()
