from collections import Counter
from buisness.Database.SQLConnector import Connection


class GuestsGetter(Connection):
    def __init__(self):
        """
        "intentions"
        """
        super().__init__()

    def get_guests(self, when):
        query = self.sql_querry(
            f"SELECT * FROM intentions "
            f"LEFT OUTER JOIN employees "
            f"ON employees.abreviation = "
            f"intentions.celebrated_by "
            f"WHERE intentions.celebration_date "
            f"LIKE ('{when}-__') and employees.on_duty "
            f"IS NOT ('1');"
        )
        return list(Counter([x[4] for x in query if x[4] != ""]).items())


class IntentionsColsGetter(Connection):
    def __init__(self):
        """
        "employees"
        """
        super().__init__()

    def get_abreviations(self):
        """Returns list of abreviations"""
        query = self.sql_querry(
            "SELECT abreviation FROM employees WHERE on_duty IS ('1');"
        )
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []

    def get_all(self):
        """Returns everything"""
        return self.sql_querry("SELECT * FROM intentions;")

    def get_one(self, col):
        """Returns everything from one column"""
        return self.sql_querry("SELECT {col} FROM intentions;")


class UniqueIDGetter(Connection):
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
                f"SELECT uniqueID FROM employees WHERE abreviation IS '{abrev}' AND on_duty IS ('{onduty}');"
            )
            assert len(query) == 1
            return query[0][0] if len(query) == 1 else None
        except:
            raise Exception("Brak takiego rejestru")

    def get_list_uniqueID_when_on_duty(self):
        """Returns list of actualy working [on_duty] employees"""
        query = self.sql_querry(
            "SELECT uniqueID FROM employees WHERE on_duty IS ('1');"
        )
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []
