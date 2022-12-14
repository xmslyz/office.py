import ast

from buisness.Database.Geter import UniqueIDGetter, IntentionsColsGetter
from buisness.Employee import Identity, ManageEmployee
from buisness.Employee.ManageEmployee import (
    UpdateEmployeeData,
    DeleteEmployeeData,
)


class EmployeeDetails:

    def add_tax(self, uid, tax_name, tax_amount) -> dict:
        actual_taxes = self.__extract_taxes(uid)
        if actual_taxes:
            actual_taxes[tax_name] = tax_amount
            return str(actual_taxes)
        else:
            return str({})

    def __extract_taxes(self, uid):
        return ast.literal_eval(IntentionsColsGetter()
                                 .get_tax_by_uid(uid)[0][0])

    def add_abreviation_sugestion(self):
        # get Name from QT object
        qtName = "Adam"
        # get MiddleName from QT object
        qtMiddleName = "Antoni"
        # get Surname from QT object
        qtSurname = "Adamski"

        return f'{qtName[0].upper()}' \
               f'{qtMiddleName[0].upper()}' \
               f'{qtSurname[0].upper()}'


class TabEmployee:
    def get_employee_data(self):
        # tworzy pusty obiekt rejestru dla księgi intencji
        employee_obj = Identity.EmployeeIdentity()

        # przykładowe dane otrzymane z GUI
        name = "Chichini"
        middlename = ""
        surname = "Bitucco"
        shortname = "BiBio"
        abreviation = "BB"
        function = "Wikarxy"
        taxes = {}  # ??
        on_duty = True

        employee_obj.name = name
        employee_obj.middlename = middlename
        employee_obj.surname = surname
        employee_obj.shortname = shortname
        employee_obj.abreviation = abreviation
        employee_obj.function = function
        employee_obj.taxes = taxes
        employee_obj.is_working = on_duty

        return employee_obj

    def add_new_employee(self):
        employee_obj = self.get_employee_data()
        new_emp = ManageEmployee.NewEmployee()
        new_emp.get_conn_details("employees")
        new_emp.new_employee(employee_obj)

        return None

    def update_employee(self):
        # get employees uniqueID
        get_uid = UniqueIDGetter()
        qid = get_uid.get_uniqueID("BB")

        employee_obj = self.get_employee_data()
        update_emp = UpdateEmployeeData()
        update_emp.get_conn_details("employees")
        update_emp.update_employee(employee_obj, qid)

        return None

    def delete_employee(self):
        # get employees uniqueID
        DeleteEmployeeData().delete_employee(
            UniqueIDGetter().get_uniqueID("AM", 0)
        )

        return None
