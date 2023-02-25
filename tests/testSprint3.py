import sqlite3
import tkinter as tk

import main


def test_get_data():
    conn = sqlite3.connect(main.db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO WuFooData (First_Name, Last_Name) VALUES ('John', 'Doe')")
    cursor.execute("INSERT INTO WuFooData (First_Name, Last_Name) VALUES ('Jane', 'Doe')")
    conn.commit()
    conn.close()

    expected_data = [('John', 'Doe'), ('Jane', 'Doe')]
    assert main.get_data() == expected_data


def test_display_data():
    root = tk.Tk()
    main.root = root
    main.db_name = "test.sqlite"
    conn = sqlite3.connect(main.db_name)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE WuFooData
                      (EntryID INTEGER PRIMARY KEY,
                       Prefix TEXT,
                       First_Name TEXT,
                       Last_Name TEXT,
                       Title TEXT,
                       Org TEXT,
                       Email TEXT,
                       OrgWebsite TEXT,
                       Phone TEXT,
                       Course_Project INTEGER,
                       Guest_Speaker INTEGER,
                       Site_Visit INTEGER,
                       Job_Shadow INTEGER,
                       Internship INTEGER,
                       Career_Panel INTEGER,
                       Networking_Event INTEGER,
                       Summer_2022 INTEGER,
                       Fall_2022 INTEGER,
                       Spring_2023 INTEGER,
                       Summer_2023 INTEGER,
                       Other TEXT,
                       Permission_to_Share INTEGER,
                       dateCreated TEXT)""")
    cursor.execute("""INSERT INTO WuFooData VALUES
                      (1, 'Mr.', 'John', 'Doe', 'Engineer', 'ACME Inc.', 'johndoe@example.com',
                       'https://www.acme.com', '555-1234', 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, '', 1, '2022-01-01')""")
    cursor.execute("""INSERT INTO WuFooData VALUES
                      (2, 'Ms.', 'Jane', 'Doe', 'Manager', 'XYZ Corp.', 'janedoe@example.com',
                       'https://www.xyzcorp.com', '555-5678', 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, '', 1, '2022-01-02')""")
    conn.commit()
    conn.close()
    main.display_data(None)
    assert main.data_label.cget("text") == (
        "EntryID: 1\nPrefix: Mr.\nFirst_Name: John\nLast_Name: Doe\nTitle: Engineer\nOrg: ACME Inc.\nEmail: johndoe@example.com\nOrgWebsite: https://www.acme.com\nPhone: 555-1234\nCourse_Project: 1\nGuest_Speaker: 1\nSite_Visit: 0\nJob_Shadow: 0\nInternship: 0\nCareer_Panel: 1\nNetworking_Event: 0\nSummer_2022: 1\nFall_2022: 0\nSpring_2023: 1\nSummer_2023: 0\nOther:\nPermission_to_Share: 1\ndateCreated: 2022-01-01")
