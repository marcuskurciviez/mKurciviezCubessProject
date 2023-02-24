import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(
        filename
    )  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
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
    Other TEXT
    Permission_to_Share TEXT,
    dateCreated TEXT);"""


    cursor.execute(create_statement)


def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insertStatement = """INSERT OR IGNORE INTO WuFooData (EntryID, Prefix, First_Name, Last_Name, Title, Org, Email, OrgWebsite,
    Phone, Course_Project, Guest_Speaker, Site_Visit, Job_Shadow, Internship, Career_Panel, Networking_Event, Summer_2022, Fall_2022, Spring_2023, Summer_2023,
    Other, Permission_to_Share, dateCreated) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(
            entry_values[0]
        )  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:-3]
        cursor.execute(insertStatement, entry_values)
