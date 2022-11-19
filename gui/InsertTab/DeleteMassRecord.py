import buisness.Income.ManageStipend


class Button_Delete_Mass_Record:
    def delete_intention_row(self):
        """
        Usuwa wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = '246'
        up = buisness.Income.ManageStipend.DeleteMassStipend()
        up.get_conn_details("intentions")
        up.delete(input_from_gui)

    def delete_last(self):
        up = buisness.Income.ManageStipend.DeleteMassStipend()
        up.get_conn_details("intentions")
        up.delete_last_record()
