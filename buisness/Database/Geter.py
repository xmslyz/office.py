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
        super().__init__()

    def get_abreviations(self):
        """Returns list of abreviations"""

        query = self.sql_querry(
            "SELECT abreviation FROM employees WHERE on_duty IS ('1');",
            dblink="employees")
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
        return self.sql_querry(f"SELECT {col} FROM intentions;")

    def get_list_to_pars(self):
        """Returns cualified to recive pars """
        prob = self.sql_querry("SELECT uniqueID FROM employees WHERE "
                               "function IS ('Proboszcz');",
                               dblink="employees")

        wik = self.sql_querry("SELECT uniqueID FROM employees WHERE "
                              "function IS ('Wikary');",
                              dblink="employees")

        return prob, wik

    def search_everything(self, qtype="Stypendium mszalne",
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
        return self.sql_querry(sql_stmt=__sql)


class UniqueIDGetter(Connection):
    def __init__(self):
        super().__init__()
        self.dblink = "employees"

    def get_uniqueID(self, abrev, onduty=1):
        try:
            query = self.sql_querry(
                f"SELECT uniqueID FROM employees "
                f"WHERE abreviation IS '{abrev}' "
                f"AND on_duty IS '{onduty}';", dblink=self.dblink)
            assert len(query) == 1
            return query[0][0] if len(query) == 1 else None
        except IndexError:
            raise Exception("Brak takiego rejestru")

    def get_list_uniqueID_when_on_duty(self):
        """Returns list of actualy working [on_duty] employees"""
        query = self.sql_querry(
            "SELECT uniqueID FROM employees WHERE on_duty IS ('1');",
            dblink=self.dblink)
        uni_list = []
        if (len(query)) != 0:
            for _ in query:
                uni_list.append(_[0])
            return uni_list
        else:
            return []


