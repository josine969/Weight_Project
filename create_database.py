# Import SQLITE module
import sqlite3
# Connect to Database
conn = sqlite3.connect('weight.db')
# Create a cursor to move in database
curs = conn.cursor()

# Create a table
curs.execute('create table profile (Date, Kg, Thigh, Waist, Arm, Chest)')
curs.execute('create table run (Date, Time , Feeling)')

# Add value
#curs.execute("insert into run values ('05/06', 34.20, 'Not bad')")

# Añado muchos valores
#values = [('05/06', 40.20, 'Good'), ('06/06', 42.22, 'Correct'), ('07/07', 50.21, 'Bad'), ('08/08', 50.60, 'The Worst day ever')]
#curs.executemany('insert into Liga_Verano values(?,?,?)', values)

# Commit to save the changes and close the connection
conn.commit()
conn.close()