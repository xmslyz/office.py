import buisness.Database.Geter
import buisness.Database.SQLConnector
from buisness.Database.Filter import Filter
import buisness.Computing.tax_computer
from buisness.Input import Caster as cast


class Collation(Filter):
    """
    conn_details : "intentions"
    """

    BINATION = float(buisness.Database.SQLConnector.KeyGeter.constants_getter(
        "bin"))
    GUEST = float(buisness.Database.SQLConnector.KeyGeter.constants_getter(
        "inv"))

    def __init__(self, qdate):
        super().__init__()
        self.qdate = qdate
        self.counted_mediana = None

    def record_by_id(self, qid):
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
        return [x for x in self.select_all_where_q_is()
                if x[5].startswith(self.qdate)]

    def binations__list(self):
        return [x for x in self.select_all_where_q_is(qfirst_mass="0")
                if x[5].startswith(self.qdate)]

    def gregorian__list(self):
        return [x for x in self.select_all_where_q_is(qgregorian=1)
                if x[5].startswith(self.qdate)]

    def aplicated_stipends__list(self):
        return [x for x in self.select_all_where_q_is_not(qcelebrated_by="")
                if x[5].startswith(self.qdate)]

    def paid_not_applicated__list(self):
        return [x for x in self.select_all_where_q_like(qamount='%.%',
                                                        qcelebrated_by="")
                if x[5].startswith(self.qdate)]

    def not_paid_but_aplicated__list(self):
        return [x for x in self.select_all_where_q_like(qamount='',
                                                        qcelebrated_by="_%",
                                                        qgregorian='0')
                if x[5].startswith(self.qdate)]

    def not_paid_nor_aplicated__list(self):
        return [x for x in self.select_all_where_q_is(qamount="",
                                                      qcelebrated_by="")
                if x[5].startswith(self.qdate)]

    def amount_of_all_paid(self):
        return len([x for x in self.select_all_where_q_is_not(qamount="")
                    if x[5].startswith(self.qdate)])

    def amount_of_binations(self):
        return len(self.binations__list())

    def amount_of_all_gregorian(self):
        return len([x for x in self.select_all_where_q_is(qgregorian=1)
                    if x[5].startswith(self.qdate)])

    def amount_of_guest_masses(self):
        uid = buisness.Database.Geter.GuestsGetter()
        uid.get_conn_details("testintentions")
        result = uid.get_guests(self.qdate)
        return sum([int(x[1]) for x in result])

    def amount_of_aplicated(self):
        return len(self.aplicated_stipends__list())

    def sum_of_all_recived(self):
        result = [x[2] for x in self.select_all_where_q_is()
                  if x[5].startswith(self.qdate) and isinstance(x[2],
                                                                float)]
        return float(sum(result))

    def sum_of_all_gregorian(self):
        result = [x[2] for x in self.select_all_where_q_is(qgregorian=1)
                  if x[5].startswith(self.qdate) and isinstance(x[2],
                                                                float)]
        return float(sum(result))


class Compute(Collation):

    def mediana(self):
        """
        Oblicza wartość średniego stypendium

        :return: średnie stypendium

        """
        # goła suma
        netsum = self.sum_of_all_recived() \
                 - self.sum_of_all_gregorian() \
                 - self.sum_of_binations() \
                 - self.sum_for_guests()

        # suma łącznie z średnią z gregorianek
        total = netsum + self.gregorian_sum_of_medianas()

        if (self.amount_of_aplicated() - self.amount_of_binations()) <= 0:
            raise Exception("Ilość zaaplikowanych intencji nie może być "
                            "ujemna")
        else:
            divider = self.amount_of_aplicated() \
                      - self.amount_of_binations() \
                      - self.amount_of_guest_masses()
            if divider > 0:
                self.counted_mediana = round((total / divider), 2)
                return round((total / divider), 2)
            else:
                raise Exception("Ilość zaaplikowanych intencji nie może być "
                                "ujemna")

    def sum_of_binations(self):
        return float(self.amount_of_binations() * self.BINATION)

    def gregorian_mediana(self):
        if self.amount_of_all_gregorian() == 0:
            return 0
        else:
            return self.sum_of_all_gregorian() / self.amount_of_all_gregorian()

    def gregorian_sum_of_medianas(self):
        return self.gregorian_mediana() * self.amount_of_all_gregorian()

    def sum_for_guests(self):
        return round((self.amount_of_guest_masses() * self.GUEST), 2)


class EmployeeCollation(Collation):
    def __init__(self, qdate, who_recived):
        super().__init__(qdate)
        self.who_recived = who_recived

    def list_of_recieved_by_a_priest(self):
        return [x for x in
                self.select_all_where_q_is(qpriest_reciving=self.who_recived)
                if x[5].startswith(self.qdate) and isinstance(x[2],
                                                              float)]

    def sum_of_recieved_by_a_priest(self):
        return sum([x[2] for x in self.list_of_recieved_by_a_priest()])

    def amount_of_all_masses_applied_by_a_priest(self):
        result = [x for x in
                  self.select_all_where_q_is(qcelebrated_by=self.who_recived)
                  if x[5].startswith(self.qdate) and isinstance(x[2],
                                                                float)]
        return len(result)

    def amount_of_first_masses_applied_by_a_priest(self):
        return len([x[2] for x in
                    self.select_all_where_q_is(qcelebrated_by=self.who_recived,
                                               qfirst_mass="1")
                    if x[5].startswith(self.qdate)])

    def amount_of_bination_applied_by_a_priest(self):
        return len([x[2] for x in
                    self.select_all_where_q_is(qcelebrated_by=self.who_recived,
                                               qfirst_mass="0")
                    if x[5].startswith(self.qdate)])


class ComputeEmployee(EmployeeCollation):
    def __init__(self, qdate, who_recived, compute=None):
        super().__init__(qdate, who_recived)
        self.compute = compute

    def quota_for_priest(self):
        """
        (Quota) Iloraz ilości odprawionych mszy i średniej wartości intencji.
        :return: float
        """

        med = self.compute.mediana()
        if med > 0:
            return round(self.amount_of_first_masses_applied_by_a_priest()
                         * med, 2)
        else:
            raise Exception("Średnia intencja nie może być ujemna")

    def bination_quota_for_priest(self):
        """
        (Binacje) Iloraz ilości odprawionych (kolejnych w danym dniu mszy)
        i stałej wartości intencji "binacyjnej.

        :return: float

        """
        bination = self.amount_of_all_masses_applied_by_a_priest() \
                   - self.amount_of_first_masses_applied_by_a_priest()

        return round(float(bination * self.BINATION), 2)

    def total_wage_for_priest(self):
        return round(
            self.quota_for_priest() + self.bination_quota_for_priest(), 2)

    def net_for_priest(self):
        uid = buisness.Database.Geter.UniqueIDGetter()
        uid.get_conn_details("testemployees")

        tax = buisness.Computing.tax_computer.GeneralStmt(self.qdate)
        tax.get_conn_details("testemployees")
        total_tax = tax.sum_taxes_for_employee(uid.get_uniqueID(
            self.who_recived, "1"))

        total = (self.total_wage_for_priest()
                 + self.pars_for_priest()
                 - total_tax) \
                - self.sum_of_recieved_by_a_priest()

        return round(total, 2)

    def pars_for_priest(self):
        return 0.0
