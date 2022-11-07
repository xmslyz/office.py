import BuisnessLayer.Database.Builder


def remove_db_file():
    mydb = BuisnessLayer.Database.Builder.PLUG_database_operator(path_num=1, dbnm_num=1, tbl_num=1)
    # zabezpieczenie przed usunięciem, w programie może to być monitorowane komunikatem okienka pop-up proszącym o potiwerdzenie operacji
    mydb.file_destroyer(confirmed=False)
