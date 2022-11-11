import os
import pathlib
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
        new_dbname = re.sub(r'[^A-Z_a-z0-9]+', '', os.path.splitext(str(value).strip().lower())[0])
        self.__dbname = str(pathlib.PurePath(new_dbname).with_suffix(".db"))

    @property
    def db_path(self):
        return self.__path
    @db_path.getter
    def db_path(self):
        return self.__path
    @db_path.setter
    def db_path(self, value) -> str:
        if value == "" or value is None:
            raise Exception("Ścieżka katalogu nie może być pusta")
        dirname = re.sub(r'[^A-Za-z0-9/\\_]+', '', str(value).strip())
        purepath = str(pathlib.PurePath(os.getcwd(), dirname).joinpath())
        self.__path = purepath
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
        if value is None:
            raise Exception("Nazwa tabeli nie może być pusta.")
        new_tblname = re.sub(r'[^A-Z_a-z0-9]+', '', os.path.splitext(str(value).strip().lower())[0])
        self.__table_name = str(pathlib.PurePath(new_tblname))

    @property
    def db_full_path(self):
        return self.__full_path
    @db_full_path.getter
    def db_full_path(self):
        return self.__full_path
    @db_full_path.setter
    def db_full_path(self, x=1):
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), f'{self.__path}\\', self.__dbname)


# class TableSettings(DBSettings):
#     def __init__(self):
#         super().__init__()
#         self.__table_name = None
#
#     @property
#     def db_table_name(self):
#         return self.__table_name
#     @db_table_name.getter
#     def db_table_name(self):
#         return self.__table_name
#     @db_table_name.setter
#     def db_table_name(self, value):
#         if value == "" or value is None:
#             raise Exception("Nazwa bazy danych nie może być pusta.")
#         new_tblname = re.sub(r'[^A-Z_a-z0-9]+', '', os.path.splitext(str(value).strip().lower())[0])
#         self.__table_name = str(pathlib.PurePath(new_tblname))
