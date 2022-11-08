import BuisnessLayer.Database.Builder


def drop_db_intentions():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
    mydb.drop_table(1, 1, 1)


def drop_db_employees():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
    mydb.drop_table(1, 1, 2)


def drop_db_monthly_stmt():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
    mydb.drop_table(1, 1, 3)


def drop_db_general_stmt():
    mydb = BuisnessLayer.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
    mydb.drop_table(1, 1, 4)
