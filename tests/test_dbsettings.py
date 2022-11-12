import os
import pathlib
from unittest import TestCase
from buissnes.Database import AtributesSetter as DBS


class TestDBName(TestCase):

    def test_dbname__correct_form(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "constans"
        assert test_db.db_name == "constans.db"

    def test_dbname__good_practice(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "sofa4.0"
        assert test_db.db_name == "sofa4.db"

    def test_dbname__nonalfanumeric(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "d!a@t#a$b%^a^s^e_n&a*m(e).com"
        assert test_db.db_name == "database_name.db"

    def test_dbname__empty(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_name = ''
        self.assertTrue('Nazwa bazy danych nie może być pusta.' in str(context.exception))

    def test_dbname__name_with_ext(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "Database.pl"
        assert test_db.db_name == "database.db"

    def test_dbname__name_with_spaces(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "   da#ta      base      . pl"
        assert test_db.db_name == "database.db"


class TestDBPath(TestCase):

    def test_path__nonalfanumeric(self):
        test_db = DBS.DBSettings()
        test_db.db_path = "QQQQ\\aaa"
        assert test_db.db_path == str(pathlib.PurePath(os.getcwd(), "QQQQ\\aaa"))

    def test_path__emptypath(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_path = ''
        self.assertTrue('Ścieżka katalogu nie może być pusta' in str(context.exception))

    def test_path__Nonepath(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_path = None
        self.assertTrue('Ścieżka katalogu nie może być pusta' in str(context.exception))


class TestDBTablename(TestCase):
    def test_dbtablename(self):
        test_db = DBS.DBSettings()
        test_db.db_table_name = "da@ta#b$a$s$e_t{a{b  l e      "
        assert test_db.db_table_name == "database_table"

    def test_dbtablename__empty(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_table_name = ''
        self.assertTrue('Nazwa tabeli nie może być pusta.' in str(context.exception))

    def test_dbtablename__None(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_table_name = None
        self.assertTrue('Nazwa tabeli nie może być pusta.' in str(context.exception))

    def test_dbtablename__name_with_ext(self):
        test_db = DBS.DBSettings()
        test_db.db_table_name = "database.pl"
        print(test_db.db_table_name)
        assert test_db.db_table_name == "database"


class TestDBFullPath(TestCase):
    def test_fullpath(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "TEST\\test"
        test_db.db_file_path = ''
        assert test_db.db_file_path == str(pathlib.PurePath(os.getcwd(), "TEST\\test", "test.db"))

    def test_fullpath__nonalfanumeric(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "T@EST\\tes^t"
        test_db.db_file_path = ''
        assert test_db.db_file_path == str(pathlib.PurePath(os.getcwd(), "TEST\\test", "test.db"))

    def test_fullpath__emptypath(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_file_path = None
        self.assertTrue('Ścieżka katalogu nie może być NoneType.' in str(context.exception))

    def test_fullpath__Nonepath(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_path = None
        self.assertTrue('Ścieżka katalogu nie może być pusta' in str(context.exception))

    def test_fullpath__NoSetter(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "TEST\\test"
        assert test_db.db_file_path == str(pathlib.PurePath(os.getcwd(), "DatabaseLayer\\SQLDataBase", "accounting.db").joinpath())