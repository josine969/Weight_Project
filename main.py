# Import SQLITE module
import sqlite3
# Connect to Database
conn = sqlite3.connect('weight.db')
# Create a cursor to move in database
curs = conn.cursor()

# Select and save today date
from datetime import date
today = date.today()
print("Today's date:", today)

# Ask for the data

print("How time do you use for the 5km daily run?")
time = input()

print("How do you feel?")
feeling = input()

print("Day", today, "Time", time, "Feeling", feeling)

# Add value
curs.execute("INSERT INTO run VALUES (?, ?, ?)", (today, time, feeling))

conn.commit()
conn.close()
