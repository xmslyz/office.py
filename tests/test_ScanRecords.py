from unittest import TestCase
import buissnes.Database.SQLConnector as sr


class test_get_conn_details(TestCase):
    # Working keys
    def test_get_conn_by_key_1(self):
        conn = sr.Connection()
        conn.get_conn_details("intentions")
        assert conn.table_name == "intentions"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_2(self):
        conn = sr.Connection()
        conn.get_conn_details("employees")
        assert conn.table_name == "employees"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_3(self):
        conn = sr.Connection()
        conn.get_conn_details("monthly_stmt")
        assert conn.table_name == "monthly_stmt"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_4(self):
        conn = sr.Connection()
        conn.get_conn_details("general_stmt")
        assert conn.table_name == "general_stmt"
        assert conn.db_name == "sofa.db"

    def test_get_conn_by_key_5(self):
        conn = sr.Connection()
        conn.get_conn_details("pars")
        assert conn.table_name == "pars"
        assert conn.db_name == "sofa.db"

    def test_get_connby_key_6(self):
        conn = sr.Connection()
        conn.get_conn_details("constants")
        assert conn.table_name == "constants"
        assert conn.db_name == "constants.db"

    # Key errors
    def test_get_wrong_key_spelling(self):
        conn = sr.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details("constans")
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))
        
    def test_get_empty_key(self):
        conn = sr.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details("")
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

    def test_get_None_key(self):
        conn = sr.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details(None)
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

    def test_get_False_key(self):
        conn = sr.Connection()
        with self.assertRaises(Exception) as context:
            conn.get_conn_details(False)
        self.assertTrue("Nie ma takiego klucza" in str(context.exception))

