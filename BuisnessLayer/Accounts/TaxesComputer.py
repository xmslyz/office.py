import re
from BuisnessLayer.Database.ScanRecords import RecordsScanner


class GeneralStmt(RecordsScanner):
    def __init__(self, path_num, dbnm_num, tbl_num, qdate):
        super().__init__(path_num, dbnm_num, tbl_num)
        self.qdate = qdate

    def sum_taxes_for_employee(self, qid):
        result = self.left_outer_join(qid)
        tax_sum = 0
        try:
            if result is None:
                return 0
            else:
                taxes = result[0][8]
                tax_list = re.sub(r'[^0-9.,]+', '', str(taxes)).split(",")
                for tax in tax_list:
                    if tax != "":
                        tax_sum += float(tax)
            return tax_sum
        except:
            return 0

