import tkinter as tk
import sqlite3

db_name = "cubes_Project.sqlite"


def display_data(row_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM WuFoo_Data WHERE EntryID={row_id}")
    data = cursor.fetchone()
    conn.close()

    # display data however you want


def main():
    root = tk.Tk()
    root.title("Data Display")

    # create a listbox to display the names
    name_listbox = tk.Listbox(root)
    name_listbox.pack(side="left")

    # populate the listbox with names from the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT EntryID, First_Name, Last_Name FROM WuFoo_Data")
    for row in cursor.fetchall():
        name_listbox.insert("end", f"{row[1]} {row[2]}")
    conn.close()

    # add a scrollbar to the listbox
    scrollbar = tk.Scrollbar(root, command=name_listbox.yview)
    scrollbar.pack(side="left", fill="y")
    name_listbox.config(yscrollcommand=scrollbar.set)

    # when a name is clicked on, display the rest of the data for that row
    def on_select(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            row_id = name_listbox.get(index).split()[0]
            if row_id.isdigit():
                display_data(row_id)
            else:
                # handle the case where the selected name does not have a valid ID
                print("Invalid row ID")

    name_listbox.bind("<<ListboxSelect>>", on_select)

    root.mainloop()


if __name__ == "__main__":
    main()
