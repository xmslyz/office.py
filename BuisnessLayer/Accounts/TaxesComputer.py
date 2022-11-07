import re
from BuisnessLayer.Database.ScanRecords import RecordsScanner


class GeneralStmt(RecordsScanner):
    def __init__(self, path_num, dbnm_num, tbl_num, qdate):
        super().__init__(path_num, dbnm_num, tbl_num)
        self.qdate = qdate
        print(self.__repr__())

    def sum_taxes_for_employee(self, qid):
        result = self.left_outer_join(qid)
        print(result)
        tax_sum = 0
        if result is None:
            return 0
        else:
            taxes = result[0][8]
            print(taxes)
            tax_list = re.sub(r'[^0-9.,]+', '', str(result)).split(",")
            for tax in tax_list:
                
                if tax != "":
                    tax_sum += float(tax)
        print(tax_sum)
        return tax_sum

