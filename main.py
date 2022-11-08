import datetime

# import BuisnessLayer.Accounts.TaxesComputer as tc
# import BuisnessLayer.Employees.Employee as emp
import BuisnessLayer.Database.InsertData
# import BuisnessLayer.Database.ScanRecords
import BuisnessLayer.Database.Geter
import BuisnessLayer.Database.Updater  # ->
# import GUILayer.SettingsTab.database_settings
import GUILayer.SettingsTab.database_builder
# import GUILayer.SettingsTab.database_droper
# import GUILayer.SettingsTab.database_remover
import GUILayer.InsertTab.InsertRecord
# import GUILayer.InsertTab.UpdateRecord
# import GUILayer.ShowDataTab.qaz
# import GUILayer.ShowDataTab.wsx
# from collections import Counter
# import BuisnessLayer.Accounts.TaxesComputer


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()
    # BUDOWA TABEL BAZ DANYCH
    # GUILayer.SettingsTab.database_builder.build_db_intentions()
    # GUILayer.SettingsTab.database_builder.build_db_employees()
    # GUILayer.SettingsTab.database_builder.build_db_monthly_stmt()
    GUILayer.SettingsTab.database_builder.build_db_general_stmt()
    # USUWANIE TABEL BAZ DANYCH
    # GUILayer.SettingsTab.database_droper.drop_db_intentions()
    # GUILayer.SettingsTab.database_droper.drop_db_employees()
    # GUILayer.SettingsTab.database_droper.drop_db_monthly_stmt()
    # USUWANIE PLIKÓW BAZ DANYCH
    # GUILayer.SettingsTab.database_remover.remove_db_file()

    # WPROWADZANIE DANYCH DO BAZY DANYCH
    # GUILayer.InsertTab.InsertRecord.insert_mass_records()
    # GUILayer.InsertTab.InsertRecord.add_employee()
    # AKTUALIZACJA KOMÓREK BAZ DANYCH
    # GUILayer.InsertTab.UpdateRecord.update_value()

    # AKTUALIZACJA DANYCH W monthly_stmt
    # empList = ['PK', 'TO', 'DC', 'WM', 'MS', 'SO']
    # for _ in empList:
    #     BuisnessLayer.Database.Updater.foroneupdater("2022-10", _).update_value()

    # BuisnessLayer.Database.Updater.foroneupdater("2022-10", "SO").update_value()
    #
    # print(BuisnessLayer.Database.Geter.GuestsGetter(1, 1, 1).get_guests("2022-10"))

    li = BuisnessLayer.Database.Geter.UniqueIDGetter(1, 1, 2).get_list_uniqueID()
    for _ in li:
        BuisnessLayer.Database.InsertData.GeneralStmt(1, 1, 4).insert_monthly_stmt("2022-10", _)

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
