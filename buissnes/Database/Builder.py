import gc
import os
import pathlib
import sqlite3
from sqlite3 import Error
from buissnes.Database.SQLConnector import Connection


class DBConnector(Connection):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        print(f'DataBase Connector: {self.__class__.__qualname__}\n\t'
              f'path -> {self.path}\n\t'
              f'dbname -> {self.db_name}\n\t'
              f'table_name -> {self.table_name}\n\t'
              f'full_path -> {self.file_path}\n')

    def is_path(self) -> str:
        db_dir = os.path.join(os.path.abspath(os.getcwd()), self.path)
        return True if os.path.exists(db_dir) else False

    # fpath = 'D:/workspace/python/samplefile.txt'
    # isFile = os.path.isfile(fpath)
    # isDirectory = os.path.isdir(fpath)
    # E:\PycharmProjects\test311\DatabaseLayer\SQLDataBase\pp.py

    def make_path(self):
        db_dir = db_dir = pathlib.PurePath(os.getcwd(), self.path).joinpath()
        # db_dir2 = os.path.join(os.path.abspath(os.getcwd()), self.path)
        os.makedirs(db_dir, mode=0o700, exist_ok=True)
        db_dir = os.path.join(db_dir, self.db_name)
        return db_dir

    def create_connection(self, pin, sql_stmt, val):
        if not self.is_path():
            self.make_path()
        result = ()
        try:
            conn = sqlite3.connect(self.file_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cur = conn.cursor()
            if pin == 0:
                cur.execute(sql_stmt, val)
            elif pin == 1:
                cur.execute(sql_stmt, (val,))
            elif pin == 2:
                cur.executemany(sql_stmt, val)
            else:
                cur.execute(sql_stmt)
            result = cur.fetchall()
            conn.commit()
            cur.close()
        except Error as e:
            print(e)
        return result


class DBCreationStmts(DBConnector):
    def __init__(self):
        super().__init__()

    def db_intentions(self):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.table_name} " \
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
        self.create_connection(0, mysql, '')

    def db_general_stmt(self):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.table_name} " \
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
        self.create_connection(0, mysql, '')

    def db_monthly_stmt(self):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.table_name} " \
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
        self.create_connection(0, mysql, '')

    def db_employee(self):
        mysql = f"CREATE TABLE IF NOT EXISTS {self.table_name} " \
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
        self.create_connection(0, mysql, '')

    def drop_table(self):
        mysql = f'DROP TABLE IF EXISTS {self.table_name}'
        self.sql_querry(mysql)
        gc.collect()

    def file_destroyer(self, *, confirmed):
        if confirmed is True:
            try:
                os.remove(os.path.join(self.file_path)) if os.path.exists(self.file_path) else None
                print("Plik usunięty")
            except PermissionError:
                print("Plik nie może zostać usunięty, ponieważ nie można uzyskać dostępu do pliku.")
        else:
            print("Plik zabezpieczony przed usunięciem")


class DatabaseConstructor(DBConnector):
    def __init__(self):
        super().__init__()

    def db_constructor(self, sql_stmt, value) -> tuple:
        self.__database_dir_builder()
        self.create_connection(0, sql_stmt, value)

    def __database_dir_builder(self):
        if not self.is_path():  # gdy nie istnieje struktura katalogu
            sqlite3.connect(self.make_path(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        else:
            sqlite3.connect(self.file_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
