from buisness.Database.SQLConnector import Connection


class Filter(Connection):
    def __init__(self):
        super().__init__()

    def select_all_where_q_is(self, qtype="Stypendium mszalne",
                              qamount=None, qpriest_reciving=None,
                              qcelebrated_by=None, qcelebration_date=None,
                              qcelebration_hour=None, qcelebration_type=None,
                              qgregorian=None, qfirst_mass=None):

        __sql_sub1 = __sql_sub2 = __sql_sub3 = __sql_sub4 = __sql_sub5 = \
            __sql_sub6 = __sql_sub7 = __sql_sub8 = __sql_sub9 = ""

        if qtype is not None: __sql_sub1 = \
            f'type IS "{qtype}"'
        if qamount is not None: __sql_sub2 = \
            f' AND amount IS "{qamount}"'
        if qpriest_reciving is not None: __sql_sub3 = \
            f' AND priest_reciving IS "{qpriest_reciving}"'
        if qcelebrated_by is not None: __sql_sub4 = \
            f' AND celebrated_by IS "{qcelebrated_by}"'
        if qcelebration_date is not None: __sql_sub5 = \
            f' AND celebration_date IS "{qcelebration_date}"'
        if qcelebration_hour is not None: __sql_sub6 = \
            f' AND celebration_hour IS "{qcelebration_hour}"'
        if qcelebration_type is not None: __sql_sub7 = \
            f' AND celebration_type IS "{qcelebration_type}"'
        if qgregorian is not None: __sql_sub8 = \
            f' AND gregorian IS "{qgregorian}"'
        if qfirst_mass is not None: __sql_sub9 = \
            f' AND first_mass IS "{qfirst_mass}"'

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

    def select_all_where_q_is_not(self, qtype="Stypendium mszalne",
                                  qamount=None, qpriest_reciving=None,
                                  qcelebrated_by=None, qcelebration_date=None,
                                  qcelebration_hour=None,
                                  qcelebration_type=None, qgregorian=None,
                                  qfirst_mass=None):

        __sql_sub1 = __sql_sub2 = __sql_sub3 = __sql_sub4 = __sql_sub5 = \
            __sql_sub6 = __sql_sub7 = __sql_sub8 = __sql_sub9 = ""

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

    def select_all_where_q_like(self, qtype="Stypendium mszalne", qamount=None,
                                qpriest_reciving=None, qcelebrated_by=None,
                                qcelebration_date=None,
                                qcelebration_hour=None, qcelebration_type=None,
                                qgregorian=None, qfirst_mass=None, qid=None):

        __sql_sub1 = __sql_sub2 = __sql_sub3 = __sql_sub4 = \
            __sql_sub5 = __sql_sub6 = __sql_sub7 = __sql_sub8 = \
            __sql_sub9 = __sql_sub10 = ""

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

    def search_employees_by_uniqueID(self, val):
        mysql3 = f"SELECT * FROM employees LEFT OUTER JOIN monthly_stmt " \
                 f"ON employees.uniqueID = monthly_stmt.uniqueID WHERE " \
                 f"employees.uniqueID IS '{val}';"
        self.sql_querry(mysql3)
