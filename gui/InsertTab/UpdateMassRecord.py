import buissnes.Database.Geter
import buissnes.Employee.ManageEmployee
import buissnes.Statements.ManageMonthlyStmt
import buissnes.Database.ScanRecords
import buissnes.Income.ManageStipend
import buissnes.Income.Stipend


class Button_Update_Mass_Record:
    def update_intention_row(self):
        """
        Aktualizuje wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = '4'
        valinput = Input_Actual_Data.recive_updated_data()
        buissnes.Income.ManageStipend.UpdateMassStipend(1, 1, 1).update(valinput, input_from_gui)


class Input_Actual_Data:
    def recive_updated_data():
        # przykładowe dane
        amount = "30"
        reciving_priest = "MS"
        celebrating_priest = "WM"
        hour_oc = "07:00:00"
        date_oc = "2022-10-01"
        type_of_mass = ""
        is_gregorian = False

        # tworzy pusty obiekt rejestru dla księgi intencji
        stipend = buissnes.Income.Stipend.StipendRecord()
        stipend.amount = amount
        stipend.reciving_priest = reciving_priest
        stipend.celebrating_priest = celebrating_priest
        stipend.hour_of_celebration = hour_oc
        stipend.date_of_celebration = date_oc
        stipend.type_of_mass = type_of_mass
        stipend.is_gregorian = is_gregorian
        return stipend
