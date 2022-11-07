import BuisnessLayer.Database.Builder


def build_db_intentions():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=1)
    mydb.db_intentions(1, 1, 1)


def build_db_employees():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=2)
    mydb.db_employee(1, 1, 2)


def build_db_collations():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=3)
    mydb.db_collations(1, 1, 3)
