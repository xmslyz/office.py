import uuid
import buissnes.Employee.Identity
from buissnes.Database.Builder import DBConnector


class NewEmployee(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

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
        colldb = NewEmployee(1, 1, 3)
        coll = buissnes.Employee.Identity.EmployeeCollations()
        coll.uniqueID = uniqueID
        coll.monthly_stmt = None
        sql_stmt = (f"INSERT INTO {colldb.table_name}"
                    f"(uniqueID, stmt_date) VALUES (?,?);")
        values = (coll.uniqueID,
                  coll.monthly_stmt)
        self.create_connection(0, sql_stmt, values)


class UpdateEmployeeData(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def update_value(self, *, column, value, qid):
        sql_stmt = f"UPDATE {self.table_name} SET {column} = '{value}' WHERE uniqueID IS '{qid}';"
        self.create_no_val_connection(sql_stmt)


class DeleteEmployeeData(DBConnector):
    """
    usuwanie z rejestru
    """
    pass


class RetireEmployee(DBConnector):
    """
    wyłączanie employee z rozliczenia
    """
    pass
