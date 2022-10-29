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

    def sql_querry(self, sql_stmt) -> str:
        """
        Enter valid sql statement.
        :param sql_stmt: sql SELECT_STMT
        :return: cursor.fetchall()
        """
        self.__open_connection()
        try:
            self.__cur.execute(sql_stmt)
            return self.__cur.fetchall()
        finally:
            self.__close_conection()
