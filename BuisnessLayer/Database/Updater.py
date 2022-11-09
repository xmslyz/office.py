from collections import Counter

import BuisnessLayer.Database.Builder
import BuisnessLayer.Income.StipendIncome
import BuisnessLayer.Database.InsertData
import BuisnessLayer.Employees.Employee
from BuisnessLayer.Database.Geter import UniqueIDGetter
import BuisnessLayer.Accounts.MonthlyStatementsComputer  # ->
import BuisnessLayer.Accounts.TaxesComputer


class Table1Updater:
    def col1updt(self):
        pass
#     sum_of_all_recived -> ', ssc.sum_of_all_recived())
#     list_of_all_recived -> ', ssc.list_of_all_recived())
#     amount_of_aplicated -> ', ssc.amount_of_aplicated())
#     amount_of_all_paid -> ', ssc.amount_of_all_paid())
#     mediana -> ', ssc.mediana())
#     amount_of_binations -> ', ssc.amount_of_binations())
#     list_of_binations -> ', ssc.list_of_binations())
#     sum_of_binations -> ', ssc.sum_of_binations())
#     list_of_all_gregorian -> ', ssc.list_of_all_gregorian())
#     amount_of_all_gregorian -> ', ssc.amount_of_all_gregorian())
#     sum_of_all_gregorian -> ', ssc.sum_of_all_gregorian())
#     gregorian_mediana -> ', ssc.gregorian_mediana())
#     gregorian_sum_of_medianas -> ', ssc.gregorian_sum_of_medianas())
#     list_of_aplicated_stipends -> ', ssc.list_of_aplicated_stipends())
#     amount_of_aplicated -> ', ssc.amount_of_aplicated())
#     list_not_paid_aplicated -> ', ssc.list_not_paid_aplicated())
#     list_not_paid_aplicated -> ', ssc.list_not_paid_aplicated())
#     list_not_paid_not_aplicated -> ', ssc.list_not_paid_not_aplicated())


class Update_monthly_stmt_for_all:
    def update(self):
        when = ''
        who = ''
        # Update_monthly_stmt_for_one(when, who).update_value()
        print("aktualizuje")


class Update_monthly_stmt_for_one:
    def __init__(self, when, who):
        self.when = when
        self.who = who
        self.emp_stmt = BuisnessLayer.Accounts.MonthlyStatementsComputer.EmployeeStmt(1, 1, 1, when, who)

    def saveit4later(self):
        self.emp_stmt.list_of_recieved_by_a_priest()
        self.emp_stmt.amount_of_all_masses_applied_by_a_priest()

    def update_value(self):
        uni = UniqueIDGetter(1, 1, 2).get_uniqueID(self.who, "1")
        self.up_coll_date('stmt_date', uni)
        self.up_int_amount('intention_amount', uni)
        self.up_int_sum('intention_sum', uni)
        self.up_bin_amount('bination_amount', uni)
        self.up_bin_sum('bination_sum', uni)
        self.up_pars('pars', uni)
        self.up_pretax('pretax', uni)
        self.up_taxes('taxes', uni)
        self.up_receival('receival', uni)
        self.up_net('net', uni)

    def up_coll_date(self, col, uid):
        val = self.when
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_amount(self, col, uid):
        val = self.emp_stmt.amount_of_first_masses_applied_by_a_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_sum(self, col, uid):
        val = self.emp_stmt.quota_for_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_amount(self, col, uid):
        val = self.emp_stmt.amount_of_bination_applied_by_a_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_sum(self, col, uid):
        val = self.emp_stmt.bination_quota_for_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_pars(self, col, uid):
        val = self.emp_stmt.pars_for_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_pretax(self, col, uid):
        val = self.emp_stmt.total_wage_for_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_taxes(self, col, uid):
        val = BuisnessLayer.Accounts.TaxesComputer.GeneralStmt(1, 1, 2, self.when).sum_taxes_for_employee(uid)
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_receival(self, col, uid):
        val = self.emp_stmt.sum_of_recieved_by_a_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_net(self, col, uid):
        val = self.emp_stmt.net_for_priest()
        stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)
