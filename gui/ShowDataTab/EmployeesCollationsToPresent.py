import buissnes.Computing.statements_computer


coll = buissnes.Computing.statements_computer.ComputeEmployee("2022-10", "PK")
comp = buissnes.Computing.statements_computer.EmployeeCollation("2022-10", "PK")


def list_of_recieved_by_a_priest(): return coll.list_of_recieved_by_a_priest()
def sum_of_recieved_by_a_priest(): return coll.sum_of_recieved_by_a_priest()
def amount_of_all_masses_applied_by_a_priest(): return coll.amount_of_all_masses_applied_by_a_priest()
def amount_of_first_masses_applied_by_a_priest(): return coll.amount_of_first_masses_applied_by_a_priest()
def amount_of_bination_applied_by_a_priest(): return coll.amount_of_bination_applied_by_a_priest()
def quota_for_priest(): return coll.quota_for_priest()
def bination_quota_for_priest(): return coll.bination_quota_for_priest()
def total_wage_for_priest(): return coll.total_wage_for_priest()



