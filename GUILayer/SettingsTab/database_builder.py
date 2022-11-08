import BuisnessLayer.Database.Builder


def build_db_intentions():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
    mydb.db_intentions(1, 1, 1)


def build_db_employees():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
    mydb.db_employee(1, 1, 2)


def build_db_monthly_stmt():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
    mydb.db_monthly_stmt(1, 1, 3)


def build_db_general_stmt():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
    mydb.db_general_stmt(1, 1, 4)
