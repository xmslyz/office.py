import buissnes.Database.InsertData
import buissnes.Employees.Employee


class Button_Add_New_Employee:
    def add_new_employee(self):
        employee_obj = Input_Add_New_Employee.get_new_employee_data()
        buissnes.Database.InsertData.PersonalData(1, 1, 2).new_employee(employee_obj)


class Input_Add_New_Employee:
    def get_new_employee_data():
        # przykładowe dane otrzymane z GUI
        name = 'Arturo'
        surname = 'Marzo'
        shortname = 'Arturito'
        abreviation = 'AM'
        function = 'Residente'
        taxes = '(230,100.50,50)'

        # tworzy pusty obiekt rejestru dla księgi intencji
        employee_obj = buissnes.Employees.Employee.EmployeeIdentity()
        employee_obj.name = name
        employee_obj.surname = surname
        employee_obj.shortname = shortname
        employee_obj.abreviation = abreviation
        employee_obj.function = function
        employee_obj.taxes = taxes

        return employee_obj
