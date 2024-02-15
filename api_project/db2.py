import sqlite3

conn= sqlite3.connect("empdatabase.db")

print("Opened the db successfully")

conn.execute("CREATE TABLE emp(id INTEGER PRIMARY KEY, name TEXT, addr TEXT,city TEXT, salary TEXT)")

print("Table created")

conn.close()