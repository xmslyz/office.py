import datetime
import BuisnessLayer.Accounts.TaxesComputer as tc
import BuisnessLayer.Employees.Employee as emp
import BuisnessLayer.Database.InsertData as idata
import BuisnessLayer.Database.ScanRecords
import BuisnessLayer.Database.Updater
import GUILayer.SettingsTab.database_settings
import GUILayer.SettingsTab.database_builder
import GUILayer.SettingsTab.database_droper
import GUILayer.SettingsTab.database_remover
import GUILayer.InsertTab.InsertRecord
import GUILayer.InsertTab.UpdateRecord
import GUILayer.ShowDataTab.qaz
import GUILayer.ShowDataTab.wsx
from collections import Counter
import BuisnessLayer.Accounts.TaxesComputer



def main():
    print("Hi World!")
    t1 = datetime.datetime.now()
    # BUDOWA TABEL BAZ DANYCH
    # GUILayer.SettingsTab.database_builder.build_db_intentions()
    # GUILayer.SettingsTab.database_builder.build_db_employees()
    # GUILayer.SettingsTab.database_builder.build_db_collations()
    # USUWANIE TABEL BAZ DANYCH
    # GUILayer.SettingsTab.database_droper.drop_db_intentions()
    # GUILayer.SettingsTab.database_droper.drop_db_employees()
    # GUILayer.SettingsTab.database_droper.drop_db_collations()
    # USUWANIE PLIKÓW BAZ DANYCH
    # GUILayer.SettingsTab.database_remover.remove_db_file()

    # WPROWADZANIE DANYCH DO BAZY DANYCH
    # GUILayer.InsertTab.InsertRecord.insert_mass_records()
    # GUILayer.InsertTab.InsertRecord.add_employee()
    # AKTUALIZACJA KOMÓREK BAZ DANYCH
    # GUILayer.InsertTab.UpdateRecord.update_value()

    # BuisnessLayer.Database.Updater.foroneupdater("2022-10", "PK").update_value()
    # w = BuisnessLayer.Accounts.TaxesComputer.GeneralStmt(1,1,2,"2022-12").
    w = BuisnessLayer.Accounts.TaxesComputer.GeneralStmt(1, 1, 2, "2022-12").sum_taxes_for_employee("bcc31ae3-9f61-4b07-b119-6e8dbf9e9a46")

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
