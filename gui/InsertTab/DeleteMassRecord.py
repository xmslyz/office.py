import buissnes.Income.ManageStipend


class Button_Delete_Mass_Record:
    def delete_intention_row(self):
        """
        Usuwa wiersz w tabeli intencje dla id = ?
        """
        input_from_gui = '249'
        up = buissnes.Income.ManageStipend.DeleteMassStipend()
        up.get_conn_details(1, 1, 1)
        up.delete(input_from_gui)

    def delete_last(self):
        up = buissnes.Income.ManageStipend.DeleteMassStipend()
        up.get_conn_details(1, 1, 1)
        up.delete_last_record()
