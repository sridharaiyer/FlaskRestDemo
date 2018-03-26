import sqlite3

connection = sqlite3.connect('data.db')

cursur = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'
cursur.execute(create_table)

user = (1, 'Bob', 'Password1')
insert_query = 'INSERT INTO users VALUES (?,?,?)'

cursur.execute(insert_query, user)


users = [
    (2, 'Susan', 'Password1'),
    (3, 'Charles', 'Password1')]

cursur.executemany(insert_query, users)

select_query = 'SELECT * FROm users'

for row in cursur.execute(select_query):
    print(row)

connection.commit()
connection.close()
