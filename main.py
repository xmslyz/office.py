import datetime
import random

import BuisnessLayer.Database.InsertData
import BuisnessLayer.Database.Connector
import BuisnessLayer.Database.Operator
import BuisnessLayer.Database.AtributesSetter
import BuisnessLayer.Income.stipend_income
import PresentationLayer.temp.add
import PresentationLayer.temp.build as bdb
import PresentationLayer.temp.add as add
import PresentationLayer.temp.print as p


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()

    path = "DatabaseLayer\\SQLDataBase\\"
    db_name = "sofa2_db.db"
    table_name = "intentions"

    buduj = bdb.PLUG_database_operator()
    buduj.budowa_bazy_danych_employee()
    buduj.budowa_bazy_danych_collations()
    buduj.budowa_bazy_danych_intentions()

    # PresentationLayer.temp.add.single_record(amount="100", reciving_priest="OO",
    #                                          celebrating_priest="PP", hour_oc="13:12:00",
    #                                          date_oc="2022-12-12", type_of_mass="",
    #                                          is_gregorian=False)

    PresentationLayer.temp.add.multiple_record(amount="100", reciving_priest="OO",
                                               celebrating_priest="PP", hour_oc="15:12:00",
                                               date_oc="2022-12-12", type_of_mass="",
                                               is_gregorian=False)

    # buduj.usuniecie_tabeli_list()
    # buduj.usuniecie_tabeli_collations()
    # buduj.usuniecie_tabeli_intentions()

    # buduj.file_employee_destroyer()
    # buduj.file_masses_destroyer()

    # wyrzuca na konsolę wyniki z DB
    # p.wydruk_ogolny()
    # p.wydruk_osoba()
    # p.wypis_po_id(qid="12106")

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
