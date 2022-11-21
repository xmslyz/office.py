from buisness.Database.Geter import UniqueIDGetter
from buisness.Employee import Identity, ManageEmployee
from buisness.Employee.ManageEmployee import (
    UpdateEmployeeData,
    DeleteEmployeeData,
)


class TabEmployee:
    def get_employee_data(self):
        # tworzy pusty obiekt rejestru dla księgi intencji
        employee_obj = Identity.EmployeeIdentity()

        # przykładowe dane otrzymane z GUI
        name = "Chichini"
        surname = "Bitucco"
        shortname = "BiBio"
        abreviation = "BB"
        function = "Wikarxy"
        taxes = {"dziesięcina": "230.00", "dke": "100", "szkoła": "120"}
        on_duty = False

        employee_obj.name = name
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
        qid = get_uid.get_uniqueID("BB", 0)

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
