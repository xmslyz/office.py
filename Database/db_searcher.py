import os
import sqlite3


class DatabaseSearcher:
    def __init__(self, path="Files\\Database\\default.db"):
        self.__path = path
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), self.__path)

    def __open_connection(self):
        self.__con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()

    def __close_conection(self):
        self.__con.commit()
        self.__cur.close()

    def make_connection(self, __meth, *args):
        self.__open_connection()
        __meth(*args)
        self.__close_conection()

    def sql_querry_SELECT__FROM__WHERE__IS__(self, column_to_select, table, column_to_lookfor, querry):
        # zwraca listę przyjętych ofiar za msze przez konkretnego ks.
        __sql = f"SELECT {column_to_select} FROM {table} WHERE {column_to_lookfor} IS '{querry}'"
        for row in self.__cur.execute(__sql):
            print(sum(row))
