import uuid
import buissnes.Employee.Identity
from buissnes.Database.Builder import DBConnector
from buissnes.Database.SQLConnector import Connection


class NewEmployee(DBConnector):
    def __init__(self):
        super().__init__()

    def new_employee(self, employee):
        uniqueID = str(uuid.uuid4())
        employee.uniqueID = uniqueID
        self.__insert_new_employee(employee)
        self.__insert_new_monthly_stmt(uniqueID)

    def __insert_new_employee(self, val):
        sql_stmt = (f"INSERT INTO {self.table_name} "
                    f"(uniqueID,type,name,surname,shortname,abreviation,function,taxes) "
                    f"VALUES (?,?,?,?,?,?,?,?);")
        values = (val.uniqueID,
                  val.type,
                  val.name,
                  val.surname,
                  val.shortname,
                  val.abreviation,
                  val.function,
                  val.taxes)
        self.create_connection(0, sql_stmt, values)
        return val

    def __insert_new_monthly_stmt(self, uniqueID):
        colldb = NewEmployee()
        colldb.get_conn_details("monthly_stmt")
        coll = buissnes.Employee.Identity.EmployeeCollations()
        coll.uniqueID = uniqueID
        coll.monthly_stmt = None
        sql_stmt = (f"INSERT INTO {colldb.table_name}"
                    f"(uniqueID, stmt_date) VALUES (?,?);")
        values = (coll.uniqueID,
                  coll.monthly_stmt)
        self.create_connection(0, sql_stmt, values)


class UpdateEmployeeData(Connection):
    def __init__(self):
        super().__init__()

    def update_value(self, *, column, value, qid):
        sql_stmt = f"UPDATE {self.table_name} SET {column} = '{value}' WHERE uniqueID IS '{qid}';"
        self.sql_querry(sql_stmt)


class DeleteEmployeeData(Connection):
    """
    usuwanie z rejestru
    """
    pass


class RetireEmployee(Connection):
    """
    wyłączanie employee z rozliczenia
    """
    pass
