import buissnes.Database
import buissnes.Database.Builder


class Build_DB_Button:
    def build_database(self):
        self.__build_db_intentions()
        self.__build_db_employees()
        self.__build_db_monthly_stmt()
        self.__build_db_general_stmt()

    def __build_db_intentions(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.__repr__()
        mydb.get_conn_details(1, 1, 1)
        mydb.db_intentions()

    def __build_db_employees(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 2)
        mydb.db_employee()

    def __build_db_monthly_stmt(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 3)
        mydb.db_monthly_stmt()

    def __build_db_general_stmt(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 4)
        mydb.db_general_stmt()


class Drop_DB_Button:

    def drop_database(self):
        self.__drop_db_intentions()
        self.__drop_db_employees()
        self.__drop_db_monthly_stmt()
        self.__drop_db_general_stmt()

    def __drop_db_intentions(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 1)
        mydb.drop_table()

    def __drop_db_employees(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 2)
        mydb.drop_table()

    def __drop_db_monthly_stmt(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 3)
        mydb.drop_table()

    def __drop_db_general_stmt(self):
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 4)
        mydb.drop_table()


class Remove_DB_Files:

    def remove_db_file():
        mydb = buissnes.Database.Builder.DBCreationStmts()
        mydb.get_conn_details(1, 1, 1)
        # zabezpieczenie przed usunięciem, w programie może to być monitorowane komunikatem okienka pop-up proszącym o potiwerdzenie operacji
        mydb.file_destroyer(confirmed=True)


class Format_DB:

    def format_database():
        Drop_DB_Button().drop_database()
        Remove_DB_Files.remove_db_file()
        Build_DB_Button().build_database()

