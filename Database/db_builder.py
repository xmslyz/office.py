import os
import sqlite3


class Database:
    def __init__(self, path="Files\\Database\\", dbname="default.db", table_name="main_table"):
        self.path = path
        self.dbname = dbname
        self.table_name = table_name
        self.full_path = os.path.join(os.path.abspath(os.getcwd()), self.path, dbname)

    def show_db_details(self):
        print(f"Tworzenie tabeli {self.table_name} w bazie danych {self.dbname} w katalogu {self.path}.")

    def database_creator(self):
        self.__database_file_builder()
        self.__database_table_builder()

    def __path_finder(self) -> str:
        return True if os.path.exists(self.full_path) else False

    def __path_maker(self) -> str:
        if not self.dbname:
            if not self.path:
                self.path = "Files\\Database\\"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, "default.db")
            return new_dbfile
        else:
            if not self.path:
                self.path = "Files\\Database\\"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, self.dbname)
            return new_dbfile

    def __dbtable_finder(self):
        con = sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        __sql = f'SELECT name FROM sqlite_master WHERE type="table"'
        try:
            for _ in cur.execute(__sql).fetchall():
                return True if _ == (self.table_name,) else False
        finally:
            con.commit()
            cur.close()

    def __database_file_builder(self):
        if not self.__path_finder():  # gdy nie istnieje struktura katalogu
            self.__path_maker()

        dbfile = self.__path_maker()
        sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def __database_table_builder(self):
        con = sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        if self.__dbtable_finder():
            print(f"Tabela o nazwie {self.table_name} już istnieje. Wybierz inną nazwę lub usuń istniejącą.")
        else:
            __sql = f'CREATE TABLE {self.table_name} ' \
                    f'(type TEXT NOT NULL, date DATE, amount REAL, priest_reciving TEXT, celebrated TEXT)'
            try:
                cur.execute(__sql)
            except sqlite3.OperationalError:
                print("Tabela o podanych parametrach już istnieje.")
        con.commit()
        cur.close()
