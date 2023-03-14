import sqlite3
from typing import Tuple

from getWufooData import get_wufoo_data


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(
        filename
    )  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # save changes
    connection.close()


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS WuFooData(
    EntryID INTEGER PRIMARY KEY,
    Prefix TEXT NOT NULL,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Title TEXT,
    Org TEXT,
    Email TEXT,
    OrgWebsite TEXT,
    Phone TEXT,
    Course_Project BOOLEAN,
    Guest_Speaker BOOLEAN,
    Site_Visit BOOLEAN,
    Job_Shadow BOOLEAN,
    Internship BOOLEAN,
    Career_Panel BOOLEAN,
    Networking_Event BOOLEAN,
    Summer_2022 BOOLEAN,
    Fall_2022 BOOLEAN,
    Spring_2023 BOOLEAN,
    Summer_2023 BOOLEAN,
    Other TEXT,
    Permission_to_Share TEXT,
    dateCreated TEXT);"""

    cursor.execute(create_statement)

    # Create a new table called "users"
    create_users_table_statement = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    bsu_email TEXT NOT NULL,
    department TEXT);"""
    cursor.execute(create_users_table_statement)

def update_entries_table(cursor: sqlite3.Cursor):
    entries_data = get_wufoo_data()["Entries"]
    add_entries_to_db(cursor, entries_data)

def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    insertStatement = """INSERT OR IGNORE INTO WuFooData (EntryID, Prefix, First_Name, Last_Name, Title, Org, Email, OrgWebsite,
    Phone, Course_Project, Guest_Speaker, Site_Visit, Job_Shadow, Internship, Career_Panel, Networking_Event, Summer_2022, Fall_2022, Spring_2023, Summer_2023,
    Other, Permission_to_Share, dateCreated) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(entry_values[0])  # convert the first value to an integer
        entry_values = entry_values[:-3]
        cursor.execute(insertStatement, entry_values)
