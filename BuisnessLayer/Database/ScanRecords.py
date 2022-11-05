import os
import sqlite3


class RecordsScanner:
    def __init__(self, path="DatabaseLayer\\SQLDataBase\\sofa.db"):  # NIE ZAPOMNIJ USUNĄĆ AUTOMATYCZNĄ [PATH!]
        self.table_name = "intentions"
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

        __sql = f'SELECT * FROM {self.table_name} ' \
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

        __sql = f'SELECT * FROM {self.table_name} ' \
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

        __sql = f'SELECT * FROM {self.table_name} ' \
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