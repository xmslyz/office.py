from collections import Counter

import buissnes.Database
from buissnes.Database.ScanRecords import Filter


class MonthlyStmtGeter(Filter):
    def __init__(self):
        super().__init__()
        self.query = Filter()
        self.query.get_conn_details(1, 1, 3)

    def get_monthly_stmt_by_uniqueID(self, when, uniID):
        query = self.query.sql_querry(f"SELECT * FROM monthly_stmt WHERE stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0:
            return query[0]
        else:
            return ()

    def get_general_stmt_by_uniqueID_and_date(self, when, uniID):
        query = self.query.sql_querry(f"SELECT * FROM general_stmt WHERE monthly_stmt_date LIKE ('{when}') AND uniqueID IS ('{uniID}');")
        if len(query) > 0 and query is not None:
            return query[0]
        else:
            return ()


class GuestsGetter(Filter):
    def __init__(self):
        super().__init__()
        self.query = Filter()
        self.query.get_conn_details(1, 1, 1)

    def get_guests(self, when):
        guest_list = []
        query = self.query.sql_querry(f"SELECT * FROM intentions LEFT OUTER JOIN employees "
                                      f"ON employees.abreviation = intentions.celebrated_by "
                                      f"WHERE intentions.celebration_date LIKE ('{when}-__');")
        for _ in query:
            if _[10] is None:
                guest_list.append(_[4])
        return list(Counter(guest_list).items())


class IntentionsColsGetter(Filter):
    def __init__(self):
        super().__init__()
        self.query = Filter()
        self.query.get_conn_details(1, 1, 2)

    def get_abreviations(self):
        """ Returns list of abreviations """
        query = self.query.sql_querry(f"SELECT abreviation FROM employees WHERE on_duty IS ('1');")
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []

    def get_all(self):
        """ Returns list of abreviations """
        return self.query.sql_querry(f"SELECT * FROM intentions;")

    def get_one(self, col):
        """ Returns list of abreviations """
        return self.query.sql_querry(f"SELECT {col} FROM intentions;")


class UniqueIDGetter(Filter):
    def __init__(self):
        super().__init__()
        self.query = Filter()
        self.query.get_conn_details(1, 1, 2)

    def get_uniqueID(self, abrev, onduty):
        try:
            query = self.query.sql_querry(f"SELECT uniqueID FROM employees WHERE abreviation IS '{abrev}' AND on_duty IS ('{onduty}');")
            assert len(query) == 1
            return query[0][0] if len(query) == 1 else None
        except:
            print("Brak takiego rejestru")
            return None

    def get_list_uniqueID(self):
        """ Returns list of actualy working [on_duty] employees """
        query = self.query.sql_querry(f"SELECT uniqueID FROM employees WHERE on_duty IS ('1');")
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []


class AtributesGeter:
    def db_path_getter(x):
        if x == 1:
            return "DatabaseLayer\\SQLDataBase\\"
        if x == 2:
            return "DatabaseLayer\\Constants\\"

    def db_name_getter(x):
        if x == 1:
            return "sofa.db"
        if x == 2:
            return "constants.db"
        else:
            return f"{x}.db"

    def db_tablename_getter(x):
        if x == 0:
            return "constants"
        elif x == 1:
            return "intentions"
        elif x == 2:
            return "employees"
        elif x == 3:
            return "monthly_stmt"
        elif x == 4:
            return "general_stmt"
        elif x == 5:
            return "pars"
        elif x == 6:
            return "x"
        elif x == 7:
            return "y"
        else:
            return x

    def constants_getter(const):
        db = buissnes.Database.ScanRecords.Connection()
        db.get_conn_details(2, 2, 0)
        result = 0
        if const == "bin":
            result = db.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
        elif const == "inv":
            result = db.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
        return int(result[0][0])
