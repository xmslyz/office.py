import os
import sqlite3
from Random_Generator import random_values_generator as rvg


class DatabaseFiller:
    def __init__(self, path="Files\\Database\\default.db"):
        self.__path = path
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), self.__path)

    def __open_connection(self):
        self.__con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()

    def __close_conection(self):
        self.__con.commit()
        self.__cur.close()

    def make_connection(self, __meth):
        self.__open_connection()
        __meth()
        self.__close_conection()

    def filler_with_dbObject(self):
        rvl = rvg.random_value_list_generator(0, 10)
        self.__cur.executemany("INSERT INTO main_table VALUES(?, ?, ?, ?, ?, ?)", rvl)
