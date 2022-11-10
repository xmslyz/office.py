import buissnes.Database.Geter
from buissnes.Database.ScanRecords import Filter
import buissnes.Computing.tax_computer


BINATION = buissnes.Database.Geter.AtributesGeter.constants_getter("bin")
GUEST = buissnes.Database.Geter.AtributesGeter.constants_getter("inv")


class Collation(Filter):
    def __init__(self, qdate):
        super().__init__()
        self.qdate = qdate
        self.qry = Filter()
        self.qry.get_conn_details(1, 1, 1)

    def record_by_id(self, qid):
        x = self.qry.select_all_where_q_like(qid=qid)
        if x:
            return x[0]
        else:
            print("No record with this id")
            return None

    def list_of_all_recived(self):
        result = self.qry.select_all_where_q_is()
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_of_binations(self):
        result = self.qry.select_all_where_q_is(qfirst_mass="0")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_of_all_gregorian(self):
        result = self.qry.select_all_where_q_is(qgregorian=1)
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_of_aplicated_stipends(self):
        result = self.qry.select_all_where_q_is_not(qcelebrated_by="")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_paid_not_applicated(self):
        result = self.qry.select_all_where_q_like(qamount='%.%', qcelebrated_by="")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_not_paid_aplicated(self):
        result = self.qry.select_all_where_q_like(qamount='', qcelebrated_by="_%", qgregorian='0')
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def list_not_paid_not_aplicated(self):
        result = self.qry.select_all_where_q_is(qamount="", qcelebrated_by="")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return qlist

    def amount_of_all_paid(self):
        result = self.qry.select_all_where_q_is_not(qamount="")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_[2])
        return len(qlist)

    def amount_of_binations(self): return len(self.list_of_binations())

    def amount_of_all_gregorian(self):
        result = self.qry.select_all_where_q_is(qgregorian=1)
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_)
        return len(qlist)

    def amount_of_guest_masses(self):
        uid = buissnes.Database.Geter.GuestsGetter().get_guests(self.qdate)
        total = 0
        for _ in uid:
            total += _[1]
        return total

    def amount_of_aplicated(self): return len(self.list_of_aplicated_stipends())

    def sum_of_all_recived(self):
        result = self.qry.select_all_where_q_is()
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                qlist.append(float(_[2]))
        return sum(qlist)

    def sum_of_all_gregorian(self):
        result = self.qry.select_all_where_q_is(qgregorian=1)
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                qlist.append(_[2])
        return sum(qlist)


class Compute(Collation):

    def mediana(self):
        no_greg_sum = self.sum_of_all_recived() - self.sum_of_all_gregorian() - self.sum_of_binations() - self.sum_for_guests()
        total = no_greg_sum + self.gregorian_sum_of_medianas()
        if (self.amount_of_aplicated() - self.amount_of_binations()) <= 0:
            return 1
        else:
            divider = self.amount_of_aplicated() - self.amount_of_binations() - self.amount_of_guest_masses()
            if divider > 0:
                return round((total / divider), 2)
            else:
                return round(0, 2)

    def sum_of_binations(self):
        return self.amount_of_binations() * BINATION

    def gregorian_mediana(self):
        if self.amount_of_all_gregorian() == 0:
            return 0
        else:
            return self.sum_of_all_gregorian() / self.amount_of_all_gregorian()

    def gregorian_sum_of_medianas(self):
        return self.gregorian_mediana() * self.amount_of_all_gregorian()

    def sum_for_guests(self):
        uid = buissnes.Database.Geter.GuestsGetter().get_guests(self.qdate)
        total = 0
        for _ in uid:
            total += _[1]
        return total * GUEST


class EmployeeCollation(Collation):
    def __init__(self, qdate, who_recived):
        super().__init__(qdate)
        self.who_recived = who_recived

    def list_of_recieved_by_a_priest(self):
        result = self.qry.select_all_where_q_is(qpriest_reciving=self.who_recived)
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                qlist.append(float(_[2]))
        return qlist

    def sum_of_recieved_by_a_priest(self): return sum(self.list_of_recieved_by_a_priest())

    def amount_of_all_masses_applied_by_a_priest(self):
        result = self.qry.select_all_where_q_is(qcelebrated_by=self.who_recived)
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_[2])
        return len(qlist)

    def amount_of_first_masses_applied_by_a_priest(self):
        result = self.qry.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="1")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_[2])
        return len(qlist)

    def amount_of_bination_applied_by_a_priest(self):
        result = self.qry.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="0")
        qlist = []
        for _ in result:
            if _[5][0:7] == self.qdate:
                qlist.append(_[2])
        return len(qlist)


class ComputeEmployee(EmployeeCollation):
    def __init__(self, qdate, who_recived):
        super().__init__(qdate, who_recived)

    def quota_for_priest(self):
        """
        (Quota) Iloraz ilości odprawionych mszy i średniej wartości intencji.
        :return: float
        """
        mediana = Compute(self.qdate).mediana()
        if mediana > 0:
            total_stipend = self.amount_of_first_masses_applied_by_a_priest() * mediana
            return round(total_stipend, 2)
        else:
            return round(0, 2)

    def bination_quota_for_priest(self):
        """
        (Binacje) Iloraz ilości odprawionych (kolejnych w danym dniu mszy) i stałej wartości intencji "binacyjnej.
        :return: float
        """
        bination = self.amount_of_all_masses_applied_by_a_priest() - self.amount_of_first_masses_applied_by_a_priest()
        return round(float(bination * BINATION), 2)

    def total_wage_for_priest(self): return round(self.quota_for_priest() + self.bination_quota_for_priest(), 2)

    def net_for_priest(self):
        uid = buissnes.Database.Geter.UniqueIDGetter().get_uniqueID(self.who_recived, "1")
        tax = buissnes.Computing.tax_computer.GeneralStmt(self.qdate).sum_taxes(uid)
        total = (self.total_wage_for_priest() + self.pars_for_priest() - tax) - self.sum_of_recieved_by_a_priest()
        return total

    def pars_for_priest(self):
        return 0.0
