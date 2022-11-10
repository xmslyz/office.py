import os
import re


class DBSettings:
    def __init__(self):
        self.__full_path = None
        self.__dbname = None
        self.__path = None
        self.__table_name = None

    @property
    def db_name(self):
        return self.__dbname
    @db_name.getter
    def db_name(self):
        return self.__dbname
    @db_name.setter
    def db_name(self, value):
        if value == "":
            raise Exception("Nazwa bazy danych nie może być pusta.")
        new_dbname = re.sub(r'[^A-Za-z0-9_]+', '', os.path.splitext(str(value).strip())[0])
        self.__dbname = f'{new_dbname}.db'

    @property
    def db_path(self):
        return self.__path
    @db_path.getter
    def db_path(self):
        return self.__path
    @db_path.setter
    def db_path(self, value):
        new_path = re.sub(r'[^A-Za-z0-9\\_]+', '', str(value).strip())
        new_path = new_path.rstrip('\\')
        self.__path = new_path

    @property
    def db_table_name(self):
        return self.__table_name
    @db_table_name.getter
    def db_table_name(self):
        return self.__table_name
    @db_table_name.setter
    def db_table_name(self, value):
        if value == "":
            raise Exception("Nazwa tabeli nie może być pusta.")
        new_table_name = re.sub(r'[^A-Za-z0-9_]+', '', os.path.splitext(str(value).strip())[0])
        self.__table_name = new_table_name

    @property
    def db_full_path(self):
        return self.__full_path
    @db_full_path.getter
    def db_full_path(self):
        return self.__full_path
    @db_full_path.setter
    def db_full_path(self, x=1):
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), f'{self.__path}\\', self.__dbname)


class TableSettings(DBSettings):
    def __init__(self):
        super().__init__()
        self.__table_name = None

    @property
    def db_table_name(self):
        return self.__table_name
    @db_table_name.getter
    def db_table_name(self):
        return self.__table_name
    @db_table_name.setter
    def db_table_name(self, value):
        new_table_name = re.sub(r'[^A-Za-z0-9_]+', '', os.path.splitext(str(value).strip())[0])
        self.__table_name = new_table_name
