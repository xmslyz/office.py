# import unittest
# from buisness.Database.Builder import DBConnector
# from buisness.Computing import statements_computer as comp
#
#
# class TestComputing(unittest.TestCase):
#     qdate = "2022-11"
#
#     def setUp(self):
#         # Setup a temporary database
#
#         # create database
#         self.int = DBConnector()
#         self.int.get_conn_details("testintentions")
#
#         # create necessary tables
#         msg = f"CREATE TABLE IF NOT EXISTS intentions " \
#               f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
#               f"type TEXT, " \
#               f"amount REAL," \
#               f"priest_reciving TEXT," \
#               f"celebrated_by TEXT," \
#               f"celebration_date TEXT," \
#               f"celebration_hour TEXT," \
#               f"celebration_type TEXT," \
#               f"gregorian INTEGER," \
#               f"first_mass INTEGER);"
#         self.int.create_connection(0, msg, '')
#
#         self.gstmt = DBConnector()
#         self.gstmt.get_conn_details("testgeneral_stmt")
#         msg = f"CREATE TABLE IF NOT EXISTS general_stmt " \
#               f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
#               f"uniqueID TEXT, " \
#               f"type TEXT, " \
#               f"monthly_stmt_date TEXT, " \
#               f"intention_amount INTEGER, " \
#               f"intention_sum REAL, " \
#               f"bination_amount INTEGER, " \
#               f"bination_sum REAL, " \
#               f"pars REAL, " \
#               f"pretax REAL, " \
#               f"taxes REAL, " \
#               f"receival REAL, " \
#               f"net REAL);"
#         self.gstmt.create_connection(0, msg, '')
#
#         self.mstmt = DBConnector()
#         self.mstmt.get_conn_details("testmonthly_stmt")
#         msg = f"CREATE TABLE IF NOT EXISTS monthly_stmt " \
#               f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
#               f"uniqueID TEXT, " \
#               f"type TEXT, " \
#               f"stmt_date TEXT, " \
#               f"intention_amount INTEGER, " \
#               f"intention_sum REAL, " \
#               f"bination_amount INTEGER, " \
#               f"bination_sum REAL, " \
#               f"pars REAL, " \
#               f"pretax REAL, " \
#               f"taxes REAL, " \
#               f"receival REAL, " \
#               f"net REAL);"
#         self.mstmt.create_connection(0, msg, '')
#
#         self.emp = DBConnector()
#         self.emp.get_conn_details("testemployees")
#         msg = f"CREATE TABLE IF NOT EXISTS employees " \
#               f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  " \
#               f"uniqueID TEXT, " \
#               f"type TEXT, " \
#               f"name TEXT, " \
#               f"surname TEXT, " \
#               f"shortname TEXT, " \
#               f"abreviation TEXT, " \
#               f"function TEXT, " \
#               f"taxes TEXT," \
#               f"on_duty INTEGER);"
#         self.emp.create_connection(0, msg, '')
#
#         # insert employee data
#         emp1 = ('aa1', 'Dane osobowe', 'Arturo', 'Adelante', 'Arturito', 'AA', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '100'}",
#                 1)
#         emp2 = ('bb2', 'Dane osobowe', 'Bravo', 'Bigote', 'Bigotes', 'BB', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '120'}", 1)
#         emp3 = ('cc3', 'Dane osobowe', 'Castillo', 'Clavo', 'Clavito', 'CC', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szkoła': '140'}", 1)
#         emp4 = ('dd4', 'Dane osobowe', 'Daniel', 'Deza', 'DaDa', 'DD', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'szpital': '80'}", 1)
#         emp5 = ('ee5', 'Dane osobowe', 'Egipcio', 'Edmundo', 'Edi', 'EE',
#                 'Wikary', "{'dziesięcina': '230.00', 'dke': '100', 'areszt': "
#                           "'200'}", 0)
#         emp6 = ('ff6', 'Dane osobowe', 'Francisco', 'Fuerte', 'Fufu', 'FF', 'Wikary', "{'dziesięcina': '230.00', 'dke': '100'}", 0)
#
#         int1 = ("Stypendium mszalne", "100.00", "AA", "AA", "2022-11-01", "07:00", "", "0", "1")
#         int2 = ("Stypendium mszalne", "100.00", "AA", "BB", "2022-11-01", "07:00", "", "0", "1")
#         int3 = ("Stypendium mszalne", "100.00", "AA", "CC", "2022-11-01", "07:00", "", "0", "1")
#         int4 = ("Stypendium mszalne", "100.00", "AA", "DD", "2022-11-01", "07:00", "", "0", "1")
#         int5 = ("Stypendium mszalne", "100.00", "AA", "EE", "2022-11-01", "07:00", "", "0", "1")
#         int6 = ("Stypendium mszalne", "100.00", "AA", "AA", "2022-11-01", "07:00", "", "0", "0")
#         int7 = ("Stypendium mszalne", "100.00", "AA", "BB", "2022-11-02", "07:00", "", "0", "1")
#         int8 = ("Stypendium mszalne", "100.00", "AA", "CC", "2022-11-02", "07:00", "", "0", "1")
#         int9 = ("Stypendium mszalne", "100.00", "AA", "DD", "2022-11-02", "07:00", "", "0", "1")
#         int10 = ("Stypendium mszalne", "100.00", "AA", "EE", "2022-11-02", "07:00", "", "0", "1")
#         int11 = ("Stypendium mszalne", "900.00", "BB", "AA", "2022-11-03", "07:00", "", "1", "1")
#         int12 = ("Stypendium mszalne", "0.00", "BB", "BB", "2022-11-03", "07:00", "", "1", "1")
#         int13 = ("Stypendium mszalne", "0.00", "BB", "CC", "2022-11-03", "07:00", "", "1", "1")
#         int14 = ("Stypendium mszalne", "0.00", "BB", "DD", "2022-11-03", "07:00", "", "1", "1")
#         int15 = ("Stypendium mszalne", "0.00", "BB", "EE", "2022-11-03", "07:00", "", "1", "1")
#         int16 = ("Stypendium mszalne", "0.00", "BB", "AA", "2022-11-04", "07:00", "", "1", "1")
#         int17 = ("Stypendium mszalne", "0.00", "BB", "BB", "2022-11-03", "07:00", "", "1", "0")
#         int18 = ("Stypendium mszalne", "0.00", "BB", "CC", "2022-11-04", "07:00", "", "1", "1")
#         int19 = ("Stypendium mszalne", "0.00", "BB", "DD", "2022-11-04", "07:00", "", "1", "1")
#         int20 = ("Stypendium mszalne", "0.00", "BB", "EE", "2022-11-04", "07:00", "", "1", "1")
#         int21 = ("Stypendium mszalne", "80.00", "CC", "AA", "2022-11-05", "07:00", "", "0", "1")
#         int22 = ("Stypendium mszalne", "80.00", "CC", "BB", "2022-11-05", "07:00", "", "0", "1")
#         int23 = ("Stypendium mszalne", "80.00", "CC", "CC", "2022-11-05", "07:00", "", "0", "1")
#         int24 = ("Stypendium mszalne", "80.00", "CC", "DD", "2022-11-05", "07:00", "", "0", "1")
#         int25 = ("Stypendium mszalne", "80.00", "CC", "EE", "2022-11-05", "07:00", "", "0", "1")
#         int26 = ("Stypendium mszalne", "80.00", "CC", "AA", "2022-11-06", "07:00", "", "0", "1")
#         int27 = ("Stypendium mszalne", "80.00", "CC", "BB", "2022-11-05", "07:00", "", "0", "0")
#         int28 = ("Stypendium mszalne", "80.00", "CC", "CC", "2022-11-06", "07:00", "", "0", "1")
#         int29 = ("Stypendium mszalne", "80.00", "CC", "DD", "2022-11-06", "07:00", "", "0", "1")
#         int30 = ("Stypendium mszalne", "80.00", "CC", "EE", "2022-11-06", "07:00", "", "0", "1")
#         int31 = ("Stypendium mszalne", "70.00", "DD", "AA", "2022-11-07", "07:00", "", "0", "1")
#         int32 = ("Stypendium mszalne", "70.00", "DD", "BB", "2022-11-07", "07:00", "", "0", "1")
#         int33 = ("Stypendium mszalne", "70.00", "DD", "CC", "2022-11-07", "07:00", "", "0", "1")
#         int34 = ("Stypendium mszalne", "70.00", "DD", "DD", "2022-11-07", "07:00", "", "0", "1")
#         int35 = ("Stypendium mszalne", "70.00", "DD", "EE", "2022-11-07", "07:00", "", "0", "1")
#         int36 = ("Stypendium mszalne", "70.00", "DD", "AA", "2022-11-08", "07:00", "", "0", "1")
#         int37 = ("Stypendium mszalne", "70.00", "DD", "BB", "2022-11-08", "07:00", "", "0", "1")
#         int38 = ("Stypendium mszalne", "70.00", "DD", "CC", "2022-11-08", "07:00", "", "0", "1")
#         int39 = ("Stypendium mszalne", "70.00", "DD", "DD", "2022-11-08", "07:00", "", "0", "1")
#         int40 = ("Stypendium mszalne", "70.00", "DD", "EE", "2022-11-08", "07:00", "", "0", "1")
#         int41 = ("Stypendium mszalne", "60.00", "EE", "AA", "2022-11-09", "07:00", "", "0", "1")
#         int42 = ("Stypendium mszalne", "60.00", "EE", "BB", "2022-11-09", "07:00", "", "0", "1")
#         int43 = ("Stypendium mszalne", "60.00", "EE", "CC", "2022-11-09", "07:00", "", "0", "1")
#         int44 = ("Stypendium mszalne", "60.00", "EE", "DD", "2022-11-09", "07:00", "", "0", "1")
#         int45 = ("Stypendium mszalne", "60.00", "EE", "EE", "2022-11-09", "07:00", "", "0", "1")
#         int46 = ("Stypendium mszalne", "60.00", "EE", "AA", "2022-11-10", "07:00", "", "0", "1")
#         int47 = ("Stypendium mszalne", "60.00", "EE", "BB", "2022-11-10", "07:00", "", "0", "1")
#         int48 = ("Stypendium mszalne", "60.00", "EE", "CC", "2022-11-10", "07:00", "", "0", "1")
#         int49 = ("Stypendium mszalne", "60.00", "EE", "DD", "2022-11-10", "07:00", "", "0", "1")
#         int50 = ("Stypendium mszalne", "60.00", "EE", "EE", "2022-11-10", "07:00", "", "0", "1")
#         int51 = ("Stypendium mszalne", "", "", "ZZ", "2022-11-30", "07:00", "", "0", "1")
#         int52 = ("Stypendium mszalne", "", "", "ZZ", "2022-11-30", "07:00", "", "0", "1")
#         int53 = ("Stypendium mszalne", "", "", "", "2022-11-30", "07:00", "", "0", "1")
#         int54 = ("Stypendium mszalne", "90.00", "BB", "", "2022-11-30", "07:00", "", "0", "1")
#
#         mth_stmt1 = ("aa1", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         mth_stmt2 = ("bb2", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         mth_stmt3 = ("cc3", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         mth_stmt4 = ("dd4", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         mth_stmt5 = ("ee5", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         mth_stmt6 = ("ff6", "Zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#
#         gen_stmt1 = ("aa1", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt2 = ("bb2", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt3 = ("cc3", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt4 = ("dd4", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt5 = ("ee5", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt6 = ("ff6", "Całościowe zestawienie", "2022-10", "", "", "", "", "", "", "", "", "")
#         gen_stmt7 = ("aa1", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt8 = ("bb2", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt9 = ("cc3", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt10 = ("dd4", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt11 = ("ee5", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt12 = ("ff6", "Całościowe zestawienie", "2022-11", "", "", "", "", "", "", "", "", "")
#         gen_stmt13 = ("aa1", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#         gen_stmt14 = ("bb2", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#         gen_stmt15 = ("cc3", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#         gen_stmt16 = ("dd4", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#         gen_stmt17 = ("ee5", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#         gen_stmt18 = ("ff6", "Całościowe zestawienie", "2022-12", "", "", "", "", "", "", "", "", "")
#
#         'Całościowe zestawienie'
#
#         msg = '''INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?,?,?) '''
#         self.emp.create_connection(2, msg, [emp1, emp2, emp3, emp4, emp5, emp6])
#
#         msg = '''INSERT INTO intentions VALUES (NULL,?,?,?,?,?,?,?,?,?) '''
#         self.int.create_connection(2, msg, [int1, int2, int3, int4, int5, int6, int7, int8, int9,
#                                             int10, int11, int12, int13, int14, int15, int16, int17, int18, int19,
#                                             int20, int21, int22, int23, int24, int25, int26, int27, int28, int29,
#                                             int30, int31, int32, int33, int34, int35, int36, int37, int38, int39,
#                                             int40, int41, int42, int43, int44, int45, int46, int47, int48, int49,
#                                             int50, int51, int52, int53, int54])
#
#         msg = '''INSERT INTO monthly_stmt VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?) '''
#         self.mstmt.create_connection(2, msg, [mth_stmt1, mth_stmt2, mth_stmt3, mth_stmt4, mth_stmt5, mth_stmt6])
#
#         msg = '''INSERT INTO general_stmt VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?) '''
#         self.mstmt.create_connection(2, msg, [gen_stmt1, gen_stmt2, gen_stmt3, gen_stmt4, gen_stmt5, gen_stmt6,
#                                               gen_stmt7, gen_stmt8, gen_stmt9, gen_stmt10, gen_stmt11, gen_stmt12,
#                                               gen_stmt13, gen_stmt14, gen_stmt15, gen_stmt16, gen_stmt17, gen_stmt18])
#
#     def tearDown(self):
#         mysql = f'DROP TABLE IF EXISTS employees'
#         self.emp.create_connection(0, mysql, '')
#
#         mysql = f'DROP TABLE IF EXISTS intentions'
#         self.int.create_connection(0, mysql, '')
#
#         mysql = f'DROP TABLE IF EXISTS monthly_stmt'
#         self.gstmt.create_connection(0, mysql, '')
#
#         mysql = f'DROP TABLE IF EXISTS general_stmt'
#         self.mstmt.create_connection(0, mysql, '')
#
#     def test_get_record_by_id(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.record_by_id("1")
#         assert result[0][2] == 100.0
#         assert result[0][3] == 'AA'
#         assert result[0][5] == '2022-11-01'
#
#     def test_get_record_in_qdate(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.records_in_qdate__list()
#         assert (len(result)) == 54
#         assert result[0][5] == '2022-11-01'
#         assert result[-1][5] == '2022-11-30'
#
#     def test_get_it__wrong_type_input(self):  # works with: None, bool, etc.
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         with self.assertRaises(Exception) as context:
#             stmt.record_by_id(1)
#         self.assertTrue("Wrong input type" in str(context.exception))
#
#     def test_get_it__no_reocrd(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         with self.assertRaises(Exception) as context:
#             stmt.record_by_id("0")
#         self.assertTrue("No record with this id" in str(context.exception))  # or: "Out of range", what's better?
#
#     #  LISTS
#     def test_list_all_cash_recived(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.records_in_qdate__list()
#         assert len(result) == 54
#
#     def test_list_binations(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.binations__list()
#         assert len(result) == 3
#
#     def test_list_gregorians(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.gregorian__list()
#         assert len(result) == 10
#
#     def test_list_aplicated(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.aplicated_stipends__list()
#         assert len(result) == 52
#
#     def test_list_paidnotaplicated(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result = stmt.paid_not_applicated__list()
#         assert len(result) == 1
#
#     def test_not_paid(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         result1 = stmt.not_paid_but_aplicated__list()
#         result2 = stmt.not_paid_nor_aplicated__list()
#         assert len(result1) == 2
#         assert len(result2) == 1
#
#     # AMOUNT
#     def test_amount_of_all_paid(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_all_paid() == 51
#
#     def test_amount_all_binations(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_binations() == 3
#
#     def test_amount_all_gregorian(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_all_gregorian() == 10
#
#     def test_amount_all_guest_masses(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_guest_masses() == 12
#
#     def test_amount_of_aplicated(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_aplicated() == 52
#
#     def test_sum_of_all_recived(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_of_all_recived() == 4090.0
#
#     def test_sum_of_all_gregorian(self):
#         stmt = comp.Collation(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_of_all_gregorian() == 900.0
#
# #  COMPUTE
#     def test_mediana(self):
#         stmt = comp.Compute(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.mediana() == 87.03
#
#     def test_sum_of_binations(self):
#         stmt = comp.Compute(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_of_binations() == 150.0
#
#     def test_gregorian_mediana(self):
#         stmt = comp.Compute(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.gregorian_mediana() == 90.0
#
#     def test_gregorian_sum_of_medianas(self):
#         stmt = comp.Compute(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.gregorian_sum_of_medianas() == 900.0
#
#     def test_sum_for_guests(self):
#         stmt = comp.Compute(self.qdate)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_for_guests() == 720.0
#
#     # EMPLOYEE
#     def test_recieved_by_a_priest__list(self):
#         who_recived = 'AA'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         zz = stmt.list_of_recieved_by_a_priest()
#         assert len(zz) == 10
#
#     def test_sum_recieved_by_a_AA(self):
#         who_recived = 'AA'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_of_recieved_by_a_priest() == 1000.0
#
#     def test_sum_recieved_by_a_BB(self):
#         who_recived = 'BB'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.sum_of_recieved_by_a_priest() == 990.0
#
#     def test_amount_of_all_masses_aplied_by_a_priest(self):
#         who_recived = 'BB'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_all_masses_applied_by_a_priest() == 10
#
#     def test_amount_of_first_masses_applied_by_a_priest(self):
#         who_recived = 'AA'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_first_masses_applied_by_a_priest() == 9
#
#     def test_amount_of_bination_applied_by_a_priest(self):
#         who_recived = 'AA'
#         stmt = comp.EmployeeCollation(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.amount_of_bination_applied_by_a_priest() == 1
#
#     # EMPLOYEE COLATION
#     def test_quota_for_priest(self):
#         who_recived = 'AA'
#         compt = comp.Compute(self.qdate)
#         compt.get_conn_details("testintentions")
#         stmt = comp.ComputeEmployee(self.qdate, who_recived, compt)
#         stmt.get_conn_details("testintentions")
#         assert stmt.quota_for_priest() == 783.27
#
#     def test_bination_quota_for_priest(self):
#         who_recived = 'AA'
#         compt = comp.Compute(self.qdate)
#         compt.get_conn_details("testintentions")
#         stmt = comp.ComputeEmployee(self.qdate, who_recived, compt)
#         stmt.get_conn_details("testintentions")
#         assert stmt.bination_quota_for_priest() == 50.0
#
#     def test_total_wage_for_priest(self):
#         who_recived = 'AA'
#         compt = comp.Compute(self.qdate)
#         compt.get_conn_details("testintentions")
#         stmt = comp.ComputeEmployee(self.qdate, who_recived, compt)
#         stmt.get_conn_details("testintentions")
#         assert stmt.total_wage_for_priest() == 833.27
#
#     def test_net_for_priest(self):
#         who_recived = 'AA'
#         compt = comp.Compute(self.qdate)
#         compt.get_conn_details("testintentions")
#         stmt = comp.ComputeEmployee(self.qdate, who_recived, compt)
#         stmt.get_conn_details("testintentions")
#         assert stmt.net_for_priest() == -166.73
#
#     def test_pars_for_priest(self):
#         who_recived = 'AA'
#         stmt = comp.ComputeEmployee(self.qdate, who_recived)
#         stmt.get_conn_details("testintentions")
#         assert stmt.pars_for_priest() == 0
#
#
# if __name__ == '__main__':
#     unittest.main()
