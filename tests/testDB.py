import pytest
import main


def test_database():
    data_test = [(11, "Mr", "Qui", "Yo", "Cool", "BSU", "yosocool@lol.com", "", "6175326910", "", "", "Yes", "", "Yes", "", "No", "", "", "HeckYeah", "", "", "Yes", "",
                  "101010", "lol")]

    connection, db_cursor = main.open_db("testDatabase.db")
    main.create_wufoo_table(db_cursor)
    main.put_wufoo_data_in("test", data_test, db_cursor)
    connection.commit()
