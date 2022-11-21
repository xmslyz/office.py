import buisness.Database.SQLConnector


class Button_Show_Mass_Record:
    def select_intention_row(self):
        """Pobiera dane dla GUI na podstawie id"""
        input_from_gui = "4"
        sql_stmt = (
            f"SELECT amount, "
            f"priest_reciving, "
            f"celebrated_by, "
            f"celebration_date, "
            f"celebration_hour, "
            f"celebration_type, "
            f"gregorian "
            f"FROM intentions "
            f"WHERE id IS ('{input_from_gui}');"
        )
        con = buisness.Database.SQLConnector.Connection()
        con.get_conn_details("intentions")
        if con.sql_querry(sql_stmt):
            # amount = sql_stmt[0]
            # priest_reciving = sql_stmt[1]
            # celebrated_by = sql_stmt[2]
            # celebration_date = sql_stmt[3]
            # celebration_hour = sql_stmt[4]
            # celebration_type = sql_stmt[5]
            # gregorian = sql_stmt[6]
            print()
