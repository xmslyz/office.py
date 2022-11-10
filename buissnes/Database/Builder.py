import gc
import os
import sqlite3
from sqlite3 import Error
import buissnes.Database
import buissnes.Database.AtributesSetter
import buissnes.Database.Geter


class DatabaseOperator:
    def __init__(self, *, path_num, dbnm_num, tbl_num):
        rs = buissnes.Database.AtributesSetter.TableSettings()

        rs.db_path = buissnes.Database.Geter.AtributesGeter.db_path_getter(path_num)
        self.__path = rs.db_path

        rs.db_name = buissnes.Database.Geter.AtributesGeter.db_name_getter(dbnm_num)
        self.__db_name = rs.db_name

        rs.db_table_name = buissnes.Database.Geter.AtributesGeter.db_tablename_getter(tbl_num)
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
        DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def db_general_stmt(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Całościowe zestawienie', " \
                f"monthly_stmt_date TEXT, " \
                f"intention_amount INTEGER, " \
                f"intention_sum REAL, " \
                f"bination_amount INTEGER, " \
                f"bination_sum REAL, " \
                f"pars REAL, " \
                f"pretax REAL, " \
                f"taxes REAL, " \
                f"receival REAL, " \
                f"net REAL);"
        DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def db_monthly_stmt(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Zestawienie', " \
                f"stmt_date TEXT, " \
                f"intention_amount INTEGER, " \
                f"intention_sum REAL, " \
                f"bination_amount INTEGER, " \
                f"bination_sum REAL, " \
                f"pars REAL, " \
                f"pretax REAL, " \
                f"taxes REAL, " \
                f"receival REAL, " \
                f"net REAL);"
        DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def db_employee(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.__table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID TEXT NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Dane osobowe', " \
                f"name TEXT, " \
                f"surname TEXT, " \
                f"shortname TEXT, " \
                f"abreviation TEXT, " \
                f"function TEXT, " \
                f"taxes TEXT," \
                f"on_duty INTEGER DEFAULT 0);"

        DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')

    def drop_table(self, path_NUM, dbn_NUM, tbl_NUM):
        mysql = f'DROP TABLE IF EXISTS {self.__table_name}'
        DatabaseConstructor(path_NUM, dbn_NUM, tbl_NUM).db_constructor(mysql, '')
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


class DBConnector:
    def __init__(self, path_num, dbnm_num, tbl_num):
        dbs = buissnes.Database.AtributesSetter.DBSettings()

        dbs.db_path = buissnes.Database.Geter.AtributesGeter.db_path_getter(path_num)
        self.__path = dbs.db_path

        dbs.db_name = buissnes.Database.Geter.AtributesGeter.db_name_getter(dbnm_num)
        self.__db_name = dbs.db_name

        dbs.db_table_name = buissnes.Database.Geter.AtributesGeter.db_tablename_getter(tbl_num)
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
