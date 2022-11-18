import buisness.Database.Geter
import buisness.Database.SQLConnector
from buisness.Database.Filter import Filter
import buisness.Computing.tax_computer
from buisness.Input import Caster as cast


class Collation(Filter):
    """
    conn_details : "intentions"
    """

    BINATION = buisness.Database.SQLConnector.KeyGeter.constants_getter("bin")
    GUEST = buisness.Database.SQLConnector.KeyGeter.constants_getter("inv")

    def __init__(self, qdate):
        super().__init__()
        self.qdate = qdate

    def record_by_id(self, qid):
        """
        Search by record id

        :param qid: record id
        :return: (tuple) where id=qid
        """
        qid = cast.string_2_string(qid)
        if qid:
            query = self.select_all_where_q_like(qid=qid)
            if query:
                return query
            else:
                raise Exception("No record with this id")
        else:
            raise Exception("Wrong input type")

    def records_in_qdate__list(self):
        """
        List of all records in aforementioned qdate
        :return: [list of tuples]
        """
        result = []
        for _ in self.select_all_where_q_is():
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def binations__list(self):
        query = self.select_all_where_q_is(qfirst_mass="0")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def gregorian__list(self):
        query = self.select_all_where_q_is(qgregorian=1)
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def aplicated_stipends__list(self):
        query = self.select_all_where_q_is_not(qcelebrated_by="")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def paid_not_applicated__list(self):
        query = self.select_all_where_q_like(qamount='%.%', qcelebrated_by="")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def not_paid_but_aplicated__list(self):
        query = self.select_all_where_q_like(qamount='', qcelebrated_by="_%", qgregorian='0')
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def not_paid_nor_aplicated__list(self):
        query = self.select_all_where_q_is(qamount="", qcelebrated_by="")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return result

    def amount_of_all_paid(self):
        query = self.select_all_where_q_is_not(qamount="")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_[2])
        return len(result)

    def amount_of_binations(self): return len(self.binations__list())

    def amount_of_all_gregorian(self):
        query = self.select_all_where_q_is(qgregorian=1)
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_)
        return len(result)

    def amount_of_guest_masses(self):
        uid = buisness.Database.Geter.GuestsGetter().get_guests(self.qdate)
        total = 0
        for _ in uid:
            total += _[1]
        return total

    def amount_of_aplicated(self): return len(self.aplicated_stipends__list())

    def sum_of_all_recived(self):
        query = self.select_all_where_q_is()
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                result.append(float(_[2]))
        return sum(result)

    def sum_of_all_gregorian(self):
        query = self.select_all_where_q_is(qgregorian=1)
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                result.append(_[2])
        return sum(result)


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
        return self.amount_of_binations() * self.BINATION

    def gregorian_mediana(self):
        if self.amount_of_all_gregorian() == 0:
            return 0
        else:
            return self.sum_of_all_gregorian() / self.amount_of_all_gregorian()

    def gregorian_sum_of_medianas(self):
        return self.gregorian_mediana() * self.amount_of_all_gregorian()

    def sum_for_guests(self):
        uid = buisness.Database.Geter.GuestsGetter().get_guests(self.qdate)
        total = 0
        for _ in uid:
            total += _[1]
        return total * self.GUEST


class EmployeeCollation(Collation):
    def __init__(self, qdate, who_recived):
        super().__init__(qdate)
        self.who_recived = who_recived

    def list_of_recieved_by_a_priest(self):
        query = self.select_all_where_q_is(qpriest_reciving=self.who_recived)
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate and isinstance((_[2]), float):
                result.append(float(_[2]))
        return result

    def sum_of_recieved_by_a_priest(self): return sum(self.list_of_recieved_by_a_priest())

    def amount_of_all_masses_applied_by_a_priest(self):
        query = self.select_all_where_q_is(qcelebrated_by=self.who_recived)
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_[2])
        return len(result)

    def amount_of_first_masses_applied_by_a_priest(self):
        query = self.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="1")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_[2])
        return len(result)

    def amount_of_bination_applied_by_a_priest(self):
        query = self.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="0")
        result = []
        for _ in query:
            if _[5][0:7] == self.qdate:
                result.append(_[2])
        return len(result)


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
        return round(float(bination * self.BINATION), 2)

    def total_wage_for_priest(self): return round(self.quota_for_priest() + self.bination_quota_for_priest(), 2)

    def net_for_priest(self):
        uid = buisness.Database.Geter.UniqueIDGetter().get_uniqueID(self.who_recived, "1")
        tax = buisness.Computing.tax_computer.GeneralStmt(self.qdate).sum_taxes(uid)
        total = (self.total_wage_for_priest() + self.pars_for_priest() - tax) - self.sum_of_recieved_by_a_priest()
        return total

    def pars_for_priest(self):
        return 0.0
