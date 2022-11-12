import re
from buissnes.Database.Filter import Filter


class GeneralStmt(Filter):
    def __init__(self, qdate):
        super().__init__()
        self.qdate = qdate

    def sum_taxes_for_employee(self, qid):
        result = Filter().search_employees_by_uniqueID(qid)
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

    def sum_taxes(self, qid):
        result = Filter().search_employees_by_uniqueID(qid)
        tax_sum = 0
        try:
            if result is None:
                return 0
            else:
                sumik = 0
                for _ in result[0].values():
                    if _ or _ != "":
                        sumik += float(_)
            return tax_sum
        except:
            return 0
