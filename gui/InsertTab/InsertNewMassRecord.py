import buissnes.Database.Builder
import buissnes.Income.ManageStipend
import buissnes.Income.Stipend
import buissnes.Database.Geter
import buissnes.Employee.Identity
import buissnes.Statements.ManageMonthlyStmt


class Button_Add_New_Record:

    def add_new_mass_record(self):
        """
        Wrzuca dane z obiektu do tabeli.
        : jobs: dla ilu kolejnych dni (od daty początkowej) default = 1
        :return:
        """
        jobs = Input_Add_New_Record.insert_batch_job()
        stipend = Input_Add_New_Record.insert_mass_records()
        stip = buissnes.Income.ManageStipend.CreateNewStipend()
        stip.get_conn_details(1, 1, 1)
        stip.insert_record(val=stipend, amount=jobs)


class Input_Add_New_Record:
    """ ilość powtórzeń """
    def insert_batch_job():
        reps = 1
        return reps

    def insert_mass_records():
        # przykładowe dane z GUI
        amount = 55
        reciving_priest = "WM"
        celebrating_priest = "SO"
        hour_oc = "12:00:00"
        date_oc = "2022-11-12"
        type_of_mass = "test"
        is_gregorian = False

        # tworzy pusty obiekt rejestru dla księgi intencji
        batch = buissnes.Income.Stipend.StipendRecord()
        batch.amount = amount
        batch.reciving_priest = reciving_priest
        batch.celebrating_priest = celebrating_priest
        batch.hour_of_celebration = hour_oc
        batch.date_of_celebration = date_oc
        batch.type_of_mass = type_of_mass
        batch.is_gregorian = is_gregorian

        return batch
