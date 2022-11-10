import buissnes.Database
import buissnes.Database.Builder


class Build_DB_Button:
    def build_database(self):
        self.__build_db_intentions()
        self.__build_db_employees()
        self.__build_db_monthly_stmt()
        self.__build_db_general_stmt()

    def __build_db_intentions(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        mydb.db_intentions(1, 1, 1)

    def __build_db_employees(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
        mydb.db_employee(1, 1, 2)

    def __build_db_monthly_stmt(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
        mydb.db_monthly_stmt(1, 1, 3)

    def __build_db_general_stmt(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
        mydb.db_general_stmt(1, 1, 4)


class Drop_DB_Button:

    def drop_database(self):
        self.__drop_db_intentions()
        self.__drop_db_employees()
        self.__drop_db_monthly_stmt()
        self.__drop_db_general_stmt()

    def __drop_db_intentions(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        mydb.drop_table(1, 1, 1)

    def __drop_db_employees(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=2)
        mydb.drop_table(1, 1, 2)

    def __drop_db_monthly_stmt(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=3)
        mydb.drop_table(1, 1, 3)

    def __drop_db_general_stmt(self):
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=4)
        mydb.drop_table(1, 1, 4)


class Remove_DB_Files:

    def remove_db_file():
        mydb = buissnes.Database.Builder.DatabaseOperator(path_num=1, dbnm_num=1, tbl_num=1)
        # zabezpieczenie przed usunięciem, w programie może to być monitorowane komunikatem okienka pop-up proszącym o potiwerdzenie operacji
        mydb.file_destroyer(confirmed=True)


class Format_DB:

    def format_database():
        Drop_DB_Button().drop_database()
        Remove_DB_Files.remove_db_file()
        Build_DB_Button().build_database()

