import re

import BuisnessLayer.Database.ScanRecords


class GeneralStmt:
    def __init__(self, table_name, scanner, qdate):
        self.table_name = table_name
        self.db_query = scanner
        self.qdate = qdate

    def sum_taxes_for_employee(self, qid):
        scanner = BuisnessLayer.Database.ScanRecords.RecordsScanner()
        result = scanner.left_outer_join(qid)
        tax_sum = 0
        if result is None:
            return 0
        else:
            taxes = result[0][8]
            tax_list = re.sub(r'[^0-9.,]+', '', str(taxes)).split(",")
            for tax in tax_list:
                if tax != "":
                    tax_sum += float(tax)
        return tax_sum

