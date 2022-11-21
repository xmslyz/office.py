import re
from buisness.Database.SQLConnector import Connection


class GeneralStmt(Connection):
    def __init__(self, qdate):
        super().__init__()
        self.qdate = qdate

    def sum_taxes_for_employee(self, qid):
        """
        Geting sum of all taxes of employee
        :param qid: uniqeID of employee
        :return: float(tax)
        """
        # geting tax dicionary from employee by his unique ID
        conn = Connection()
        conn.get_conn_details("employees")
        stmt = f"SELECT taxes FROM employees WHERE uniqueID IS '{qid}';"

        # computing tax from taxes
        tax_sum = 0
        try:
            result = conn.sql_querry(stmt)[0][0]
            if result:
                taxes = result
                tax_list = re.sub(r"[^0-9.,]+", "", str(taxes)).split(",")
                for tax in tax_list:
                    if tax != "":
                        tax_sum += float(tax)
                return tax_sum
            else:
                return 0
        except IndexError:
            return 0
