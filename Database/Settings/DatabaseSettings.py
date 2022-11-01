import os
import re


class DatabaseSettings:
    def __init__(self):
        self.path = None
        self.dbname = None
        self.table_name = None

    # Wyłączyłem, nie wiem z jakiej przyczyny otrzymuje w konsoli
    # >>> TypeError: 'NoneType' object is not callable
    # @property
    # def __dbname(self):
    #     return self.__dbname
    # @__dbname.setter
    # def __dbname(self, __dbname):
    #     new_dbname = re.sub(r'[^A-Za-z0-9_]+', '', os.__path.splitext(str(__dbname).strip())[0])
    #     self.__dbname = f'{new_dbname}.db'

    def set_dbname(self, dbname):
        new_dbname = re.sub(r'[^A-Za-z0-9_]+', '', os.path.splitext(str(dbname).strip())[0])
        self.dbname = f'{new_dbname}.db'

    def set_path(self, *args):
        new_path = ''
        for arg in args:
            arg = re.sub(r'[^A-Za-z0-9\\_]+', '', os.path.splitext(str(arg).strip())[0])
            new_path += arg + '\\'
        self.path = new_path

    def set_table_name(self, table_name):
        new_table_name = re.sub(r'[^A-Za-z0-9_]+', '', os.path.splitext(str(table_name).strip())[0])
        self.table_name = new_table_name

    def get_dbname(self):
        return self.dbname

    def get_path(self):
        return self.path

    def get_table_name(self):
        return self.table_name

    def get_full_path(self):
        return os.path.join(os.path.abspath(os.getcwd()), self.path, self.dbname)
