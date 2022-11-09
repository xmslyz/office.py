import buissnes.Database.Geter
import buissnes.Database.InsertData
import buissnes.Database.Updater


class Button_Update_Mass_Record:

    def update_mass_record():
        Input_Actual_Data.updated_values()

        buissnes.Database.Updater.Update_monthly_stmt_for_all().update()


class Input_Actual_Data:
    def updated_values():
        gui_column = "pars" # -> stała
        gui_abreviation = "PK"
        gui_value = "3200" # input
        gui_uniqueID = buissnes.Database.Geter.UniqueIDGetter().get_uniqueID(gui_abreviation, 1)

        # wrzuca dane z obiektu do tabeli
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.__repr__()
        stip.update_value(column=gui_column, value=gui_value, qid=gui_uniqueID)

    def recive_updated_data():
        # przykładowe dane
        amount = 60
        reciving_priest = "MS"
        celebrating_priest = "MS"
        hour_oc = "07:00:00"
        date_oc = "2022-11-07"
        type_of_mass = ""
        is_gregorian = False

        # tworzy pusty obiekt rejestru dla księgi intencji
        batch = buissnes.Income.StipendIncome.StipendRecord()
        batch.amount = amount
        batch.reciving_priest = reciving_priest
        batch.celebrating_priest = celebrating_priest
        batch.hour_of_celebration = hour_oc
        batch.date_of_celebration = date_oc
        batch.type_of_mass = type_of_mass
        batch.is_gregorian = is_gregorian

        return batch