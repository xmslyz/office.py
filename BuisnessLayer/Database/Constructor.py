import sqlite3
from BuisnessLayer.Database.Connector import DBConnector
import BuisnessLayer.Database.AtributesSetter
import PresentationLayer.SettingsTab.database_settings


class DatabaseConstructor(DBConnector):
    def __init__(self, path_num, dbnm_num, tbl_num):
        super().__init__(path_num, dbnm_num, tbl_num)

        dbs = BuisnessLayer.Database.AtributesSetter.DBSettings()

        dbs.db_path = PresentationLayer.SettingsTab.database_settings.db_path_getter(path_num)
        self.__path = dbs.db_path

        dbs.db_name = PresentationLayer.SettingsTab.database_settings.db_name_getter(dbnm_num)
        self.__db_name = dbs.db_name

        dbs.db_table_name = PresentationLayer.SettingsTab.database_settings.db_tablename_getter(tbl_num)
        self.__table_name = dbs.db_table_name

        dbs.db_full_path = ''
        self.__full_path = dbs.db_full_path

    def db_constructor(self, sql_stmt, value) -> tuple:
        self.__database_dir_builder()
        self.create_connection(sql_stmt, value)

    def __database_dir_builder(self):
        if not self.is_path():  # gdy nie istnieje struktura katalogu
            sqlite3.connect(self.make_path(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        else:
            sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

