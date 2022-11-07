import os
import sqlite3
from sqlite3 import Error

import BuisnessLayer.Database.AtributesSetter
import GUILayer.SettingsTab.database_settings


class DBConnector:
    def __init__(self, path_num, dbnm_num, tbl_num):
        dbs = BuisnessLayer.Database.AtributesSetter.DBSettings()

        dbs.db_path = GUILayer.SettingsTab.database_settings.db_path_getter(path_num)
        self.__path = dbs.db_path

        dbs.db_name = GUILayer.SettingsTab.database_settings.db_name_getter(dbnm_num)
        self.__db_name = dbs.db_name

        dbs.db_table_name = GUILayer.SettingsTab.database_settings.db_tablename_getter(tbl_num)
        self.table_name = dbs.db_table_name

        dbs.db_full_path = ''
        self.full_path = dbs.db_full_path

    def __repr__(self):
        print(f'DataBase Connector: {self.__class__.__qualname__}\n\t'
              f'path -> {self.__path}\n\t'
              f'dbname -> {self.__db_name}\n\t'
              f'table_name -> {self.table_name}\n\t'
              f'full_path -> {self.full_path}\n')

    def is_path(self) -> str:
        db_dir = os.path.join(os.path.abspath(os.getcwd()), self.__path)
        return True if os.path.exists(db_dir) else False

    def make_path(self):
        db_dir = os.path.join(os.path.abspath(os.getcwd()), self.__path)
        os.makedirs(db_dir, mode=0o700, exist_ok=True)
        db_dir = os.path.join(db_dir, self.__db_name)
        return db_dir

    def create_connection(self, pin, sql_stmt, val):
        if not self.is_path():
            self.make_path()
        result = ()
        try:
            conn = sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cur = conn.cursor()
            if pin == 0:
                cur.execute(sql_stmt, val)
            elif pin == 1:
                cur.execute(sql_stmt, (val,))
            else:
                cur.execute(sql_stmt)
            result = cur.fetchall()
            conn.commit()
            cur.close()
        except Error as e:
            print(e)
        return result

    def create_no_val_connection(self, sql_stmt):
        if not self.is_path():
            self.make_path()
        result = ()
        try:
            conn = sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cur = conn.cursor()
            cur.execute(sql_stmt)
            result = cur.fetchall()
            conn.commit()
            cur.close()
        except Error as e:
            print(e)
        return result
