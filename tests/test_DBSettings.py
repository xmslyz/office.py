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
        test_db.db_name = "database.com.pl"
        print(test_db.db_name)
        assert test_db.db_name == "database.db"



class TestDBSettings(TestCase):

    def test_dbname(self):
        test_db = DBS.DBSettings()
        test_db.db_name = "da*ta+ba/se_na(me_test"
        assert test_db.db_name == "database_name_test.db"

    def test_path(self):
        test_db = DBS.DBSettings()
        test_db.db_path = "QQQQ\\aaa\\"
        assert test_db.db_path == "QQQQ\\aaa\\"

    def test_table_name(self):
        test_db = DBS.DBSettings()
        test_db.db_table_name = "da@ta#b$a$s$e_t{a{b  l e      "
        assert test_db.db_table_name == "database_table"

    def test_full_path(self):
        test_db = DBS.DBSettings()
        cwd = os.getcwd()
        test_db.db_name = "da*ta+ba/se_na(me_test"
        test_db.db_path = "QQQQ\\aaa\\"
        test_db.db_full_path = 1
        assert test_db.db_full_path == f"{cwd}\\QQQQ\\aaa\\database_name_test.db"