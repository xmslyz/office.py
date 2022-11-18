import buisness.Employee.ManageEmployee
import buisness.Database.Geter
import buisness.Computing.statements_computer
import buisness.Computing.tax_computer


class Update_monthly_stmt_for_one:
    def __init__(self, when, who):
        self.when = when
        self.who = who
        self.emp_stmt = buisness.Computing.statements_computer.ComputeEmployee(when, who)
        self.emp_stmt.get_conn_details("employees")

    def __repr__(self):
        return f"**********\n{self.emp_stmt}----------\nUpdating {self.when} employee stmt for {self.who}\n**********\n"

    def update_value(self, abrev=None):
        if not abrev:
            uni = buisness.Database.Geter.UniqueIDGetter().get_uniqueID(self.who, "1")
        else:
            uni = buisness.Database.Geter.UniqueIDGetter().get_uniqueID(abrev, "1")
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
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_amount(self, col, uid):
        val = self.emp_stmt.amount_of_first_masses_applied_by_a_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_int_sum(self, col, uid):
        val = self.emp_stmt.quota_for_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_amount(self, col, uid):
        val = self.emp_stmt.amount_of_bination_applied_by_a_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_bin_sum(self, col, uid):
        val = self.emp_stmt.bination_quota_for_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_pars(self, col, uid):
        val = self.emp_stmt.pars_for_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_pretax(self, col, uid):
        val = self.emp_stmt.total_wage_for_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_taxes(self, col, uid):
        val = buisness.Computing.tax_computer.GeneralStmt(self.when).sum_taxes(uid)
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_receival(self, col, uid):
        val = self.emp_stmt.sum_of_recieved_by_a_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)

    def up_net(self, col, uid):
        val = self.emp_stmt.net_for_priest()
        stip = buisness.Employee.ManageEmployee.UpdateEmployeeData()
        stip.get_conn_details("monthly_stmt")
        stip.update_value(column=col, value=val, qid=uid)


class Update_monthly_stmt_for_all:
    def __init__(self):
        conn = buisness.Database.Geter.IntentionsColsGetter()
        conn.get_conn_details("employees")
        self.on_duty = conn.get_abreviations()

    def update(self, when):
        for _ in self.on_duty:
            Update_monthly_stmt_for_one(when, _).update_value(_)
