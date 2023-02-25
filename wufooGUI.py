import tkinter as tk
import sqlite3
from tkinter import ttk

db_name = "cubesProject.sqlite"


def get_data():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT Org FROM WuFooData")
    rows = cursor.fetchall()
    conn.close()
    return rows


def display_data(event):
    selected_name = name_listbox.get(name_listbox.curselection())
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WuFooData WHERE Org=?", selected_name)
    data = cursor.fetchone()
    conn.close()

    data_str = '\n'.join([f"{key}: {value}" for key, value in zip(['EntryID', 'Prefix', 'First_Name', 'Last_Name', 'Title', 'Org', 'Email', 'OrgWebsite', 'Phone', 'Course_Project', 'Guest_Speaker', 'Site_Visit', 'Job_Shadow', 'Internship', 'Career_Panel', 'Networking_Event', 'Summer_2022', 'Fall_2022', 'Spring_2023', 'Summer_2023', 'Other', 'Permission_to_Share', 'dateCreated'], data)])
    data_label.config(text=data_str)


root = tk.Tk()
root.title("WuFooData")

# Create and populate name listbox
names = get_data()
name_listbox = tk.Listbox(root, width=25, height=25)
for name in names:
    name_listbox.insert(tk.END, name)
name_listbox.pack(side=tk.LEFT)

# Create and place scrollbar for name listbox
scrollbar = tk.Scrollbar(root, command=name_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
name_listbox.config(yscrollcommand=scrollbar.set)

# Create and place label for displaying data
data_label = tk.Label(root, text="", font=("Courier", 20), justify=tk.LEFT)
data_label.pack(side=tk.LEFT, padx=20)

# Bind click event to name listbox
name_listbox.bind("<<ListboxSelect>>", display_data)

root.mainloop()
