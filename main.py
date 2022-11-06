import datetime
import BuisnessLayer.Accounts.TaxesComputer as tc

import BuisnessLayer.Database.InsertData as idata
import PresentationLayer.SettingsTab.database_settings


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()

# dane DB
    path = PresentationLayer.SettingsTab.database_settings.db_path_getter()
    db_name = PresentationLayer.SettingsTab.database_settings.db_name_getter()
    table_name = PresentationLayer.SettingsTab.database_settings.db_tablename_getter(1)

# budowa baz danych i tabel
#     buduj = bdb.PLUG_database_operator()
#     buduj.budowa_bazy_danych_employee()
#     buduj.budowa_bazy_danych_collations()
#     buduj.budowa_bazy_danych_intentions()

# wstawianie pojedynczego rekordu
    # PresentationLayer.SettingsTab.add.single_record(amount="100", reciving_priest="OO",
    #                                          celebrating_priest="PP", hour_oc="13:12:00",
    #                                          date_oc="2022-12-12", type_of_mass="",
    #                                          is_gregorian=False)
# wstawianie wielokrotne rekordów
#     PresentationLayer.SettingsTab.add.multiple_record(amount="100", reciving_priest="OO",
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
#     qe = ("Jan", "Kowalski", "Jasiek", "JK", "Wikariusz", ("100", "180"))
#     PresentationLayer.SettingsTab.add.new_employee(qe)

    taxsum = tc.GeneralStmt(path, db_name, table_name).sum_taxes_for_employee("05879c7f-533f-4305-88ea-83697af554cd")
    idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="taxes", value=taxsum, qid="05879c7f-533f-4305-88ea-83697af554cd")
    idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="collation_date", value="2022-05", qid="05879c7f-533f-4305-88ea-83697af554cd")
    idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="intention_amount", value="12", qid="05879c7f-533f-4305-88ea-83697af554cd")
    idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="intention_sum", value="345.50", qid="05879c7f-533f-4305-88ea-83697af554cd")

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
