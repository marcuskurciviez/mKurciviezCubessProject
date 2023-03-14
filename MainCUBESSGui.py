import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as tkmb
import getWufooData
from database import close_db, add_entries_to_db, open_db


# Function to open the "Add User" window
def open_add_user_window():
    # Create a new window for adding a user
    add_user_window = tk.Toplevel(root)
    add_user_window.title("Add User")

    # Create labels and entry fields for each required information
    first_name_label = tk.Label(add_user_window, text="First Name:")
    first_name_label.pack(pady=5)
    first_name_entry = tk.Entry(add_user_window)
    first_name_entry.pack()

    last_name_label = tk.Label(add_user_window, text="Last Name:")
    last_name_label.pack(pady=5)
    last_name_entry = tk.Entry(add_user_window)
    last_name_entry.pack()

    title_label = tk.Label(add_user_window, text="Title:")
    title_label.pack(pady=5)
    title_entry = tk.Entry(add_user_window)
    title_entry.pack()

    email_label = tk.Label(add_user_window, text="BSU Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(add_user_window)
    email_entry.pack()

    department_label = tk.Label(add_user_window, text="Department:")
    department_label.pack(pady=5)
    department_entry = tk.Entry(add_user_window)
    department_entry.pack()

    # Function to get the user input and add the new user to the database
    def add_user():
        # Get the input values
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_entry.get()
        email = email_entry.get()
        department = department_entry.get()

        # Check if email already exists in users table
        conn = sqlite3.connect("cubesProject.sqlite")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE bsu_email=?", (email,))
        result = c.fetchone()

        if result:
            # Display error message if email already exists
            tkmb.showerror("Error", "The user with the same email has already submitted a proposal.")
        else:
            # Add the new user to the database
            c.execute("INSERT INTO users (first_name, last_name, title, bsu_email, department) VALUES (?, ?, ?, ?, ?)",
                      (first_name, last_name, title, email, department))
            conn.commit()
            conn.close()

            # Close the window
            add_user_window.destroy()

    # Create a button to add the new user
    add_button = tk.Button(add_user_window, text="Add User", font=("Arial", 12), command=add_user)
    add_button.pack(pady=10)


# Create the "Data Visualization" button
def open_data_visualization_window():
    # Call the wufooGUI.py file in a new window
    data_visualization_window = tk.Toplevel(root)
    data_visualization_window.title("WuFooData Viewer")
    exec(open("wufooGUI.py").read(), globals())

def refresh_data():
    data = getWufooData.get_wufoo_data()
    entries_data = data["Entries"]
    conn, cursor = open_db("cubesProject.sqlite")
    add_entries_to_db(cursor, entries_data)
    close_db(conn)

    messagebox.showinfo("Success", "Data has been refreshed")

def open_user_table_window():
    # Create a new window for displaying the user table data
    user_table_window = tk.Toplevel(root)
    user_table_window.title("User Table")

    # Connect to the database and retrieve all data from the "users" table
    conn = sqlite3.connect("cubesProject.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    # Create a table to display the data in the new window
    table = tk.Frame(user_table_window)
    table.pack(padx=10, pady=10)

    # Add the data to the table
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            label = tk.Label(table, text=value)
            label.grid(row=i, column=j)

    # Close the database connection
    conn.close()

# Create the main window
root = tk.Tk()

# Set the window title
root.title("CUBESS Project Submission")

# Set the window size
root.geometry("600x200")

# Create a label for the greeting message
greeting_label = tk.Label(root, text="Welcome to CUBESS Project Submission", font=("Arial", 16))
greeting_label.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the "Add User" button
add_user_button = tk.Button(button_frame, text="Add User", font=("Arial", 12), padx=10, pady=5,
                            command=open_add_user_window)
add_user_button.pack(side=tk.LEFT, padx=10)

# Create the "Refresh Data" button
refresh_data_button = tk.Button(button_frame, text="Refresh Data", font=("Arial", 12), padx=10, pady=5, command=refresh_data)
refresh_data_button.pack(side=tk.LEFT, padx=10)

# Create the "Claim" button
claim_button = tk.Button(button_frame, text="Claim", font=("Arial", 12), padx=10, pady=5, command=open_user_table_window)
claim_button.pack(side=tk.LEFT, padx=10)

# Create the "Data Visualization" button
visualization_button = tk.Button(button_frame, text="Data Visualization", font=("Arial", 12), padx=10, pady=5, command=open_data_visualization_window)
visualization_button.pack(side=tk.LEFT, padx=10)

# Run the main loop
root.mainloop()
