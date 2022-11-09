import buissnes.Database
import buissnes.Database.Builder


class Build_DB_Button:
    def build_database(self):
        self.build_db_intentions()
        self.build_db_employees()
        self.build_db_monthly_stmt()
        self.build_db_general_stmt()

    def build_db_intentions():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        mydb.db_intentions(1, 1, 1)

    def build_db_employees():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
        mydb.db_employee(1, 1, 2)

    def build_db_monthly_stmt():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
        mydb.db_monthly_stmt(1, 1, 3)

    def build_db_general_stmt():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
        mydb.db_general_stmt(1, 1, 4)


class Drop_DB_Button:

    def drop_database(self):
        self.drop_db_intentions()
        self.drop_db_employees()
        self.drop_db_monthly_stmt()
        self.drop_db_general_stmt()

    def drop_db_intentions():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        mydb.drop_table(1, 1, 1)

    def drop_db_employees():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
        mydb.drop_table(1, 1, 2)

    def drop_db_monthly_stmt():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
        mydb.drop_table(1, 1, 3)

    def drop_db_general_stmt():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
        mydb.drop_table(1, 1, 4)


class Remove_DB_Files:

    def remove_db_file():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        # zabezpieczenie przed usunięciem, w programie może to być monitorowane komunikatem okienka pop-up proszącym o potiwerdzenie operacji
        mydb.file_destroyer(confirmed=False)


class Format_DB:

    def format_database():
        Drop_DB_Button().drop_database()
        Remove_DB_Files.remove_db_file()
        Build_DB_Button().build_database()

