from collections import Counter

import buissnes.Database.Builder
import buissnes.Income.StipendIncome
import buissnes.Database.InsertData
import buissnes.Employees.Employee
from buissnes.Database.Geter import UniqueIDGetter
import buissnes.Computing.statements_computer  # ->
import buissnes.Computing.tax_computer


class Update_monthly_stmt_for_all:
    def update(self):
        when = ''
        who = ''
        # Update_monthly_stmt_for_one(when, who).update_value()


class Update_monthly_stmt_for_one:
    def __init__(self, when, who):
        self.when = when
        self.who = who
        self.emp_stmt = buissnes.Accounts.MonthlyStatementsComputer.ComputeEmployeeStmt(1, 1, 1, when, who)

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
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_amount(self, col, uid):
        val = self.emp_stmt.amount_of_first_masses_applied_by_a_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_sum(self, col, uid):
        val = self.emp_stmt.quota_for_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_amount(self, col, uid):
        val = self.emp_stmt.amount_of_bination_applied_by_a_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_sum(self, col, uid):
        val = self.emp_stmt.bination_quota_for_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_pars(self, col, uid):
        val = self.emp_stmt.pars_for_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_pretax(self, col, uid):
        val = self.emp_stmt.total_wage_for_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_taxes(self, col, uid):
        val = buissnes.Accounts.TaxesComputer.ComputeMonthlyStmt(1, 1, 2, self.when).sum_taxes_for_employee(uid)
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_receival(self, col, uid):
        val = self.emp_stmt.sum_of_recieved_by_a_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)

    def up_net(self, col, uid):
        val = self.emp_stmt.net_for_priest()
        stip = buissnes.Database.InsertData.PersonalData(1, 1, 3)
        stip.update_value(column=col, value=val, qid=uid)
