import buissnes.Computing.statements_computer
x = buissnes.Accounts.MonthlyStatementsComputer.ComputeMonthlyStmt(1, 1, 1, "2022-10")


def scan_id(): return x.record_by_id("12")
def sum_of_all_recived(): return x.sum_of_all_recived()
def list_of_all_recived(): return x.list_of_all_recived()
def amount_of_aplicated(): return x.amount_of_aplicated()
def amount_of_all_paid(): return x.amount_of_all_paid()
def mediana(): return x.mediana()
def amount_of_binations(): return x.amount_of_binations()
def list_of_binations(): return x.list_of_binations()
def sum_of_binations(): return x.sum_of_binations()
def list_of_all_gregorian(): return x.list_of_all_gregorian()
def amount_of_all_gregorian(): return x.amount_of_all_gregorian()
def sum_of_all_gregorian(): return x.sum_of_all_gregorian()
def gregorian_mediana(): return x.gregorian_mediana()
def gregorian_sum_of_medianas(): return x.gregorian_sum_of_medianas()
def list_of_aplicated_stipends(): return x.list_of_aplicated_stipends()
def list_not_paid_aplicated(): return x.list_not_paid_aplicated()
def list_not_paid_not_aplicated(): return x.list_not_paid_not_aplicated()

