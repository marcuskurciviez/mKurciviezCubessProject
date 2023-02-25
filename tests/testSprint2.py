import unittest
import database
import getWufooData


class TestGetData(unittest.TestCase):

    def test_get_data(self):
        """ for this test we are just getting the data from wufoo, getting the Entries and counting them"""
        json_data = getWufooData.get_wufoo_data()
        entries = json_data['Entries']
        self.assertGreaterEqual(len(entries), 10)

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.connection, self.cursor = database.open_db("test.db")
        database.create_entries_table(self.cursor)
        entries_data = [
            {
                "EntryID": "1",
                "Prefix": "Mr.",
                "First_Name": "John",
                "Last_Name": "Doe",
                "Permission_to_Share": "Yes",
                "dateCreated": "2022-02-01",
            }
        ]
        database.add_entries_to_db(self.cursor, entries_data)

    def tearDown(self):
        database.close_db(self.connection)

    def test_entries_table_has_data(self):
        self.cursor.execute("SELECT COUNT(*) FROM WuFooData")
        num_entries = self.cursor.fetchone()[0]
        self.assertGreater(num_entries, 0)


if __name__ == '__main__':
    unittest.main()


