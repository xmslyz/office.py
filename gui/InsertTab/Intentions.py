from buisness.Income import ManageStipend, Stipend


class TabIntentions:
    def get_intention_data(self):
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

    def add_new_record(self, reps=1):
        """
        Wrzuca dane z obiektu do tabeli.
        : reps: dla ilu kolejnych dni (od daty początkowej) default = 1
        :return:
        """
        stipend = self.get_intention_data()
        stip = ManageStipend.CreateNewStipend()
        stip.get_conn_details("intentions")
        stip.insert_record(val=stipend, amount=reps)

    def update_intention(self):
        """
        Aktualizuje wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = "245"
        valinput = self.get_intention_data()
        up = ManageStipend.UpdateMassStipend()
        up.get_conn_details("intentions")
        up.update(valinput, input_from_gui)

    def delete_intention(self):
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
