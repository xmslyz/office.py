import datetime
import BuisnessLayer.Accounts.TaxesComputer as tc
import BuisnessLayer.Employees.Employee as emp
import BuisnessLayer.Database.InsertData as idata
import BuisnessLayer.Database.ScanRecords
import GUILayer.SettingsTab.database_settings
import GUILayer.SettingsTab.database_builder
import GUILayer.SettingsTab.database_droper
import GUILayer.SettingsTab.database_remover
import GUILayer.InsertTab.InsertRecord
import GUILayer.InsertTab.UpdateRecord


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()
    # GUILayer.SettingsTab.database_builder.build_db_intentions()
    # GUILayer.SettingsTab.database_builder.build_db_employees()
    # GUILayer.SettingsTab.database_builder.build_db_collations()

    # GUILayer.SettingsTab.database_droper.drop_db_intentions()
    # GUILayer.SettingsTab.database_droper.drop_db_employees()
    # GUILayer.SettingsTab.database_droper.drop_db_collations()

    # GUILayer.SettingsTab.database_remover.remove_db_file()

    # GUILayer.InsertTab.InsertRecord.insert_mass_records()
    # GUILayer.InsertTab.InsertRecord.add_employee()

    # GUILayer.InsertTab.UpdateRecord.update_value()




#

# budowa baz danych i tabel


# wstawianie pojedynczego rekordu
    # GUILayer.SettingsTab.add.single_record(amount="100", reciving_priest="OO",
    #                                          celebrating_priest="PP", hour_oc="13:12:00",
    #                                          date_oc="2022-12-12", type_of_mass="",
    #                                          is_gregorian=False)
# wstawianie wielokrotne rekordów
#     GUILayer.SettingsTab.add.multiple_record(amount="100", reciving_priest="OO",
#                                                celebrating_priest="PP", hour_oc="15:12:00",
#                                                date_oc="2022-12-01", type_of_mass="",
#                                                is_gregorian=False)

# usuwanie tabel
#     buduj = bdb.DatabaseOperator()
#     buduj.drop_employees()
#     buduj.drop_collations()
#     buduj.usuniecie_tabeli_intentions()

#usuwanie katalogów i plików
    # buduj = bdb.DatabaseOperator()
    # buduj.file_employee_destroyer()
    # buduj.file_masses_destroyer()

# # RAPORT
# wyrzuca na konsolę wyniki z Bazy Danych
#     p.wydruk_ogolny("2022-12")
#     p.wydruk_osoba("2022-12")
#     print(p.wypis_po_id(qid="6"))

# # DANE OSOBOWE
#

    # taxsum = tc.GeneralStmt(path, db_name, table_name).sum_taxes_for_employee("05879c7f-533f-4305-88ea-83697af554cd")
    # idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="taxes", value=taxsum, qid="05879c7f-533f-4305-88ea-83697af554cd")
    # idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="collation_date", value="2022-05", qid="05879c7f-533f-4305-88ea-83697af554cd")
    # idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="intention_amount", value="12", qid="05879c7f-533f-4305-88ea-83697af554cd")
    # idata.PersonalData(path, db_name, table_name).insert_value_to_collations(column="intention_sum", value="345.50", qid="05879c7f-533f-4305-88ea-83697af554cd")

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
