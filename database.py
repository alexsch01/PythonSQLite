import sqlite3

# Query the database and print the records
def show_database():
    connect = sqlite3.connect('customer.db')
    cursor = connect.cursor()
    cursor.execute('SELECT rowid, * FROM customers')
    for data in cursor.fetchall():
        print(data)
    connect.close()

# Add a new record to the table
def add_record(fname, lname, email):
    connect = sqlite3.connect('customer.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO customers VALUES (?,?,?)",(fname,lname,email))
    connect.commit()
    connect.close()

# Add many records to the table
def add_many(list):
    connect = sqlite3.connect('customer.db')
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
    connect.commit()
    connect.close()

# Delete a record from the table
def delete_record(rowid):
    connect = sqlite3.connect('customer.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM customers WHERE rowid = ?",rowid)
    connect.commit()
    connect.close()

def name_lookup(fname, lname):
    connect = sqlite3.connect('customer.db')
    cursor = connect.cursor()
    cursor.execute('SELECT rowid, * FROM customers WHERE first_name = ? AND last_name = ?',(fname,lname))
    for data in cursor.fetchall():
        print(data)
    connect.close()
