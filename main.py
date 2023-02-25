from database import open_db, close_db
import database
import getWufooData
import wufooGUI

db_name = "cubesProject.sqlite"


def main():
    json_response = getWufooData.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = open_db(db_name)
    database.create_entries_table(cursor)
    database.add_entries_to_db(cursor, entries_list)
    close_db(conn)
    wufooGUI.WufooGUI(db_name)


if __name__ == "__main__":
    main()
