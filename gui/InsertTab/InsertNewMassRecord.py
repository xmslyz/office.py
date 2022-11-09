import buissnes.Database.Builder
import buissnes.Income.StipendIncome
import buissnes.Database.InsertData
import buissnes.Database.Geter
import buissnes.Database.Updater
import buissnes.Employees.Employee


class Button_Add_New_Record:
    def add_new_mass_record():
        """
        Wrzuca dane z obiektu do tabeli.
        : jobs: dla ilu kolejnych dni (od daty początkowej) default = 1
        :return:
        """
        jobs = Input_Add_New_Record.insert_batch_job()
        stipend = Input_Add_New_Record.insert_mass_records()

        stip = buissnes.Database.InsertData.MassRecord(1, 1, 1)
        stip.insert_record(val=stipend, amount=jobs)

        # automatycznie uaktualnij monthly_stmt
        buissnes.Database.Updater.Update_monthly_stmt_for_all().update()


class Input_Add_New_Record:
    def insert_batch_job():
        reps = 1
        return reps

    def insert_mass_records():
        # przykładowe dane
        amount = 60
        reciving_priest = "DD"
        celebrating_priest = "DD"
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
