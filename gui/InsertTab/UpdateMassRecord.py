import buisness.Income.ManageStipend
import buisness.Income.Stipend


class Button_Update_Mass_Record:
    def update_intention_row(self):
        """
        Aktualizuje wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = "245"
        valinput = Input_Actual_Data.recive_updated_data()
        up = buisness.Income.ManageStipend.UpdateMassStipend()
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
        stipend = buisness.Income.Stipend.StipendRecord()
        stipend.amount = amount
        stipend.reciving_priest = reciving_priest
        stipend.celebrating_priest = celebrating_priest
        stipend.hour_of_celebration = hour_oc
        stipend.date_of_celebration = date_oc
        stipend.type_of_mass = type_of_mass
        stipend.is_gregorian = is_gregorian
        return stipend
