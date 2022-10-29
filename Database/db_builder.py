import os
import sqlite3


class Database:
    def __init__(self, path="Files\\Database\\", dbname="default.db", table_name="main_table"):
        self.__path = path
        self.__dbname = dbname
        self.__table_name = table_name
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), self.__path, dbname)

    def show_db_details(self):
        print(f"Tworzenie tabeli {self.__table_name} w bazie danych {self.__dbname} w katalogu {self.__path}.")

    def database_creator(self):
        self.__database_file_builder()
        self.__database_table_builder()

    def __path_finder(self) -> str:
        return True if os.path.exists(self.__full_path) else False

    def __path_maker(self) -> str:
        if not self.__dbname:
            if not self.__path:
                self.__path = "Files\\Database\\"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), self.__path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, "default.db")
            return new_dbfile
        else:
            if not self.__path:
                self.__path = "Files\\Database\\"
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

    def __database_table_builder(self):
        con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        if self.__dbtable_finder():
            print(f"Tabela o nazwie {self.__table_name} już istnieje. Wybierz inną nazwę lub usuń istniejącą.")
        else:
            __sql = f'CREATE TABLE ' \
                    f'{self.__table_name} ' \
                    f'(type TEXT NOT NULL, ' \
                    f'amount REAL, ' \
                    f'priest_reciving TEXT, ' \
                    f'celebrated_by TEXT, ' \
                    f'celebration_date TEXT, ' \
                    f'celebration_hour TEXT, ' \
                    f'celebration_type TEXT, ' \
                    f'first_mass INTEGER)'  # bolean type 0 / 1
            try:
                cur.execute(__sql)
            except sqlite3.OperationalError:
                print("Tabela o podanych parametrach już istnieje.")
        con.commit()
        cur.close()
