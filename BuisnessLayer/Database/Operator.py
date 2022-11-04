import os
import sqlite3
from BuisnessLayer.Database import AtributesSetter as dbs


class DatabaseBuilder:
    def builder(path, dbname, table_name, sql_stmt):
        seti = dbs.DBSettings()
        seti.db_path = path
        seti.db_name = dbname
        seti.db_table_name = table_name
        seti.db_full_path = ""
        mydbb = DatabaseConstructor(seti)
        mydbb.db_constructor(sql_stmt)


class DatabaseConstructor:
    def __init__(self, setup_db):

        self.__path = setup_db.db_path
        self.__dbname = setup_db.db_name
        self.__table_name = setup_db.db_table_name
        self.__full_path = setup_db.db_full_path
        assert self.__path == "DatabaseLayer\\SQLDataBase\\"

    def db_constructor(self, sql_stmt) -> tuple:
        self.__database_file_builder()
        self.__database_stmt_runner(sql_stmt)

    def __path_finder(self) -> str:
        return True if os.path.exists(self.__full_path) else False

    def __path_maker(self):
        new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.__path)
        os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
        new_dbfile = os.path.join(new_dbfile, self.__dbname)
        return new_dbfile

    def __database_file_builder(self):
        if not self.__path_finder():  # gdy nie istnieje struktura katalogu
            sqlite3.connect(self.__path_maker(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        else:
            sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def __database_stmt_runner(self, sql_stmt):
        con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        cur.execute(sql_stmt)
        con.commit()
        cur.close()
