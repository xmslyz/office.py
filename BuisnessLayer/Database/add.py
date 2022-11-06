import calendar
import datetime
import random
import uuid

import BuisnessLayer.Income.stipend_income
import BuisnessLayer.Database.InsertData
import BuisnessLayer.Employyes.Employee as Emp
from BuisnessLayer.Database.InsertData import StipendEntries as se
from BuisnessLayer.Database.InsertData import PersonalData as pd


def single_record(amount, reciving_priest, celebrating_priest, hour_oc, date_oc, type_of_mass, is_gregorian):
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa.db"
    table_name = "intentions"

    sr = BuisnessLayer.Income.stipend_income.StipendRecord()
    sr.amount = amount
    sr.reciving_priest = reciving_priest
    sr.celebrating_priest = celebrating_priest
    sr.hour_of_celebration = hour_oc
    sr.date_of_celebration = date_oc
    sr.type_of_mass = type_of_mass
    sr.is_gregorian = is_gregorian
    se(path, db_name, table_name).single_entry(sr)


def multiple_record(amount, reciving_priest, celebrating_priest, hour_oc, date_oc, type_of_mass, is_gregorian):
    records = 31
    print(f"Wstawiam {records} wierszy")
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa.db"
    table_name = "intentions"

    mr = BuisnessLayer.Income.stipend_income.StipendRecord()
    mr.amount = amount
    mr.reciving_priest = reciving_priest
    mr.celebrating_priest = celebrating_priest
    mr.hour_of_celebration = hour_oc
    mr.date_of_celebration = date_oc
    mr.type_of_mass = type_of_mass
    mr.is_gregorian = is_gregorian
    se(path, db_name, table_name).compound_entry(val=mr, repeat=records)
    print("Gotowe")


def random_data():  # na potrzeby testów
    amount = random.choice([50, 60, 70, 80, 100])
    reciving_priest = random.choice(["PK", "TO", "DC", "WM", "MS"])
    celebrating_priest = random.choice(["PK", "TO", "DC", "WM", "MS", "SOL"])
    hour_of_celebration = random.choice(["06:30:00", "07:00:00", "18:00:00"])
    date_of_celebration = datetime.datetime.now().strftime("%Y-%m-%d")
    type_of_mass = ""
    is_gregorian = False
    return amount, reciving_priest, celebrating_priest, hour_of_celebration, date_of_celebration, type_of_mass, is_gregorian


def multi_records(amount, reciving_priest, celebrating_priest, hour_oc, date_oc, type_of_mass, is_gregorian):
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa.db"
    table_name = "intentions"

    x = BuisnessLayer.Income.stipend_income.StipendRecord()
    x.amount = amount
    x.reciving_priest = reciving_priest
    x.celebrating_priest = celebrating_priest
    x.hour_of_celebration = hour_oc
    x.date_of_celebration = date_oc
    x.type_of_mass = type_of_mass
    x.is_gregorian = is_gregorian
    se(path, db_name, table_name).single_entry(x)


def add_employee(uniqueID, name, surname, shortname, abreviation, function, taxes):
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa.db"
    table_name = "employees"

    emp = Emp.EmployeeIdentity()
    emp.uniqueID = uniqueID
    emp.name = name
    emp.surname = surname
    emp.shortname = shortname
    emp.abreviation = abreviation
    emp.function = function
    emp.taxes = taxes
    pd(path, db_name, table_name).introduce_new_employee(emp)


def add_cashflow(uniqueID):
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa.db"
    table_name = "collation"
    coll = Emp.EmployeeCollations()
    coll.uniqueID = uniqueID
    coll.collation_date = None
    coll.intention_amount = None
    coll.intention_sum = None
    coll.bination_amount = None
    coll.bination_sum = None
    coll.pars = None
    coll.pretax = None
    coll.taxes = None
    coll.receival = None
    coll.net = None
    pd(path, db_name, table_name).introduce_new_empees_cashflow(coll)


def new_employee(qemployee):
    uuID = uuid.uuid4()
    emp = qemployee

    add_employee(str(uuID), emp[0], emp[1], emp[2], emp[3], emp[4], emp[5])
    add_cashflow(str(uuID))
