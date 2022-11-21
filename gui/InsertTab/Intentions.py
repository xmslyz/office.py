from buisness.Income import ManageStipend, Stipend


class Button_Add_New_Record:
    def add_new_mass_record(self):
        """
        Wrzuca dane z obiektu do tabeli.
        : jobs: dla ilu kolejnych dni (od daty początkowej) default = 1
        :return:
        """
        jobs = Input_Add_New_Record.insert_batch_job()
        stipend = Input_Add_New_Record.insert_mass_records()
        stip = ManageStipend.CreateNewStipend()
        stip.get_conn_details("intentions")
        stip.insert_record(val=stipend, amount=jobs)


class Input_Add_New_Record:
    """ilość powtórzeń"""

    def insert_batch_job():
        reps = 1
        return reps

    def insert_mass_records():
        # przykładowe dane z GUI
        amount = 55
        reciving_priest = "MS"
        celebrating_priest = "SO"
        hour_oc = "12:00:00"
        date_oc = "2022-12-31"
        type_of_mass = "test"
        is_gregorian = False

        # tworzy pusty obiekt rejestru dla księgi intencji
        batch = Stipend.StipendRecord()
        batch.amount = amount
        batch.reciving_priest = reciving_priest
        batch.celebrating_priest = celebrating_priest
        batch.hour_of_celebration = hour_oc
        batch.date_of_celebration = date_oc
        batch.type_of_mass = type_of_mass
        batch.is_gregorian = is_gregorian

        return batch


class Button_Update_Mass_Record:
    def update_intention_row(self):
        """
        Aktualizuje wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = "245"
        valinput = Input_Actual_Data.recive_updated_data()
        up = ManageStipend.UpdateMassStipend()
        up.get_conn_details("intentions")
        up.update(valinput, input_from_gui)


class Input_Actual_Data:
    def recive_updated_data():
        # przykładowe dane
        amount = "100"
        reciving_priest = "ZZ"
        celebrating_priest = "PP"
        hour_oc = "07:00:00"
        date_oc = "2022-10-01"
        type_of_mass = ""
        is_gregorian = False

        # tworzy pusty obiekt rejestru dla księgi intencji
        stipend = Stipend.StipendRecord()
        stipend.amount = amount
        stipend.reciving_priest = reciving_priest
        stipend.celebrating_priest = celebrating_priest
        stipend.hour_of_celebration = hour_oc
        stipend.date_of_celebration = date_oc
        stipend.type_of_mass = type_of_mass
        stipend.is_gregorian = is_gregorian
        return stipend


class Button_Delete_Mass_Record:
    def delete_intention_row(self):
        """
        Usuwa wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = "246"
        up = ManageStipend.DeleteMassStipend()
        up.get_conn_details("intentions")
        up.delete(input_from_gui)

    def delete_last(self):
        up = ManageStipend.DeleteMassStipend()
        up.get_conn_details("intentions")
        up.delete_last_record()
