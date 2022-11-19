from collections import Counter
from buisness.Database.Filter import Filter


class MonthlyStmtGeter(Filter):
    def __init__(self):
        """
        "monthly_stmt"
        """
        super().__init__()
        # self.query = Filter()
        # self.query.get_conn_details("monthly_stmt")

    def get_monthly_stmt_by_uniqueID(self, when, uniID):
        query = self.sql_querry(
            f"SELECT * FROM monthly_stmt WHERE stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0:
            return query
        else:
            return (),

    def get_general_stmt_by_uniqueID_and_date(self, when, uniID):
        query = self.sql_querry(
            f"SELECT * FROM general_stmt WHERE monthly_stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0 and query is not None:
            return query
        else:
            return (),


class GuestsGetter(Filter):
    def __init__(self):
        """
        "intentions"
        """
        super().__init__()
        # self.query = Filter()
        # self.query.get_conn_details("intentions")

    def get_guests(self, when):
        query = self.sql_querry(f"SELECT * FROM intentions "
                                f"LEFT OUTER JOIN employees "
                                f"ON employees.abreviation = "
                                f"intentions.celebrated_by "
                                f"WHERE intentions.celebration_date "
                                f"LIKE ('{when}-__') and employees.on_duty "
                                f"IS NOT ('1');")
        return list(Counter([x[4] for x in query if x[4] != '']).items())


class IntentionsColsGetter(Filter):
    def __init__(self):
        """
        "employees"
        """
        super().__init__()
        # self.query = Filter()
        # self.query.get_conn_details("employees")

    def get_abreviations(self):
        """ Returns list of abreviations """
        query = self.sql_querry(
            f"SELECT abreviation FROM employees WHERE on_duty IS ('1');")
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []

    def get_all(self):
        """ Returns everything """
        return self.sql_querry(f"SELECT * FROM intentions;")

    def get_one(self, col):
        """ Returns everything from one column """
        return self.sql_querry(f"SELECT {col} FROM intentions;")


class UniqueIDGetter(Filter):
    def __init__(self):
        """
        "employees"
        """
        super().__init__()
        # self.query = Filter()
        # self.query.get_conn_details("employees")

    def get_uniqueID(self, abrev, onduty):
        try:
            query = self.sql_querry(
                f"SELECT uniqueID FROM employees WHERE abreviation IS '{abrev}' AND on_duty IS ('{onduty}');")
            assert len(query) == 1
            return query[0][0] if len(query) == 1 else None
        except:
            raise Exception("Brak takiego rejestru")

    def get_list_uniqueID_when_on_duty(self):
        """ Returns list of actualy working [on_duty] employees """
        query = self.sql_querry(
            f"SELECT uniqueID FROM employees WHERE on_duty IS ('1');")
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []
