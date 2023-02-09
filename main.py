import sys
import requests
import secrets
from requests.auth import HTTPBasicAuth
import json
import sqlite3
from typing import Tuple


"""This function serves the purpose of the GET request to the wufoo form, using the secrets key to retrieve the 
form submissions. Runs through a if statement for a status code if any errors occur."""
def get_wufoo_data() -> list[dict]:  # comment to test workflow
    url = "https://mkurciviez.wufoo.com/api/v3/forms/cubess-project-proposal-submission/entries/json"
    # url = "https://jsantore.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(secrets.wufoo_key, 'pass'))
    # print(response.text)

    if response.status_code != 200:
        print(f"Data retrieval failed, response code: {response.status_code} with the error message: {response.reason}")
        sys.exit(-1)
    json_response = response.json()
    return json_response['Entries']


"""Function will write data to a file, uses the json library to 'pretty print' the outputted data."""
# def write_data_to_file():
#     with open("wufoo_data.txt", "w") as outfile:
#         text = ["Marcus Kurciviez \n", "Wufoo Form Data \n"]
#        outfile.writelines(text)
#        json.dump(get_wufoo_data(), outfile, indent=3, sort_keys=True)

# def read_data():
#     f = open("wufoo_data.txt", "r")
#     print(f.readline())

def open_db(filename:str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor

def close_db(connection:sqlite3.Connection):
    connection.commit()
    connection.close()

def create_wufoo_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufootest(
    EntryID integer primary key,
    Prefix text,
    First_Name text,
    Last_Name text,
    Title text,
    Organization_Name text,
    Email text,
    Organization_Website text,
    Phone_Number text,
    Course_Project text,
    Guest_Speaker text,
    Site_Visit text,
    Job_Shadow text,
    Internships text,
    Career_Panel text,
    Networking_Event text,
    Summer_2022 text,
    Fall_2022 text,
    Spring_2023 text,
    Summer_2023 text,
    Other text,
    Permission_to_share text
    CreatedBy text,
    DateUpdated text,
    DateCreated text''')

def create_table(db_cursor: sqlite3.Cursor):
    create_wufoo_table(db_cursor)

def put_wufoo_data_in(table: str, data_to_add: list[tuple], db_cursor: sqlite3.Cursor):
    db_cursor.executemany(f"""INSERT INTO {table}(EntryId, Prefix, First_Name, Last_Name, Title, Organization_Name, Email, Organization_Website, Phone_Number,
    Course_Project, Guest_Speaker, Site_Visit, Job_Shadow, Internships, Career_Panel, Networking_Event, Summer_2022, Fall_2022, Spring_2023, Summer_2023, Other,
    Permission_to_share, CreatedBy, DateUpdated, DateCreated)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data_to_add)


# def main():
#     conn, cursor = open_db("test_db.sqlite")
#     print(type(conn))
#     close_db(conn)

def write_wufoo_data():
    conn = sqlite3.connect('wufoo.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS wufoo_data
            (
            EntryID integer primary key,
            Prefix text,
            First_Name text,
            Last_Name text,
            Title text,
            Organization_Name text,
            Email text,
            Organization_Website text,
            Phone_Number text,
            Course_Project text,
            Guest_Speaker text,
            Site_Visit text,
            Job_Shadow text,
            Internships text,
            Career_Panel text,
            Networking_Event text,
            Summer_2022 text,
            Fall_2022 text,
            Spring_2023 text,
            Summer_2023 text,
            Other text,
            Permission_to_share text
            CreatedBy text,
            DateUpdated text,
            DateCreated text
            );''')
    get_data = get_wufoo_data()

    for item in get_data:
        cur.execute("INSERT INTO wufoo_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (item['EntryId'],
                     item.get('Field1', ''), #Prefix
                     item.get('Field4', ''), #FirstName
                     item.get('Field5', ''), #LastName
                     item.get('Field7', ''), #Title
                     item.get('Field8', ''), #OrgName
                     item.get('Field9', ''), #Email
                     item.get('Field10', ''), #OrgWeb
                     item.get('Field11', ''), #Phone
                     item.get('Field13', ''), #CourseProj
                     item.get('Field14', ''), #GuestSpeaker
                     item.get('Field15', ''), #SiteVisit
                     item.get('Field16', ''), #JobShadow
                     item.get('Field17', ''), #Internships
                     item.get('Field18', ''), #CareerPanel
                     item.get('Field19', ''), #NetworkingEve
                     item.get('Field113', ''), #Summer2022
                     item.get('Field114', ''), #Fall2022
                     item.get('Field115', ''), #Spring2023
                     item.get('Field116', ''), #Summer2023
                     item.get('Field117', ''), #Other
                     item.get('Field213', ''), #Permission
                     item.get('CreatedBy', ''),
                     item.get('DateUpdated', '')))


    conn.commit()
    conn.close()
if __name__ == '__main__':
    write_wufoo_data()
    # get_wufoo_data()
    # read_data()
