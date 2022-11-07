import gc
import os

import BuisnessLayer.Database.AtributesSetter
import PresentationLayer.SettingsTab.database_settings
from BuisnessLayer.Database import Constructor as dbb, AtributesSetter as dbs


class PLUG_database_operator:
    def __init__(self, *, path_num, dbnm_num, tbl_num):
        """
        :param path_num: [1] SQLDataBase [2] Constants
        :param dbnm_num: [1] sofa [2] constants
        :param tbl_num:  [1] intentions [2] employees [3] collations [4] constants
        """
        rs = BuisnessLayer.Database.AtributesSetter.TableSettings()

        rs.db_path = PresentationLayer.SettingsTab.database_settings.db_path_getter(path_num)
        self.__path = rs.db_path

        rs.db_name = PresentationLayer.SettingsTab.database_settings.db_name_getter(dbnm_num)
        self.__db_name = rs.db_name

        rs.db_table_name = PresentationLayer.SettingsTab.database_settings.db_tablename_getter(tbl_num)
        self.__table_name = rs.db_table_name

        rs.db_full_path = ''
        self.__full_path = rs.db_full_path

    def __repr__(self):
        return f'PLUG_database_operator:\n\t' \
               f'PATH: {self.__path}\n\t' \
               f'FULL PATH: {self.__full_path}\n\t' \
               f'DATABASE NAME: {self.__db_name}\n\t' \
               f'TABLE NAME: {self.__table_name}\n'

    def db_intentions(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"type TEXT NOT NULL DEFAULT 'Stypendium mszalne', " \
                f"amount REAL DEFAULT 0," \
                f"priest_reciving TEXT," \
                f"celebrated_by TEXT," \
                f"celebration_date TEXT," \
                f"celebration_hour TEXT," \
                f"celebration_type TEXT," \
                f"gregorian INTEGER DEFAULT 0," \
                f"first_mass INTEGER DEFAULT 1);"
        dbb.DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def db_collations(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Zestawienie', " \
                f"collation_date TEXT, " \
                f"intention_amount INTEGER, " \
                f"intention_sum REAL, " \
                f"bination_amount INTEGER, " \
                f"bination_sum REAL, " \
                f"pars REAL, " \
                f"pretax REAL, " \
                f"taxes REAL, " \
                f"receival REAL, " \
                f"net REAL);"
        dbb.DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def db_employee(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Dane osobowe', " \
                f"name TEXT, " \
                f"surname TEXT, " \
                f"shortname TEXT, " \
                f"abreviation TEXT, " \
                f"function TEXT, " \
                f"taxes TEXT);"
        dbb.DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def drop_table(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f'DROP TABLE IF EXISTS {self.__table_name}'
        dbb.DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')
        gc.collect()

    def file_destroyer(self, *, confirmed):
        if confirmed is True:
            try:
                os.remove(os.path.join(self.__full_path)) if os.path.exists(self.__full_path) else None
                print("Plik usunięty")
            except PermissionError:
                print("Plik nie może zostać usunięty, ponieważ nie można uzyskać dostępu do pliku.")
        else:
            print("Plik zabezpieczony przed usunięciem")


