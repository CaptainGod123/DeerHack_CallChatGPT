import datetime
import sqlite3
import os

from flask import jsonify
from setup_db import setup_db

def check_and_setup_db():
  # set up the db file if it dne
  if not os.path.isfile('mydatabase.db'):
    setup_db()

def check_new_user(phone_number):
    # fetch all user records
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # confirm if the number already exists
    db_phone_numbers = []
    for row in rows:
        number = row[0]
        db_phone_numbers += [number]
    print(db_phone_numbers)
    conn.close()
    if (phone_number not in db_phone_numbers):
        return 1
    else:
        return 0

def add_user(phone_number, password):
  # fetch all user records
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM users')
  rows = cursor.fetchall()

  # confirm if the number already exists
  db_phone_numbers = []
  for row in rows:
    number = row[0]
    db_phone_numbers += [number]

  if (phone_number not in db_phone_numbers):
    # Insert new user
    cursor.execute("INSERT INTO users (phone_number, password, conversation) VALUES (?, ?, ?)", (phone_number, password, ''))
    conn.commit()

  conn.close()

  return 'User added successfully'

def add_message(phone_number, message, isGPT=False):

    # Connect to database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Update conversation field for user with phone number
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    message_by = 'GPT' if isGPT else 'user'

    cursor.execute(
      "UPDATE users SET conversation = conversation || ? WHERE phone_number = ?",
      (f"{date} :-: {message_by} :-: {message} :::", phone_number)
    )

    conn.commit()
    conn.close()

    # Return success message
    return jsonify({'message': f"Added message '{message}' to user with phone number {phone_number}"})
