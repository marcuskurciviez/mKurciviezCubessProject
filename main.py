from database import open_db, close_db
import database
import getWufooData

db_name = "cubes_Project.sqlite"


def main():
    json_response = getWufooData.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = open_db(db_name)
    database.create_entries_table(cursor)
    database.add_entries_to_db(cursor, entries_list)
    close_db(conn)


if __name__ == "__main__":
    main()
