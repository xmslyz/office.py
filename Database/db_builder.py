import os
import sqlite3

from Database.Settings import DatabaseSettings as dbs


class DatabaseConstructor:
    def __init__(self, db_setup):
        self.__path = db_setup.get_path()
        self.__dbname = db_setup.get_dbname()
        self.__table_name = db_setup.get_table_name()
        self.__full_path = db_setup.get_full_path()

    def db_constructor(self, table_create_vals) -> tuple:
        self.__database_file_builder()
        self.__database_table_builder(table_create_vals)

    def __path_finder(self) -> str:
        return True if os.path.exists(self.__full_path) else False

    def __path_maker(self):
        if not self.__dbname:
            if not self.__path:
                self.__path = "Files\\DatabaseConstructor\\"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.__path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, "default.db")
            return new_dbfile
        else:
            if not self.__path:
                self.__path = "Files\\DatabaseConstructor\\"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.__path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, self.__dbname)
            return new_dbfile

    def __dbtable_finder(self):
        con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        __sql = f'SELECT name FROM sqlite_master WHERE type="table"'
        try:
            for _ in cur.execute(__sql).fetchall():
                return True if _ == (self.__table_name,) else False
        finally:
            con.commit()
            cur.close()

    def __database_file_builder(self):
        if not self.__path_finder():  # gdy nie istnieje struktura katalogu
            self.__path_maker()
            dbfile = self.__path_maker()
            sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def __database_table_builder(self, sql_create_stmt):
        con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        if self.__dbtable_finder():
            print(f"Tabela o nazwie {self.__table_name} już istnieje. Wybierz inną nazwę lub usuń istniejącą.")
        else:
            new_sql_stmt = f'CREATE TABLE {self.__table_name} ('
            comas = len(sql_create_stmt)
            for _ in sql_create_stmt:
                if comas > 1:
                    new_sql_stmt += ', '.join([_[0], ""])
                else:
                    new_sql_stmt += ''.join([_[0], ""])
                comas -= 1
            __sql = new_sql_stmt + ")"
            try:
                cur.execute(__sql)
            except sqlite3.OperationalError:
                print("Tabela o podanych parametrach już istnieje.")
        con.commit()
        cur.close()


class DatabaseBuilder:
    def builder(path, dbname, table_name, sql_stmt):
        """
        Builds ready to use database with its class
        :param path: path in a main catalogue
        :param dbname: database name
        :param table_name: table name
        :param sql_stmt: tuple of tuples : names of columns and its types : ((col1 type), (col2 type))
        """
        seti = dbs.DatabaseSettings()
        seti.set_dbname(dbname)
        seti.set_path(path)
        seti.set_table_name(table_name)

        mydbb = DatabaseConstructor(seti)
        mydbb.db_constructor(sql_stmt)


class DatabaseDestructor:
    def __init__(self, path, dbname, table_name):
        seti = dbs.DatabaseSettings()
        seti.set_dbname(dbname)
        seti.set_path(path)
        seti.set_table_name(table_name)

        self.__dbname = seti.get_dbname()
        self.__path = seti.get_path()
        self.__table_name = seti.get_table_name()
        self.__full_path = seti.get_full_path()

    def database_table_droper(self):
        if os.path.exists(self.__full_path):
            con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cur = con.cursor()
            try:
                __sql = f'DROP TABLE {self.__table_name}'
                cur.execute(__sql)
                print("Tabela usunięta")
            except sqlite3.OperationalError:
                print("Podana tabela nie istnieje.")
            finally:
                con.commit()
                cur.close()

    def file_destroyer(self):
        try:
            os.remove(os.path.join(self.__full_path)) if os.path.exists(self.__full_path) else None
            print("Plik usunięty")
        except PermissionError:
            print("Plik nie może zostać usunięty, ponieważ nie można uzyskać dostępu do pliku.")

    def path_destroyer(self):
        try:
            os.removedirs(self.__path) if os.path.exists(self.__path) else None
            print("Katalog usunięty")
        except PermissionError:
            print("Brak dostępu. Katalog nie może zostać usunięty.")
        except OSError:
            print("Katalog nie jest pusty")


