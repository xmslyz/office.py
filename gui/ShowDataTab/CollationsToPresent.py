import buissnes.Computing.statements_computer
coll = buissnes.Computing.statements_computer.Collation("2022-10")
comp = buissnes.Computing.statements_computer.Compute("2022-10")


def scan_id(): return coll.record_by_id("12")
def sum_of_all_recived(): return coll.sum_of_all_recived()
def list_of_all_recived(): return coll.list_of_all_recived()
def amount_of_aplicated(): return coll.amount_of_aplicated()
def amount_of_all_paid(): return coll.amount_of_all_paid()
def mediana(): return comp.mediana()
def amount_of_binations(): return coll.amount_of_binations()
def list_of_binations(): return coll.list_of_binations()
def sum_of_binations(): return comp.sum_of_binations()
def list_of_all_gregorian(): return coll.list_of_all_gregorian()
def amount_of_all_gregorian(): return coll.amount_of_all_gregorian()
def sum_of_all_gregorian(): return coll.sum_of_all_gregorian()
def gregorian_mediana(): return comp.gregorian_mediana()
def gregorian_sum_of_medianas(): return comp.gregorian_sum_of_medianas()
def list_of_aplicated_stipends(): return coll.list_of_aplicated_stipends()
def list_not_paid_aplicated(): return coll.list_not_paid_aplicated()
def list_not_paid_not_aplicated(): return coll.list_not_paid_not_aplicated()

