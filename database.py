import sqlite3


connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # Cursors will return sqlite3.Row objects, which allow using keys (content, date).


def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")


def close_connection():
    connection.close()


def add_entry(content, date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?, ?);", (content, date))  # Avoids SQL Injection


def get_entries():
    return connection.execute("SELECT * FROM entries;")
