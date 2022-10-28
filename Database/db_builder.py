import os
import sqlite3
from MSGs import PopupMsgs as msg


class BazaDanych:
    def __init__(self, path="Database\\database\\", dbname=None, table_name="default.db"):
        self.path = path
        self.dbname = dbname
        self.table_name = table_name

    def database_builder(self):
        if not path_finder(self):  # gdy nie istnieje struktura katalogu
            path_maker(self)

        dbfile = path_maker(self)
        sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

    def path_maker(self) -> str:
        if not dbfile:
            if not path:
                path = "Database\\database"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, "default.db")
            return new_dbfile
        else:
            if not path:
                path = "Database\\database"
            new_dbfile = os.path.join(os.path.abspath(os.getcwd()), path)
            os.makedirs(new_dbfile, mode=0o700, exist_ok=True)
            new_dbfile = os.path.join(new_dbfile, dbfile)
            return new_dbfile


def database_table_builder(tablename="table_1", dbfile=None, path=()):



    """ Problem z kontrolą wyjątków """
    if not dbfile:
        dbfile = "default.db"

    if not path:
        path = os.path.join(os.path.abspath(os.getcwd()), "Database\\database\\")

    if os.path.exists(path):
        new_dbfile = os.path.join(path, dbfile)
        con = sqlite3.connect(new_dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        __sql = f'CREATE TABLE IF NOT EXISTS {tablename} ' \
                f'(type TEXT NOT NULL, date DATE, amount REAL, priest_reciving TEXT, celebrated TEXT)'
        try:
            msg.PopupMsgs.popup_msg("Okienko", "Tabela już istnieje w tym miejscu") \
                if is_table_in_db(new_dbfile) \
                else msg.PopupMsgs.popup_msg("Okienko", "Tabela została utworzona")
            cur.execute(__sql)
        except sqlite3.OperationalError:
            msg.PopupMsgs.popup_msg("Wyjątek", "Tabela bazy danych już istnieje, bądź jest otwarta")
        finally:
            con.commit()
            cur.close()


def path_finder(path) -> str:
    new_path = os.path.join(os.path.abspath(os.getcwd()), path)
    return True if os.path.exists(new_path) else False


def dbtable_finder(path, dbfile, tablename):
    con = sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = con.cursor()
    __sql = f'SELECT name FROM sqlite_master WHERE type="table" AND name={tablename}'
    try:
        if cur.execute(__sql).fetchone() is not None:
            return True
        else:
            return False
    finally:
        con.commit()
        cur.close()





def database_eraser(dbfile=None):
    pass
    # dbfile = os.path.abspath(dbfile)
    # con = sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    # cur = con.cursor()
    # try:
    #     cur.execute('DROP TABLE test')
    #     msg.PopupMsgs.popup_msg("Sukces", "Tabela bazy danych została usunięta")
    # except:
    #     msg.PopupMsgs.popup_msg("Błąd", "Nie ma takiej tabeli w bazie danch")
    # finally:
    #     con.commit()
    #     cur.close()
