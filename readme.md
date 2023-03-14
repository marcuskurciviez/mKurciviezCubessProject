# Marcus Kurciviez

### Installation:

For this project, I have used the following libraries in my code:
* import sys
* import requests
* from requests.auth import HTTPBasicAuth
* import tkinter as tk
* import sqlite3
* from tkinter import messagebox

### Brief Description:
The main.py will run the database code, as well as open the main GUI from the MainCUBESSGui.py file, in which it will display four buttons:
- Add User: Can add a user to a new table called Users, and if there is a same email address it will display an error message that a user already exists with that email.
- Refresh Data: It will update the WuFoo Data table using the getWufooData.py file.
- Claim: Will list the users from the user table.
- Data Visualization: Will display the data from the WuFoo table, and will show updated data. 

### What's Missing:
- The tests have been struggling, they want to work sometimes, and I'll come back to it later and it will fail. The error with the WuFoo table not existing, however it would work sometimes and other times it wouldn't. That is the main part that is missing from this code. 
- The claim's visual aspect/ how to incorporate it was challenging and tricky, on top of confusing my head. I did not get around to the visual part or allowing the user to claim a row in the table. 

### Wufoo Form Link:
The Wufoo data is being collected from: 

https://mkurciviez.wufoo.com/forms/cubess-project-proposal-submission/

