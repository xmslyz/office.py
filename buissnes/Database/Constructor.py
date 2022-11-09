import sqlite3
from buissnes.Database.Connector import DBConnector


class DatabaseConstructor(DBConnector):
    def __init__(self, path_num, dbnm_num, tbl_num):
        super().__init__(path_num, dbnm_num, tbl_num)

    def db_constructor(self, sql_stmt, value) -> tuple:
        self.__database_dir_builder()
        self.create_connection(0, sql_stmt, value)

    def __database_dir_builder(self):
        if not self.is_path():  # gdy nie istnieje struktura katalogu
            sqlite3.connect(self.make_path(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        else:
            sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

