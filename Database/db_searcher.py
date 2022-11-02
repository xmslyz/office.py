import os
import sqlite3


class DatabaseSearcher:
    def __init__(self, path="Files\\Databases\\default.db"):
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

    def sql_filter(self,
                   qtype="Stypendium mszalne",
                   qamount=None,
                   qpriest_reciving=None,
                   qcelebrated_by=None,
                   qcelebration_date=None,
                   qcelebration_hour=None,
                   qcelebration_type=None,
                   qfirst_mass=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""

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

        if qfirst_mass is not None:
            __sql_sub8 = f' AND first_mass IS "{qfirst_mass}"'

        __sql = f'SELECT * FROM intentions WHERE {__sql_sub1}{__sql_sub2}{__sql_sub3}{__sql_sub4}{__sql_sub5}{__sql_sub6}{__sql_sub7}{__sql_sub8};'
        return self.sql_querry(__sql)

    def sql_not_filter(self,
                       qtype="Stypendium mszalne",
                       qamount=None,
                       qpriest_reciving=None,
                       qcelebrated_by=None,
                       qcelebration_date=None,
                       qcelebration_hour=None,
                       qcelebration_type=None,
                       qfirst_mass=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""

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

        if qfirst_mass is not None:
            __sql_sub8 = f' AND first_mass IS NOT "{qfirst_mass}"'

        __sql = f'SELECT * FROM intentions WHERE {__sql_sub1}{__sql_sub2}{__sql_sub3}{__sql_sub4}{__sql_sub5}{__sql_sub6}{__sql_sub7}{__sql_sub8};'
        return self.sql_querry(__sql)

    def sql_like_filter(self,
                        qtype="Stypendium mszalne",
                        qamount=None,
                        qpriest_reciving=None,
                        qcelebrated_by=None,
                        qcelebration_date=None,
                        qcelebration_hour=None,
                        qcelebration_type=None,
                        qfirst_mass=None):

        __sql_sub1 = ""
        __sql_sub2 = ""
        __sql_sub3 = ""
        __sql_sub4 = ""
        __sql_sub5 = ""
        __sql_sub6 = ""
        __sql_sub7 = ""
        __sql_sub8 = ""

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

        if qfirst_mass is not None:
            __sql_sub8 = f' AND first_mass IS LIKE ("{qfirst_mass}")'

        __sql = f'SELECT * FROM intentions WHERE {__sql_sub1}{__sql_sub2}{__sql_sub3}{__sql_sub4}{__sql_sub5}{__sql_sub6}{__sql_sub7}{__sql_sub8};'
        return self.sql_querry(__sql)
