import unittest
from buisness.Database.Builder import DBConnector
from buisness.Database.Geter import GuestsGetter
from buisness.Database.Geter import IntentionsColsGetter
from buisness.Database.Geter import UniqueIDGetter


class TestDatabaseBasicUsage(unittest.TestCase):

    def setUp(self):

        # create database
        self.int = DBConnector()
        self.int.get_conn_details("testintentions")

        # create necessary tables
        msg = f"CREATE TABLE IF NOT EXISTS intentions " \
              f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
              f"type TEXT, " \
              f"amount REAL," \
              f"priest_reciving TEXT," \
              f"celebrated_by TEXT," \
              f"celebration_date TEXT," \
              f"celebration_hour TEXT," \
              f"celebration_type TEXT," \
              f"gregorian INTEGER," \
              f"first_mass INTEGER);"
        self.int.create_connection(0, msg, '')

        self.gstmt = DBConnector()
        self.gstmt.get_conn_details("testgeneral_stmt")
        msg = f"CREATE TABLE IF NOT EXISTS general_stmt " \
              f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
              f"uniqueID TEXT, " \
              f"type TEXT, " \
              f"monthly_stmt_date TEXT, " \
              f"intention_amount INTEGER, " \
              f"intention_sum REAL, " \
              f"bination_amount INTEGER, " \
              f"bination_sum REAL, " \
              f"pars REAL, " \
              f"pretax REAL, " \
              f"taxes REAL, " \
              f"receival REAL, " \
              f"net REAL);"
        self.gstmt.create_connection(0, msg, '')

        self.mstmt = DBConnector()
        self.mstmt.get_conn_details("testmonthly_stmt")
        msg = f"CREATE TABLE IF NOT EXISTS monthly_stmt " \
              f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
              f"uniqueID TEXT, " \
              f"type TEXT, " \
              f"stmt_date TEXT, " \
              f"intention_amount INTEGER, " \
              f"intention_sum REAL, " \
              f"bination_amount INTEGER, " \
              f"bination_sum REAL, " \
              f"pars REAL, " \
              f"pretax REAL, " \
              f"taxes REAL, " \
              f"receival REAL, " \
              f"net REAL);"
        self.mstmt.create_connection(0, msg, '')

        self.emp = DBConnector()
        self.emp.get_conn_details("testemployees")
        msg = f"CREATE TABLE IF NOT EXISTS employees " \
              f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  " \
              f"uniqueID TEXT, " \
              f"type TEXT, " \
              f"name TEXT, " \
              f"surname TEXT, " \
              f"shortname TEXT, " \
              f"abreviation TEXT, " \
              f"function TEXT, " \
              f"taxes TEXT," \
              f"on_duty INTEGER);"
        self.emp.create_connection(0, msg, '')

        # insert employee data
        emp1 = ('aa1', 'Dane osobowe', 'Arturo', 'Adelante', 'Arturito', 'AA', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '100'}",
                1)
        emp2 = ('bb2', 'Dane osobowe', 'Bravo', 'Bigote', 'Bigotes', 'BB', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '120'}", 1)
        emp3 = ('cc3', 'Dane osobowe', 'Castillo', 'Clavo', 'Clavito', 'CC', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '140'}", 1)
        emp4 = ('dd4', 'Dane osobowe', 'Daniel', 'Deza', 'DaDa', 'DD', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szpital': '80'}", 1)
        emp5 = ('ee5', 'Dane osobowe', 'Egipcio', 'Edmundo', 'Edi', 'EE', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'areszt': '200'}", 1)
        emp6 = ('ff6', 'Dane osobowe', 'Francisco', 'Fuerte', 'Fufu', 'FF', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100'}", 0)

        int1 = ("Stypendium mszalne", "100.00", "AA", "AA", "2022-11-01", "07:00", "", "0", "1")
        int2 = ("Stypendium mszalne", "100.00", "AA", "BB", "2022-11-01", "07:00", "", "0", "1")
        int3 = ("Stypendium mszalne", "100.00", "AA", "CC", "2022-11-01", "07:00", "", "0", "1")
        int4 = ("Stypendium mszalne", "100.00", "AA", "DD", "2022-11-01", "07:00", "", "0", "1")
        int5 = ("Stypendium mszalne", "100.00", "AA", "EE", "2022-11-01", "07:00", "", "0", "1")
        int6 = ("Stypendium mszalne", "100.00", "AA", "AA", "2022-11-02", "07:00", "", "0", "1")
        int7 = ("Stypendium mszalne", "100.00", "AA", "BB", "2022-11-02", "07:00", "", "0", "1")
        int8 = ("Stypendium mszalne", "100.00", "AA", "CC", "2022-11-02", "07:00", "", "0", "1")
        int9 = ("Stypendium mszalne", "100.00", "AA", "DD", "2022-11-02", "07:00", "", "0", "1")
        int10 = ("Stypendium mszalne", "100.00", "AA", "EE", "2022-11-02", "07:00", "", "0", "1")
        int11 = ("Stypendium mszalne", "90.00", "BB", "AA", "2022-11-03", "07:00", "", "0", "1")
        int12 = ("Stypendium mszalne", "90.00", "BB", "BB", "2022-11-03", "07:00", "", "0", "1")
        int13 = ("Stypendium mszalne", "90.00", "BB", "CC", "2022-11-03", "07:00", "", "0", "1")
        int14 = ("Stypendium mszalne", "90.00", "BB", "DD", "2022-11-03", "07:00", "", "0", "1")
        int15 = ("Stypendium mszalne", "90.00", "BB", "EE", "2022-11-03", "07:00", "", "0", "1")
        int16 = ("Stypendium mszalne", "90.00", "BB", "AA", "2022-11-04", "07:00", "", "0", "1")
        int17 = ("Stypendium mszalne", "90.00", "BB", "BB", "2022-11-04", "07:00", "", "0", "1")
        int18 = ("Stypendium mszalne", "90.00", "BB", "CC", "2022-11-04", "07:00", "", "0", "1")
        int19 = ("Stypendium mszalne", "90.00", "BB", "DD", "2022-11-04", "07:00", "", "0", "1")
        int20 = ("Stypendium mszalne", "90.00", "BB", "EE", "2022-11-04", "07:00", "", "0", "1")
        int21 = ("Stypendium mszalne", "80.00", "CC", "AA", "2022-11-05", "07:00", "", "0", "1")
        int22 = ("Stypendium mszalne", "80.00", "CC", "BB", "2022-11-05", "07:00", "", "0", "1")
        int23 = ("Stypendium mszalne", "80.00", "CC", "CC", "2022-11-05", "07:00", "", "0", "1")
        int24 = ("Stypendium mszalne", "80.00", "CC", "DD", "2022-11-05", "07:00", "", "0", "1")
        int25 = ("Stypendium mszalne", "80.00", "CC", "EE", "2022-11-05", "07:00", "", "0", "1")
        int26 = ("Stypendium mszalne", "80.00", "CC", "AA", "2022-11-06", "07:00", "", "0", "1")
        int27 = ("Stypendium mszalne", "80.00", "CC", "BB", "2022-11-06", "07:00", "", "0", "1")
        int28 = ("Stypendium mszalne", "80.00", "CC", "CC", "2022-11-06", "07:00", "", "0", "1")
        int29 = ("Stypendium mszalne", "80.00", "CC", "DD", "2022-11-06", "07:00", "", "0", "1")
        int30 = ("Stypendium mszalne", "80.00", "CC", "EE", "2022-11-06", "07:00", "", "0", "1")
        int31 = ("Stypendium mszalne", "70.00", "DD", "AA", "2022-11-07", "07:00", "", "0", "1")
        int32 = ("Stypendium mszalne", "70.00", "DD", "BB", "2022-11-07", "07:00", "", "0", "1")
        int33 = ("Stypendium mszalne", "70.00", "DD", "CC", "2022-11-07", "07:00", "", "0", "1")
        int34 = ("Stypendium mszalne", "70.00", "DD", "DD", "2022-11-07", "07:00", "", "0", "1")
        int35 = ("Stypendium mszalne", "70.00", "DD", "EE", "2022-11-07", "07:00", "", "0", "1")
        int36 = ("Stypendium mszalne", "70.00", "DD", "AA", "2022-11-08", "07:00", "", "0", "1")
        int37 = ("Stypendium mszalne", "70.00", "DD", "BB", "2022-11-08", "07:00", "", "0", "1")
        int38 = ("Stypendium mszalne", "70.00", "DD", "CC", "2022-11-08", "07:00", "", "0", "1")
        int39 = ("Stypendium mszalne", "70.00", "DD", "DD", "2022-11-08", "07:00", "", "0", "1")
        int40 = ("Stypendium mszalne", "70.00", "DD", "EE", "2022-11-08", "07:00", "", "0", "1")
        int41 = ("Stypendium mszalne", "60.00", "EE", "AA", "2022-11-09", "07:00", "", "0", "1")
        int42 = ("Stypendium mszalne", "60.00", "EE", "BB", "2022-11-09", "07:00", "", "0", "1")
        int43 = ("Stypendium mszalne", "60.00", "EE", "CC", "2022-11-09", "07:00", "", "0", "1")
        int44 = ("Stypendium mszalne", "60.00", "EE", "DD", "2022-11-09", "07:00", "", "0", "1")
        int45 = ("Stypendium mszalne", "60.00", "EE", "EE", "2022-11-09", "07:00", "", "0", "1")
        int46 = ("Stypendium mszalne", "60.00", "EE", "AA", "2022-11-10", "07:00", "", "0", "1")
        int47 = ("Stypendium mszalne", "60.00", "EE", "BB", "2022-11-10", "07:00", "", "0", "1")
        int48 = ("Stypendium mszalne", "60.00", "EE", "CC", "2022-11-10", "07:00", "", "0", "1")
        int49 = ("Stypendium mszalne", "60.00", "EE", "DD", "2022-11-10", "07:00", "", "0", "1")
        int50 = ("Stypendium mszalne", "60.00", "EE", "EE", "2022-11-10", "07:00", "", "0", "1")
        int51 = ("Stypendium mszalne", "100.00", "AA", "ZZ", "2022-11-10", "07:00", "", "0", "1")
        int52 = ("Stypendium mszalne", "100.00", "AA", "ZZ", "2022-11-10", "07:00", "", "0", "1")
        int53 = ("Stypendium mszalne", "90.00", "BB", "GG", "2022-11-10", "07:00", "", "0", "1")
        int54 = ("Stypendium mszalne", "90.00", "BB", "HH", "2022-11-10", "07:00", "", "0", "1")

        mth_stmt1 = ("aa1", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        mth_stmt2 = ("bb2", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        mth_stmt3 = ("cc3", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        mth_stmt4 = ("dd4", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        mth_stmt5 = ("ee5", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        mth_stmt6 = ("ff6", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")

        gen_stmt1 = ("aa1", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt2 = ("bb2", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt3 = ("cc3", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt4 = ("dd4", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt5 = ("ee5", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt6 = ("ff6", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
        gen_stmt7 = ("aa1", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt8 = ("bb2", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt9 = ("cc3", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt10 = ("dd4", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt11 = ("ee5", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt12 = ("ff6", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
        gen_stmt13 = ("aa1", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
        gen_stmt14 = ("bb2", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
        gen_stmt15 = ("cc3", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
        gen_stmt16 = ("dd4", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
        gen_stmt17 = ("ee5", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
        gen_stmt18 = ("ff6", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")

        'Całościowe zestawienie'

        msg = '''INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?,?,?) '''
        self.emp.create_connection(2, msg, [emp1, emp2, emp3, emp4, emp5, emp6])

        msg = '''INSERT INTO intentions VALUES (NULL,?,?,?,?,?,?,?,?,?) '''
        self.int.create_connection(2, msg, [int1, int2, int3, int4, int5, int6, int7, int8, int9,
                                            int10, int11, int12, int13, int14, int15, int16, int17, int18, int19,
                                            int20, int21, int22, int23, int24, int25, int26, int27, int28, int29,
                                            int30, int31, int32, int33, int34, int35, int36, int37, int38, int39,
                                            int40, int41, int42, int43, int44, int45, int46, int47, int48, int49,
                                            int50, int51, int52, int53, int54])

        msg = '''INSERT INTO monthly_stmt VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?) '''
        self.mstmt.create_connection(2, msg, [mth_stmt1, mth_stmt2, mth_stmt3, mth_stmt4, mth_stmt5, mth_stmt6])

        msg = '''INSERT INTO general_stmt VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?) '''
        self.mstmt.create_connection(2, msg, [gen_stmt1, gen_stmt2, gen_stmt3, gen_stmt4, gen_stmt5, gen_stmt6,
                                              gen_stmt7, gen_stmt8, gen_stmt9, gen_stmt10, gen_stmt11, gen_stmt12,
                                              gen_stmt13, gen_stmt14, gen_stmt15, gen_stmt16, gen_stmt17, gen_stmt18])

    def tearDown(self):
        mysql = f'DROP TABLE IF EXISTS employees'
        self.emp.create_connection(0, mysql, '')

        mysql = f'DROP TABLE IF EXISTS intentions'
        self.int.create_connection(0, mysql, '')

        mysql = f'DROP TABLE IF EXISTS monthly_stmt'
        self.gstmt.create_connection(0, mysql, '')

        mysql = f'DROP TABLE IF EXISTS general_stmt'
        self.mstmt.create_connection(0, mysql, '')

    #  TEST IF TABLE EXIST
    def test_if_int_exist(self):
        msg = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.int.table_name}';"
        assert self.int.sql_querry(msg)[0][0] == 'intentions'

    def test_if_emp_exist(self):
        msg = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.emp.table_name}';"
        assert self.emp.sql_querry(msg)[0][0] == 'employees'

    # TEST IF IT IS FILLED
    def test_emp_id(self):
        assert self.emp.sql_querry("SELECT id FROM employees") == [(1,), (2,), (3,), (4,), (5,), (6,)]

    def test_emp_abreviation(self):
        assert self.emp.sql_querry("SELECT abreviation FROM employees WHERE abreviation IS ('AA') ")[0][0] == 'AA'

    def test_guest_geter(self):
        gget = GuestsGetter()
        gget.get_conn_details("testintentions")
        res = gget.get_guests("2022-11")
        assert res == [('ZZ', 2), ('GG', 1), ('HH', 1)]

    def test_get_abreviations(self):
        abrget = IntentionsColsGetter()
        abrget.get_conn_details("testemployees")
        result = abrget.get_abreviations()
        assert result == ['AA', 'BB', 'CC', 'DD', 'EE']

    def test_get_all_data(self):
        abrget = IntentionsColsGetter()
        abrget.get_conn_details("testemployees")
        result = abrget.get_all()
        assert len(result) == 54

    def test_get_one_column(self):
        abrget = IntentionsColsGetter()
        abrget.get_conn_details("testemployees")
        result = abrget.get_one("amount")
        assert result[0] == (100,)
        assert result[10] == (90,)

    def test_get_uniqueID_onduty(self):
        uniq = UniqueIDGetter()
        uniq.get_conn_details("testemployees")
        result = uniq.get_uniqueID("AA", "1")
        assert result == "aa1"

    def test_get_uniqueID_notonduty(self):
        uniq = UniqueIDGetter()
        uniq.get_conn_details("testemployees")
        with self.assertRaises(Exception) as context:
            uniq.get_uniqueID("FF", "1")
        self.assertTrue('Brak takiego rejestru' in str(context.exception))

    def test_get_list_unique(self):
        uniq = UniqueIDGetter()
        uniq.get_conn_details("testemployees")
        result = uniq.get_list_uniqueID_when_on_duty()
        assert result == ['aa1', 'bb2', 'cc3', 'dd4', 'ee5']


if __name__ == '__main__':
    unittest.main()
