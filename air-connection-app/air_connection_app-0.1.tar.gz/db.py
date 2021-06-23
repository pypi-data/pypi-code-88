import sqlite3

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# Create db
# |id|source|destination|flight_company|flight_number|flight_time|free_seats|price|
sql_query = """ CREATE TABLE flight (
    id integer PRIMARY KEY,
    source text NOT NULL,
    destination text NOT NULL,
    Flight_company text NOT NULL,
    flight_number text NOT NULL,
    flight_time text NOT NULL,
    free_seats text NOT NULL,
    price text NOT NULL
)"""
cursor.execute(sql_query)


# Load data from file
with open('list.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO flight VALUES (?,?,?,?,?,?,?,?)", row.split(","))
        conn.commit()
        no_records += 1
conn.close()
print('\n{} Record Transferred'.format(no_records))
