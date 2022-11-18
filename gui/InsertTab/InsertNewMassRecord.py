import buisness.Database.Builder
import buisness.Income.ManageStipend
import buisness.Income.Stipend
import buisness.Database.Geter
import buisness.Employee.Identity
import buisness.Statements.ManageMonthlyStmt


class Button_Add_New_Record:

    def add_new_mass_record(self):
        """
        Wrzuca dane z obiektu do tabeli.
        : jobs: dla ilu kolejnych dni (od daty początkowej) default = 1
        :return:
        """
        jobs = Input_Add_New_Record.insert_batch_job()
        stipend = Input_Add_New_Record.insert_mass_records()
        stip = buisness.Income.ManageStipend.CreateNewStipend()
        stip.get_conn_details("intentions")
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
        batch = buisness.Income.Stipend.StipendRecord()
        batch.amount = amount
        batch.reciving_priest = reciving_priest
        batch.celebrating_priest = celebrating_priest
        batch.hour_of_celebration = hour_oc
        batch.date_of_celebration = date_oc
        batch.type_of_mass = type_of_mass
        batch.is_gregorian = is_gregorian

        return batch
