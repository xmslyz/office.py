import sqlite3
from BuisnessLayer.Database.Connector import DBConnector


class DatabaseConstructor(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def db_constructor(self, sql_stmt, value) -> tuple:
        self.__database_dir_builder()
        self.create_connection(sql_stmt, value)

    def __database_dir_builder(self):
        if not self.is_path():  # gdy nie istnieje struktura katalogu
            sqlite3.connect(self.make_path(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        else:
            sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

