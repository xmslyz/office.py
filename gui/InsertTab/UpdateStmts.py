import buisness.Statements.ManageMonthlyStmt
import buisness.Statements.ManageGeneralStmt


class ButtonUpdateMonthlyStmt:

    def update_monthly_stmt(self, when):
        """
        Update monthly statements
        :param when: 'yyyy-mm' format
        :return: none
        """
        buisness.Statements.ManageMonthlyStmt.Update_monthly_stmt_for_all().update(when)


class ButtonUpdateGeneralStmt:

    def update_general_stmt(self, when):
        """
        Update monthly statements
        :param when: 'yyyy-mm' format
        :return: none
        """
        upd = buisness.Statements.ManageGeneralStmt.NewGenStmt()
        upd.get_conn_details("general_stmt")
        upd.insert_all(when)
