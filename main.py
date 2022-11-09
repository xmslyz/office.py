import datetime
import GUILayer.InsertTab.UpdateMassRecord as UMR


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()
    UMR.Button_Update_Mass_Record.update_mass_record()


    # AKTUALIZACJA KOMÓREK BAZ DANYCH
    # GUILayer.InsertTab.UpdateRecord.update_value()

    # AKTUALIZACJA DANYCH W monthly_stmt
    # empList = ['PK', 'TO', 'DC', 'WM', 'MS', 'SO']
    # for _ in empList:
    #     BuisnessLayer.Database.Updater.Update_monthly_stmt_for_one("2022-10", _).update_value()

    # BuisnessLayer.Database.Updater.Update_monthly_stmt_for_one("2022-10", "SO").update_value()
    #
    # print(BuisnessLayer.Database.Geter.GuestsGetter(1, 1, 1).get_guests("2022-10"))

    # li = BuisnessLayer.Database.Geter.UniqueIDGetter(1, 1, 2).get_list_uniqueID()
    # for _ in li:
    #     BuisnessLayer.Database.InsertData.GeneralStmt(1, 1, 4).insert_monthly_stmt("2022-10", _)

    t2 = datetime.datetime.now()
    print(t2 - t1)


if __name__ == '__main__':
    main()
