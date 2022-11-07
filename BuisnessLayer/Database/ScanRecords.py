import os
import sqlite3
import BuisnessLayer.Database.AtributesSetter
import GUILayer.SettingsTab.database_settings
from BuisnessLayer.Database import Constructor as dbb


class RecordsScanner:
    def __init__(self, path_num, dbnm_num, tbl_num):
        """
        :param path_num: [1] SQLDataBase [2] Constants
        :param dbnm_num: [1] sofa [2] constants
        :param tbl_num:  [1] intentions [2] employees [3] collations [4] constants
        """
        rs = BuisnessLayer.Database.AtributesSetter.TableSettings()

        rs.db_path = GUILayer.SettingsTab.database_settings.db_path_getter(path_num)
        self.__path = rs.db_path

        rs.db_name = GUILayer.SettingsTab.database_settings.db_name_getter(dbnm_num)
        self.__db_name = rs.db_name

        rs.db_table_name = GUILayer.SettingsTab.database_settings.db_tablename_getter(tbl_num)
        self.__table_name = rs.db_table_name

        rs.db_full_path = ''
        self.__full_path = rs.db_full_path

    def __repr__(self):
        return f'RecordScanner:\n\t' \
               f'PATH: {self.__path}\n\t' \
               f'FULL PATH: {self.__full_path}\n\t' \
               f'DATABASE NAME: {self.__db_name}\n\t' \
               f'TABLE NAME: {self.__table_name}\n'

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
        except sqlite3.OperationalError:
            print("No such table. Program will close up now.")
            exit()
        finally:
            self.__close_conection()

    def select_all_where_q_is(self,
                              qtype="Stypendium mszalne",
                              qamount=None,
                              qpriest_reciving=None,
                              qcelebrated_by=None,
                              qcelebration_date=None,
                              qcelebration_hour=None,
                              qcelebration_type=None,
                              qgregorian=None,
                              qfirst_mass=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""
        __sql_sub9 = ""

        if qtype is not None:
            __sql_sub1 = f'type IS "{qtype}"'

        if qamount is not None:
            __sql_sub2 = f' AND amount IS "{qamount}"'

        if qpriest_reciving is not None:
            __sql_sub3 = f' AND priest_reciving IS "{qpriest_reciving}"'

        if qcelebrated_by is not None:
            __sql_sub4 = f' AND celebrated_by IS "{qcelebrated_by}"'

        if qcelebration_date is not None:
            __sql_sub5 = f' AND celebration_date IS "{qcelebration_date}"'

        if qcelebration_hour is not None:
            __sql_sub6 = f' AND celebration_hour IS "{qcelebration_hour}"'

        if qcelebration_type is not None:
            __sql_sub7 = f' AND celebration_type IS "{qcelebration_type}"'

        if qgregorian is not None:
            __sql_sub8 = f' AND gregorian IS "{qgregorian}"'

        if qfirst_mass is not None:
            __sql_sub9 = f' AND first_mass IS "{qfirst_mass}"'

        __sql = f'SELECT * FROM {self.__table_name} ' \
                f'WHERE {__sql_sub1}' \
                f'{__sql_sub2}' \
                f'{__sql_sub3}' \
                f'{__sql_sub4}' \
                f'{__sql_sub5}' \
                f'{__sql_sub6}' \
                f'{__sql_sub7}' \
                f'{__sql_sub8}' \
                f'{__sql_sub9};'
        return self.sql_querry(__sql)

    def select_all_where_q_is_not(self,
                                  qtype="Stypendium mszalne",
                                  qamount=None,
                                  qpriest_reciving=None,
                                  qcelebrated_by=None,
                                  qcelebration_date=None,
                                  qcelebration_hour=None,
                                  qcelebration_type=None,
                                  qgregorian=None,
                                  qfirst_mass=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""
        __sql_sub9 = ""

        if qtype is not None:
            __sql_sub1 = f'type IS "{qtype}"'

        if qamount is not None:
            __sql_sub2 = f' AND amount IS NOT "{qamount}"'

        if qpriest_reciving is not None:
            __sql_sub3 = f' AND priest_reciving IS NOT "{qpriest_reciving}"'

        if qcelebrated_by is not None:
            __sql_sub4 = f' AND celebrated_by IS NOT "{qcelebrated_by}"'

        if qcelebration_date is not None:
            __sql_sub5 = f' AND celebration_date IS NOT "{qcelebration_date}"'

        if qcelebration_hour is not None:
            __sql_sub6 = f' AND celebration_hour IS NOT "{qcelebration_hour}"'

        if qcelebration_type is not None:
            __sql_sub7 = f' AND celebration_type IS NOT "{qcelebration_type}"'

        if qgregorian is not None:
            __sql_sub8 = f' AND gregorian IS NOT "{qgregorian}"'

        if qfirst_mass is not None:
            __sql_sub9 = f' AND first_mass IS NOT "{qfirst_mass}"'

        __sql = f'SELECT * FROM {self.__table_name} ' \
                f'WHERE ' \
                f'{__sql_sub1}' \
                f'{__sql_sub2}' \
                f'{__sql_sub3}' \
                f'{__sql_sub4}' \
                f'{__sql_sub5}' \
                f'{__sql_sub6}' \
                f'{__sql_sub7}' \
                f'{__sql_sub8}' \
                f'{__sql_sub9};'
        return self.sql_querry(__sql)

    def select_all_where_q_like(self,
                                qtype="Stypendium mszalne",
                                qamount=None,
                                qpriest_reciving=None,
                                qcelebrated_by=None,
                                qcelebration_date=None,
                                qcelebration_hour=None,
                                qcelebration_type=None,
                                qgregorian=None,
                                qfirst_mass=None,
                                qid=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""
        __sql_sub9 = ""
        __sql_sub10 = ""

        if qtype is not None:
            __sql_sub1 = f'type IS "{qtype}"'

        if qamount is not None:
            __sql_sub2 = f' AND amount LIKE ("{qamount}")'

        if qpriest_reciving is not None:
            __sql_sub3 = f' AND priest_reciving LIKE ("{qpriest_reciving}")'

        if qcelebrated_by is not None:
            __sql_sub4 = f' AND celebrated_by LIKE ("{qcelebrated_by}")'

        if qcelebration_date is not None:
            __sql_sub5 = f' AND celebration_date LIKE ("{qcelebration_date}")'

        if qcelebration_hour is not None:
            __sql_sub6 = f' AND celebration_hour LIKE ("{qcelebration_hour}")'

        if qcelebration_type is not None:
            __sql_sub7 = f' AND celebration_type LIKE ("{qcelebration_type}")'

        if qgregorian is not None:
            __sql_sub8 = f' AND gregorian LIKE "{qgregorian}"'

        if qfirst_mass is not None:
            __sql_sub9 = f' AND first_mass LIKE ("{qfirst_mass}")'

        if qid is not None:
            __sql_sub10 = f' AND id LIKE ("{qid}")'

        __sql = f'SELECT * FROM {self.__table_name} ' \
                f'WHERE ' \
                f'{__sql_sub1}' \
                f'{__sql_sub2}' \
                f'{__sql_sub3}' \
                f'{__sql_sub4}' \
                f'{__sql_sub5}' \
                f'{__sql_sub6}' \
                f'{__sql_sub7}' \
                f'{__sql_sub8}' \
                f'{__sql_sub9}' \
                f'{__sql_sub10};'
        return self.sql_querry(__sql)

    def left_outer_join(self, val):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "employees"
        mysql3 = f"SELECT * FROM employees LEFT OUTER JOIN collation ON employees.uniqueID = collation.uniqueID WHERE employees.uniqueID IS '{val}';"
        bu = dbb.DBConnector(path, dbname, table_name)
        return bu.create_no_val_connection(mysql3)
        # SELECT * FROM A LEFT OUTER JOIN B A.f = B.f WHERE B.z IS (?)

    def scanby_seletion_key_value(self, *, selection, key, value):
        """
        Join: Triple Inner Join
        :param selection: columns to be returned
        :param key: tablename.columnname
        :param value: str lub boolean
        :return: records WHERE key IS value
        """
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "intentions"

        ssqqll = f"SELECT {selection} FROM intentions " \
                 f"INNER JOIN employees " \
                 f"ON employees.abreviation = intentions.celebrated_by " \
                 f"INNER JOIN collation " \
                 f"ON collation.uniqueID = employees.uniqueID WHERE {key} IS ?;"

        bu = dbb.DBConnector(path, dbname, table_name)
        return bu.create_connection(ssqqll, value)
