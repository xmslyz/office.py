from buisness.Database.SQLConnector import Connection
from buisness.Database.Geter import IntentionsColsGetter as icget


class IntentionsFilter:
    def __init__(self):
        self.conn = Connection()
        self.conn.get_conn_details(dblink="intentions")

    def filter_who_notcelebrated_today(self, celebration_date):
        """
        Searches for a list of employees who not celebrated in given date.

        :param celebration_date:
        :return: list
        """

        employees = icget().get_abreviations()
        when = icget.search_everything(self.conn,
                                       qcelebration_date=celebration_date)

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
