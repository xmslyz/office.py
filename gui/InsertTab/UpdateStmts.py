import buissnes.Statements.ManageMonthlyStmt
import buissnes.Statements.ManageGeneralStmt


class ButtonUpdateMonthlyStmt:

    def update_monthly_stmt(self, when):
        """
        Update monthly statements
        :param when: 'yyyy-mm' format
        :return: none
        """
        buissnes.Statements.ManageMonthlyStmt.Update_monthly_stmt_for_all().update(when)


class ButtonUpdateGeneralStmt:

    def update_general_stmt(self, when):
        """
        Update monthly statements
        :param when: 'yyyy-mm' format
        :return: none
        """
        upd = buissnes.Statements.ManageGeneralStmt.NewGenStmt()
        upd.get_conn_details(1, 1, 4)
        upd.insert_all(when)
