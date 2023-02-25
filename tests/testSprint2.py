import getWufooData
import database


def test_get_data():
    """ for this test we are just getting the data from wufoo, getting the Entries and counting them"""
    json_data = getWufooData.get_wufoo_data()
    entries = json_data['Entries']
    assert len(entries) >= 10


def test_table_created():
    connection, cursor = database.open_db("cubesProject.sqlite.db")
    database.create_entries_table(cursor)
    cursor.execute("SELECT Count() FROM SQLITE_MASTER WHERE name = ?", ["WuFooData"])
    record = cursor.fetchone()
    number_of_rows = record[0]  # the number is the first )and only) item in the tuple
    assert number_of_rows == 1
