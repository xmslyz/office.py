import datetime
import random
import BuisnessLayer.Database.InsertData
import BuisnessLayer.Database.Connector
import BuisnessLayer.Database.Operator
import BuisnessLayer.Database.AtributesSetter
import BuisnessLayer.Income.stipend_income
import BuisnessLayer.Employyes.Employee as emp
import PresentationLayer.temp.add
import PresentationLayer.temp.build as bdb
import PresentationLayer.temp.add as add
import PresentationLayer.temp.print as p


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()

# dane DB
    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa2_db.db"
    table_name = "intentions"

# budowa baz danych i tabel
#     buduj = bdb.PLUG_database_operator()
#     buduj.budowa_bazy_danych_employee()
#     buduj.budowa_bazy_danych_collations()
#     buduj.budowa_bazy_danych_intentions()

# wstawianie pojedynczego rekordu
    # PresentationLayer.temp.add.single_record(amount="100", reciving_priest="OO",
    #                                          celebrating_priest="PP", hour_oc="13:12:00",
    #                                          date_oc="2022-12-12", type_of_mass="",
    #                                          is_gregorian=False)
# wstawianie wielokrotne rekordów
#     PresentationLayer.temp.add.multiple_record(amount="100", reciving_priest="OO",
#                                                celebrating_priest="PP", hour_oc="15:12:00",
#                                                date_oc="2022-12-01", type_of_mass="",
#                                                is_gregorian=False)

# usuwanie tabel
#     buduj = bdb.PLUG_database_operator()
#     buduj.usuniecie_tabeli_list()
#     buduj.usuniecie_tabeli_collations()
#     buduj.usuniecie_tabeli_intentions()

#usuwanie katalogów i plików
    # buduj = bdb.PLUG_database_operator()
    # buduj.file_employee_destroyer()
    # buduj.file_masses_destroyer()

# # RAPORT
# wyrzuca na konsolę wyniki z Bazy Danych
#     p.wydruk_ogolny("2022-12")
#     p.wydruk_osoba("2022-12")
#     print(p.wypis_po_id(qid="6"))


# # DANE OSOBOWE
    t2 = datetime.datetime.now()
    print(t2 - t1)

    PresentationLayer.temp.add.add_employee("Maciek", "Słyż", "Maciek", "MS", "Wikariusz", ("120.67", "10.60", "50"))


if __name__ == '__main__':
    main()
