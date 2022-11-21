from buisness.Database.SQLConnector import Connection
from buisness.Database.Geter import IntentionsColsGetter as icget


class IntentionsFilter:
    def __init__(self):
        self.conn = Connection()
        self.conn.get_conn_details(dblink="intentions")

    def combo_filter(self,
                     qtype="Stypendium mszalne",
                     qamount=None,
                     qpriest_reciving=None,
                     qcelebrated_by=None,
                     qcelebration_date=None,
                     qcelebration_hour=None,
                     qcelebration_type=None,
                     qgregorian=None,
                     qfirst_mass=None):

        __sql_sub1 = \
            __sql_sub2 = \
            __sql_sub3 = \
            __sql_sub4 = \
            __sql_sub5 = \
            __sql_sub6 = \
            __sql_sub7 = \
            __sql_sub8 = \
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

        __sql = f'SELECT * FROM intentions ' \
                f'WHERE {__sql_sub1}' \
                f'{__sql_sub2}' \
                f'{__sql_sub3}' \
                f'{__sql_sub4}' \
                f'{__sql_sub5}' \
                f'{__sql_sub6}' \
                f'{__sql_sub7}' \
                f'{__sql_sub8}' \
                f'{__sql_sub9};'
        return self.conn.sql_querry(sql_stmt=__sql)

    def filter_who_notcelebrated_today(self, celebration_date):
        """
        Searches for a list of employees who not celebrated in given date.

        :param celebration_date:
        :return: list
        """

        employees = icget().get_abreviations()
        when = self.combo_filter(qcelebration_date=celebration_date)

        try:
            celebrated = [x[4] for x in when]

            res = [x for x in employees + celebrated
                   if x not in employees
                   or x not in celebrated
                   ]

        except ValueError:
            raise Exception("")

        if not res:
            return None
        else:
            return res

    def clear_filters(self):
        pass
