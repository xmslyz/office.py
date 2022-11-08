from collections import Counter

from BuisnessLayer.Database.ScanRecords import RecordsScanner


class MonthlyStmtGeter(RecordsScanner):
    def __init__(self, path_num, dbnm_num, tbl_num):
        super().__init__(path_num, dbnm_num, tbl_num)

    def get_monthly_stmt_by_uniqueID(self, when, uniID):
        query = self.sql_querry(f"SELECT * FROM monthly_stmt WHERE stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0:
            return query[0]
        else:
            return ()

    def get_general_stmt_by_uniqueID_and_date(self, when, uniID):
        query = self.sql_querry(f"SELECT * FROM general_stmt WHERE monthly_stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0 and query is not None:
            return query[0]
        else:
            return ()


class GuestsGetter(RecordsScanner):

    def __init__(self, path_num, dbnm_num, tbl_num):
        super().__init__(path_num, dbnm_num, tbl_num)

    def get_guests(self, when):
        guest_list = []
        query = self.sql_querry(f"SELECT * FROM intentions LEFT OUTER JOIN employees "
                                f"ON employees.abreviation = intentions.celebrated_by "
                                f"WHERE intentions.celebration_date LIKE ('{when}-__');")
        for _ in query:
            if _[10] is None:
                guest_list.append(_[4])
        return list(Counter(guest_list).items())


class UniqueIDGetter(RecordsScanner):

    def __init__(self, path_num, dbnm_num, tbl_num):
        super().__init__(path_num, dbnm_num, tbl_num)

    def get_uniqueID(self, abrev, onduty):
        try:
            query = self.sql_querry(f"SELECT uniqueID FROM employees WHERE abreviation IS '{abrev}' AND on_duty IS ('{onduty}');")
            assert len(query) == 1
            return query[0][0] if len(query) == 1 else None
        except:
            print("Brak takiego rejestru")
            return None

    def get_list_uniqueID(self):
        """ Returns list of actualy working [on_duty] employees """
        query = self.sql_querry(f"SELECT uniqueID FROM employees WHERE on_duty IS ('1');")
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []
