import BuisnessLayer.Database.Builder
import BuisnessLayer.Income.stipend_income
import BuisnessLayer.Database.InsertData
import BuisnessLayer.Database.Geter
import BuisnessLayer.Employees.Employee


def insert_mass_records():
    reps = 2  # domyślnie 1. liczba ta określa dla ilu kolejnych dni zapisać w bazie danych daną pozycję.
    # przykładowe dane otrzymane od użytkownika
    amount = 60
    reciving_priest = "AA"
    celebrating_priest = "SOL"
    hour_oc = "07:00:00"
    date_oc = "2022-12-03"
    type_of_mass = ""
    is_gregorian = False

    # tworzy pusty obiekt rejestru dla księgi intencji
    batch = BuisnessLayer.Income.stipend_income.StipendRecord()
    batch.amount = amount
    batch.reciving_priest = reciving_priest
    batch.celebrating_priest = celebrating_priest
    batch.hour_of_celebration = hour_oc
    batch.date_of_celebration = date_oc
    batch.type_of_mass = type_of_mass
    batch.is_gregorian = is_gregorian

    # wrzuca dane z obiektu do tabeli
    stip = BuisnessLayer.Database.InsertData.StipendEntries(1, 1, 1)
    stip.insert_record(val=batch, amount=reps)


def add_employee():
    # przykładowe dane otrzymane z GUI
    name = 'Artur'
    surname = 'Marzec'
    shortname = 'Arturo'
    abreviation = 'AM'
    function = 'Residente'
    taxes = '(230,100.50,50)'

    # tworzy pusty obiekt rejestru dla księgi intencji
    employee = BuisnessLayer.Employees.Employee.EmployeeIdentity()
    employee.name = name
    employee.surname = surname
    employee.shortname = shortname
    employee.abreviation = abreviation
    employee.function = function
    employee.taxes = taxes

    # wrzuca dane z obiektu do tabeli
    empdb = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 2)
    empdb.new_employee(employee)

