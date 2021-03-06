# https://levelup.gitconnected.com/build-a-note-taking-app-with-mysql-backend-in-python-927b4c5fad91
# https://realpython.com/python-mysql/
# tutorials cited for following on how to setup a mysql server

import mysql.connector as conn
from getpass import getpass
from mysql.connector import connect, Error


# create connection object that will be used to communicate with mySQL server running on this port
global connection
connection = conn.connect(host="localhost", port=3306, user="root", password="flashify")


def db_create_db():
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS pres_db")
    print(connection)
    connection.database = "pres_db"
    print(connection)
    return connection.database


def db_create_table():
    mycursor = connection.cursor()
    query = (
        "CREATE TABLE IF NOT EXISTS notes_tb ("
        "title VARCHAR(255) NOT NULL, "
        "course VARCHAR(255) NOT NULL,"
        "note VARCHAR(10000) NOT NULL)"
    )
    mycursor.execute(query)
    connection.commit()


def db_create_notecard_table():
    mycursor = connection.cursor()
    query = (
        "CREATE TABLE IF NOT EXISTS notecards_tb ("
        "course VARCHAR(255) NOT NULL,"
        "prompt VARCHAR(1000) NOT NULL,"
        "answer VARCHAR(1000) NOT NULL)"
    )
    mycursor.execute(query)
    connection.commit()


def db_insert(title, course, note):
    mycursor = connection.cursor()
    query = "INSERT into notes_tb (title, course, note) VALUES (%s, %s, %s)"
    mycursor.execute(query, (title, course, note))
    connection.commit()


def db_insert_notecards(course, prompt, answer):
    mycursor = connection.cursor()
    query = "INSERT into notecards_tb (course, prompt, answer) VALUES (%s, %s, %s)"
    mycursor.execute(query, (course, prompt, answer))
    connection.commit()


def db_get_all_notes():
    query = "SELECT * from notes_tb"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_course_note_titles(course):
    query = "SELECT title FROM notes_tb WHERE course = '" + course + "'"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_course_notecards(course):
    query = "SELECT prompt, answer FROM notecards_tb WHERE course = '" + course + "'"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_course_notecards_ans(course):
    query = "SELECT answer FROM notecards_tb WHERE course = '" + course + "'"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_titles():
    query = "SELECT title from notes_tb"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_all_courses():
    query = "SELECT course from notes_tb"
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_get_note(title, course):
    query = "SELECT note FROM notes_tb WHERE title = %s AND course = %s"
    mycursor = connection.cursor()
    val = (title, course)
    mycursor.execute(query, val)
    return mycursor.fetchone()[0]


def db_get_notecard(course, answer):
    query = "SELECT prompt FROM notecards_tb WHERE course = %s AND answer = %s"
    mycursor = connection.cursor()
    val = (course, answer)
    mycursor.execute(query, val)
    return mycursor.fetchone()[0]


def db_update_note(title, course, note):
    mycursor = connection.cursor()
    query = "UPDATE notes_tb SET note = %s WHERE title = %s AND course = %s"
    val = (note, title, course)
    mycursor.execute(query, val)
    connection.commit()


def db_delete_note(title, course):
    mycursor = connection.cursor()
    query = "DELETE FROM notes_tb WHERE title = %s AND course = %s"
    adr = (title, course)
    mycursor.execute(query, adr)
    connection.commit()


def db_delete_notecard(course, answer):
    mycursor = connection.cursor()
    query = "DELETE FROM notecards_tb WHERE answer = %s AND course = %s"
    adr = (answer, course)
    mycursor.execute(query, adr)
    connection.commit()


def db_delete_course_notes(course):
    mycursor = connection.cursor()
    query = "DELETE FROM notes_tb WHERE course = '" + course + "'"
    mycursor.execute(query)
    connection.commit()


def db_delete_course_notecards(course):
    mycursor = connection.cursor()
    query = "DELETE FROM notecards_tb WHERE course = '" + course + "'"
    mycursor.execute(query)
    connection.commit()
