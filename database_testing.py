import sqlite3

# Connect to the database
connect = sqlite3.connect('customer.db')

# Create cursor
cursor = connect.cursor()

# Create a table
# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email_address text
#     )""")

# cursor.execute("INSERT INTO customers VALUES ('Peter','Parker','spiderman@email.com')")

# customer_list = [
#                     ('John','Smith','js@a.com'),
#                     ('John','Cena','jc@a.com'),
#                     ('Al','Smith','as@a.com'),
#                 ]
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", customer_list)

# Update records
# cursor.execute("""UPDATE customers SET first_name = 'Steve'
#                   WHERE rowid = '4'
#         """)

# Delete records
# cursor.execute("DELETE FROM customers WHERE rowid = 6")


# Query the database - ORDER BY
cursor.execute('SELECT rowid, * FROM customers ORDER BY last_name')
# cursor.execute('SELECT * FROM customers WHERE email_address LIKE "%@a.com"')
for data in cursor.fetchall():
    print(data)

# Commit the changes
connect.commit()

# Close the connection
connect.close()