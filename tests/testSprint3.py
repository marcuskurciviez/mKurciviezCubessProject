import database
import getWufooData
from database import open_db, close_db
import tkinter as tk
import sqlite3
from database import open_db, close_db
import database
import getWufooData
import wufooGUI
from main import db_name

conn, cursor = open_db(db_name)
database.create_entries_table(cursor)
database.add_entries_to_db(cursor, entries_list)
close_db(conn)


def test_db_has_data():
    json_response = getWufooData.get_wufoo_data()
    entries_list = json_response["Entries"]
    connection, cursor = database.open_db("cubesProject.sqlite.db")
    database.add_entries_to_db(cursor, entries_list)
    cursor.execute("SELECT COUNT(*) FROM SQLITE_MASTER WHERE name = ?", ["WuFooData"])
    count = cursor.fetchone()[0]
    database.close_db(connection)
    assert count > 0, "There is no data in the table"


def test_gui_displays_firstname_data():
    db_name = "cubesProject.sqlite"
    conn, cursor = open_db(db_name)
    cursor.execute("SELECT First_Name FROM WuFooData LIMIT 1")
    first_name_db = cursor.fetchone()[0]
    close_db(conn)

    root = tk.Tk()
    name_listbox = tk.Listbox(root, width=25, height=25, font=("Courier", 20))
    names = []
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT First_Name FROM WuFooData")
    rows = cursor.fetchall()
    for name in rows:
        names.append(name[0])
        name_listbox.insert(tk.END, name[0])
    name_listbox.pack(side=tk.LEFT)
    first_name_gui = name_listbox.get(0)
    root.destroy()

    assert first_name_gui == first_name_db


def test_gui_displays_lastname_data():
    db_name = "cubesProject.sqlite"
    conn, cursor = open_db(db_name)
    cursor.execute("SELECT Last_Name FROM WuFooData LIMIT 1")
    last_name_db = cursor.fetchone()[0]
    close_db(conn)

    root = tk.Tk()
    name_listbox = tk.Listbox(root, width=25, height=25, font=("Courier", 20))
    names = []
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT Last_Name FROM WuFooData")
    rows = cursor.fetchall()
    for name in rows:
        names.append(name[0])
        name_listbox.insert(tk.END, name[0])
    name_listbox.pack(side=tk.LEFT)
    last_name_gui = name_listbox.get(0)
    root.destroy()
