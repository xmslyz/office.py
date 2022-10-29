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

    def filler_with_dbObject(self, begin_range_with, end_range_with):
        self.__open_connection()
        rvl = rvg.random_value_list_generator(begin_range_with, end_range_with)
        self.__cur.executemany("INSERT INTO main_table VALUES(?, ?, ?, ?, ?, ?, ?, ?)", rvl)
        self.__close_conection()
