import buisness.Computing.statements_computer
coll = buisness.Computing.statements_computer.Collation("2022-10")
comp = buisness.Computing.statements_computer.Compute("2022-10")


def scan_id(): return coll.record_by_id("12")
def sum_of_all_recived(): return coll.sum_of_all_recived()
def list_of_all_recived(): return coll.records_in_qdate__list()
def amount_of_aplicated(): return coll.amount_of_aplicated()
def amount_of_all_paid(): return coll.amount_of_all_paid()
def mediana(): return comp.mediana()
def amount_of_binations(): return coll.amount_of_binations()
def list_of_binations(): return coll.binations__list()
def sum_of_binations(): return comp.sum_of_binations()
def list_of_all_gregorian(): return coll.gregorian__list()
def amount_of_all_gregorian(): return coll.amount_of_all_gregorian()
def sum_of_all_gregorian(): return coll.sum_of_all_gregorian()
def gregorian_mediana(): return comp.gregorian_mediana()
def gregorian_sum_of_medianas(): return comp.gregorian_sum_of_medianas()
def list_of_aplicated_stipends(): return coll.aplicated_stipends__list()
def list_not_paid_aplicated(): return coll.not_paid_but_aplicated__list()
def list_not_paid_not_aplicated(): return coll.not_paid_nor_aplicated__list()

