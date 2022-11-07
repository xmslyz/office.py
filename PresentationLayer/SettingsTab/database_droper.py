import BuisnessLayer.Database.Builder


def drop_db_intentions():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=1)
    mydb.drop_table(1, 1, 1)


def drop_db_employees():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=2)
    mydb.drop_table(1, 1, 2)


def drop_db_collations():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=3)
    mydb.drop_table(1, 1, 3)
