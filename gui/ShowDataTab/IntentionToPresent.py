import buissnes.Database.ScanRecords


class Button_Show_Mass_Record:
    def select_intention_row(self):
        """ Pobiera dane dla GUI na podstawie id """
        input_from_gui = '4'
        sql_stmt = f"SELECT amount, priest_reciving, celebrated_by, celebration_date, celebration_hour, celebration_type, gregorian FROM intentions " \
                   f"WHERE id IS ('{input_from_gui}');"
        con = buissnes.Database.ScanRecords.Connection()
        con.get_conn_details(1, 1, 1)
        query = con.sql_querry(sql_stmt)
        if query:
            amount = sql_stmt[0]
            priest_reciving = sql_stmt[1]
            celebrated_by = sql_stmt[2]
            celebration_date = sql_stmt[3]
            celebration_hour = sql_stmt[4]
            celebration_type = sql_stmt[5]
            gregorian = sql_stmt[6]
        else:
            amount = \
                priest_reciving = \
                celebrated_by = \
                celebration_date = \
                celebration_hour = \
                celebration_type = \
                gregorian = ''
