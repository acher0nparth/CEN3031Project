# https://levelup.gitconnected.com/build-a-note-taking-app-with-mysql-backend-in-python-927b4c5fad91
# https://realpython.com/python-mysql/
# tutorials cited for following on how to setup a mysql server

import mysql.connector as conn
from getpass import getpass
from mysql.connector import connect, Error


# create connection object that will be used to communicate with mySQL server running on this port
global connection
connection = conn.connect(host="localhost", port=3306, user="root", password="flashify")


def db_create_db(connection):
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS testing_db")
    print(connection)
    connection.database = "testing_db"
    print(connection)
    return connection.database


def db_create_table(connection):
    mycursor = connection.cursor()
    query = (
        "CREATE TABLE IF NOT EXISTS notes_tb ("
        "note_id INT AUTO_INCREMENT PRIMARY KEY, "
        "title VARCHAR(255) NOT NULL, "
        "note VARCHAR(10000) NOT NULL)"
    )
    mycursor.execute(query)
    connection.commit()


def db_insert(connection, title, note):
    mycursor = connection.cursor()
    query = "INSERT into notes_tb (title, note) VALUES (%s, %s)"
    mycursor.execute(query, (title, note))
    connection.commit()


def db_get_all_notes(connection):
    query = "SELECT * from notes_tb"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_titles(connection):
    query = "SELECT title from notes_tb"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_note(connection, note_id):
    mycursor = connection.cursor()
    mycursor.execute("SELECT title, note FROM notes_tb WHERE note_id = " + str(note_id))
    return mycursor.fetchone()


def db_get_note_t(connection, title):
    mycursor = connection.cursor()
    mycursor.execute("SELECT note FROM notes_tb WHERE title = '" + title + "'")
    return mycursor.fetchone()


def db_update_note(connection, title, note, note_id):
    mycursor = connection.cursor()
    query = "UPDATE notes_tb SET title = %s, note = %s WHERE note_id = %s"
    val = (title, note, note_id)
    mycursor.execute(query, val)
    connection.commit()


def db_delete_note(connection, note_id):
    mycursor = connection.cursor()
    query = "DELETE FROM notes_tb WHERE note_id = %s"
    adr = (note_id,)
    mycursor.execute(query, adr)
    connection.commit()


# note_ex = [("Note1 title", "testing note 1"), ("Note2 title", "testing note 2")]

# db_create_db(connection)
# db_create_table(connection)

# for note in note_ex:
#     db_insert(connection, note[0], note[1])

# notes_ret = db_get_all_notes(connection)
# for note in notes_ret:
#     print(note)

# one_note = db_get_note(connection, 3)
# print(one_note)

# db_update_note(connection, "Note 1 updated", "testing updating my first note", "3")
# one_note = db_get_note(connection, 3)
# print(one_note)

# db_delete_note(connection, 1)
# db_delete_note(connection, 2)

# notes_ret = db_get_all_notes(connection)
# for note in notes_ret:
#     print(note)


# for x in range(60):
#     db_delete_note(connection, x)
# try:
#     with connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="flashify",
#     ) as connection:
#         create_db_query = "CREATE DATABASE test2_db"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
# except Error as e:
#     print(e)


# try:
#     with connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="flashify",
#         database="test1_db",
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)

# print(connection.cursor())
# show_db_query = "SHOW DATABASES"
# with connection.cursor() as cursor:
#    cursor.execute(show_db_query)
#    for db in cursor:
#         print(db)
