import uuid
from buisness.Database.Builder import DBConnector
from buisness.Database.SQLConnector import Connection


class NewEmployee(DBConnector):
    def __init__(self):
        super().__init__()

    def new_employee(self, employee):
        uniqueID = str(uuid.uuid4())
        employee.uniqueID = uniqueID
        self.__insert_new_employee(employee)

    def __insert_new_employee(self, val):
        sql_stmt = (
            f"INSERT INTO {self.table_name} "
            f"(uniqueID,"
            f"type,"
            f"name,"
            f"surname,"
            f"shortname,"
            f"abreviation,"
            f"function,"
            f"taxes,"
            f"on_duty) "
            f"VALUES (?,?,?,?,?,?,?,?,?);"
        )
        values = (
            val.uniqueID,
            val.type,
            val.name,
            val.surname,
            val.shortname,
            val.abreviation,
            val.function,
            val.taxes,
            val.is_working
        )
        self.create_connection(0, sql_stmt, values)
        return val


class UpdateEmployeeData(Connection):
    def __init__(self):
        super().__init__()

    def update_employee(self, val, qid):

        sql_stmt = (
            f"UPDATE employees "
            f"SET "
            f"type = '{val.type}', "
            f"name = '{val.name}', "
            f"surname = '{val.surname}', "
            f"shortname = '{val.shortname}', "
            f"abreviation = '{val.abreviation}', "
            f"function = '{val.function}', "
            # f"taxes = '{val.taxes}' "
            f"on_duty = {val.is_working} "
            f"WHERE uniqueID IS '{qid}';"
        )
        print(sql_stmt)
        self.sql_querry(sql_stmt, dblink="employees")

        return None


class DeleteEmployeeData(Connection):
    """
    usuwanie z rejestru
    """
    def delete_employee(self, qid):
        sql_stmt = f"DELETE FROM employees WHERE uniqueID IS '{qid}';"
        self.sql_querry(sql_stmt, dblink="employees")


class RetireEmployee(Connection):
    """
    wyłączanie employee z rozliczenia
    """

    pass
