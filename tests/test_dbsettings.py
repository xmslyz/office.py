import os
from unittest import TestCase
from buissnes.Database import AtributesSetter as DBS


class TestDBName(TestCase):

    def test_dbname__nonalfanumeric(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "da*ta+ba/se_na(me_test"
        assert test_db.db_name == "database_name_test.db"

    def test_dbname__empty(self):
        test_db = DBS.DBSettings()
        with self.assertRaises(Exception) as context:
            test_db.db_name = ''
        self.assertTrue('Nazwa bazy danych nie może być pusta.' in str(context.exception))

    def test_dbname__name_with_ext(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "database.pl"
        print(test_db.db_name)
        assert test_db.db_name == "database.db"


class TestDBPath(TestCase):

    def test_path__nonalfanumeric(self):
        test_db = DBS.DBSettings()
        test_db.db_path = "Q$QQQ\\a+-aa\\"
        print(test_db.db_path)
        assert test_db.db_path == "QQQQ\\aaa"

    def test_path__with_slashes(self):
        test_db = DBS.DBSettings()
        test_db.db_path = "Q$QQQ\\a+-aa\\\\"
        print(test_db.db_path)
        assert test_db.db_path == "QQQQ\\aaa"


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

    def test_dbtablename__name_with_ext(self):
        test_db = DBS.DBSettings()
        test_db.db_table_name = "database.pl"
        print(test_db.db_table_name)
        assert test_db.db_table_name == "database"


class TestDBFullPath(TestCase):
    def test_fullpath(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "test.db"
        test_db.db_path = "TEST\\test\\"
        test_db.db_full_path = ''
        assert test_db.db_full_path == f'{os.getcwd()}\\TEST\\test\\test.db'
