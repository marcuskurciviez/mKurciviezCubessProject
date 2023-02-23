import tkinter as tk
from database import open_db, close_db
import database

db_name = "cubes_Project.sqlite"

# Create the GUI window
window = tk.Tk()
window.title("Wufoo Data")

# Create the table to display the data
table = tk.Frame(window)
table.pack()

# Add the column labels to the table
labels = ["EntryID", "Prefix", "First_Name", "Last_Name", "Title", "Org", "Email", "OrgWebsite",
          "Phone", "Course_Project", "Guest_Speaker", "Site_Visit", "Job_Shadow", "Internship", "Career_Panel",
          "Networking_Event", "Summer_2022", "Fall_2022", "Spring_2023", "Summer_2023", "Other", "Permission_to_Share",
          "dateCreated"]
for i, label in enumerate(labels):
    tk.Label(table, text=label).grid(row=0, column=i, padx=5, pady=5)

# Get the data from the database and add it to the table
conn, cursor = open_db(db_name)
rows = cursor.execute("SELECT * FROM WuFoo_Data").fetchall()
for i, row in enumerate(rows):
    for j, value in enumerate(row):
        tk.Label(table, text=value).grid(row=i+1, column=j, padx=5, pady=5)

# Close the database connection
close_db(conn)

# Start the GUI event loop
window.mainloop()
