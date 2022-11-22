import os
import pathlib
import unittest
from unittest import TestCase
from buisness.Database import SQLConnector as connector
from buisness.Database import AtributesSetter as setter


class test_get_conn_details(TestCase):
    # Working keys
    def test_get_conn_by_key_1(self):
        conn = connector.Connection()
        conn.get_conn_details("intentions")
        assert conn.table_name == "intentions"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_2(self):
        conn = connector.Connection()
        conn.get_conn_details("employees")
        assert conn.table_name == "employees"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_5(self):
        conn = connector.Connection()
        conn.get_conn_details("office")
        assert conn.table_name == "office"
        assert conn.db_name == "sofa.db"

    def test_get_connby_key_6(self):
        conn = connector.Connection()
        conn.get_conn_details("constants")
        assert conn.table_name == "constants"
        assert conn.db_name == "sofa.db"

    # Key errors
    def test_get_wrong_key_spelling(self):
        conn = connector.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details("constans")
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

    def test_get_empty_key(self):
        conn = connector.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details("")
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

    def test_get_None_key(self):
        conn = connector.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details(None)
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

    def test_get_False_key(self):
        conn = connector.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details(False)
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))


class test_dbname_input(TestCase):
    def test_dbname__correct_form(self):
        test_db = setter.DBSettings()
        test_db.db_name = "constans"
        assert test_db.db_name == "constans.db"

    def test_dbname__good_practice(self):
        test_db = setter.DBSettings()
        test_db.db_name = "sofa4.0"
        assert test_db.db_name == "sofa4.db"

    def test_dbname__nonalfanumeric(self):
        test_db = setter.DBSettings()
        test_db.db_name = "d!a@t#a$b%^a^s^e_n&a*m(e).com"
        assert test_db.db_name == "database_name.db"

    def test_dbname__empty(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_name = ""
        self.assertTrue(
            "Nazwa bazy danych nie może być pusta." in str(context.exception)
        )

    def test_dbname__name_with_ext(self):
        test_db = setter.DBSettings()
        test_db.db_name = "Database.pl"
        assert test_db.db_name == "database.db"

    def test_dbname__name_with_spaces(self):
        test_db = setter.DBSettings()
        test_db.db_name = "   da#ta      base      . pl"
        assert test_db.db_name == "database.db"


class test_path_input(TestCase):
    def test_path__nonalfanumeric(self):
        test_db = setter.DBSettings()
        test_db.db_path = "QQQQ\\aaa"
        assert test_db.db_path == str(
            pathlib.PurePath(os.getcwd(), "QQQQ\\aaa")
        )

    def test_path__emptypath(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_path = ""
        self.assertTrue(
            "Ścieżka katalogu nie może być pusta" in str(context.exception)
        )

    def test_path__Nonepath(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_path = None
        self.assertTrue(
            "Ścieżka katalogu nie może być pusta" in str(context.exception)
        )


class test_tablename_input(TestCase):
    def test_dbtablename(self):
        test_db = setter.DBSettings()
        test_db.db_table_name = "da@ta#b$a$s$e_t{a{b  l e      "
        assert test_db.db_table_name == "database_table"

    def test_dbtablename__empty(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_table_name = ""
        self.assertTrue(
            "Nazwa tabeli nie może być pusta." in str(context.exception)
        )

    def test_dbtablename__None(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_table_name = None
        self.assertTrue(
            "Nazwa tabeli nie może być pusta." in str(context.exception)
        )

    def test_dbtablename__name_with_ext(self):
        test_db = setter.DBSettings()
        test_db.db_table_name = "database.pl"
        assert test_db.db_table_name == "database"


class test_file_pathinput(TestCase):
    def test_file(self):
        test_db = setter.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "TEST\\test"
        test_db.db_file_path = ""
        assert test_db.db_file_path == str(
            pathlib.PurePath(os.getcwd(), "TEST\\test", "test.db")
        )

    def test_file_path_nonalfanumeric(self):
        test_db = setter.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "T@EST\\tes^t"
        test_db.db_file_path = ""
        assert test_db.db_file_path == str(
            pathlib.PurePath(os.getcwd(), "TEST\\test", "test.db")
        )

    def test_file_path_Nonepath(self):
        test_db = setter.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_file_path = None
        self.assertTrue(
            "Ścieżka katalogu nie może być NoneType." in str(context.exception)
        )

    def test_file_path_NoSetter(self):
        test_db = setter.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "TEST\\test"
        assert test_db.db_file_path == str(
            pathlib.PurePath(
                os.getcwd(), "DatabaseLayer\\SQLDataBase", "accounting.db"
            ).joinpath()
        )


if __name__ == "__main__":
    unittest.main()
