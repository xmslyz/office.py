from DatabaseLayer.Constants.constants import second_mass_constant

BINACJA = second_mass_constant()


class GeneralStmt:
    def __init__(self, table_name, scanner):
        self.table_name = table_name
        self.db_query = scanner

    #  all masses
    def list_of_all_recived(self):
        result = self.db_query.select_all_where_q_is()
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist

    def sum_of_all_recived(self):
        result = self.db_query.select_all_where_q_is()
        qlist = []
        for _ in result:
            if isinstance((_[2]), float):
                qlist.append(float(_[2]))
        return sum(qlist)

    def amount_of_all_paid(self):
        result = self.db_query.select_all_where_q_is_not(qamount="")
        qlist = []
        for _ in result:
            qlist.append(_[2])
        return len(qlist)

    def mediana(self):
        no_greg_sum = self.sum_of_all_recived() - self.sum_of_all_gregorian() - self.sum_of_binations()
        total = no_greg_sum + self.gregorian_sum_of_medianas()
        return round(total / (self.amount_of_aplicated() - self.amount_of_binations()), 2)

    #
    #  binations
    #
    def list_of_binations(self):
        return self.db_query.select_all_where_q_is(qfirst_mass="0")

    def amount_of_binations(self):
        return len(self.list_of_binations())

    def sum_of_binations(self):
        return self.amount_of_binations() * BINACJA


    #
    #  gregorian masses
    #
    def list_of_all_gregorian(self):
        result = self.db_query.select_all_where_q_is(qgregorian=1)
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist

    def amount_of_all_gregorian(self):
        return len(self.db_query.select_all_where_q_is(qgregorian=1))

    def sum_of_all_gregorian(self):
        result = self.db_query.select_all_where_q_is(qgregorian=1)
        qlist = []
        for _ in result:
            if isinstance((_[2]), float):
                qlist.append(_[2])
        return sum(qlist)

    def gregorian_mediana(self):
        if self.amount_of_all_gregorian() == 0:
            return 0
        else:
            return self.sum_of_all_gregorian() / self.amount_of_all_gregorian()

    def gregorian_sum_of_medianas(self):
        return self.gregorian_mediana() * self.amount_of_all_gregorian()

    #
    # aplication
    #
    def list_of_aplicated_stipends(self):
        result = self.db_query.select_all_where_q_is_not(qcelebrated_by="")
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist

    def amount_of_aplicated(self):
        return len(self.list_of_aplicated_stipends())

    #
    #  evaluation
    #
    def list_paid_not_applicated(self):
        result = self.db_query.select_all_where_q_like(qamount='%.%', qcelebrated_by="")
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist

    def list_not_paid_aplicated(self):
        result = self.db_query.select_all_where_q_like(qamount='', qcelebrated_by="_%", qgregorian='0')
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist

    def list_not_paid_not_aplicated(self):
        result = self.db_query.select_all_where_q_is(qamount="", qcelebrated_by="")
        qlist = []
        for _ in result:
            qlist.append(_)
        return qlist


class PriestStmt(GeneralStmt):
    def __init__(self, table_name, scanner, who_recived):
        super().__init__(table_name, scanner)
        self.who_recived = who_recived
        self.db_query = scanner

    def list_of_recieved_by_a_priest(self):
        result = self.db_query.select_all_where_q_is(qpriest_reciving=self.who_recived)
        qlist = []
        for _ in result:
            if isinstance((_[2]), float):
                qlist.append(float(_[2]))
        return qlist

    def sum_of_recieved_by_a_priest(self):
        return sum(self.list_of_recieved_by_a_priest())

    def amount_of_all_masses_applied_by_a_priest(self):
        """
        Ilość wszystkich mszy odprawionych przez ks.
        :return: int
        """
        result = self.db_query.select_all_where_q_is(qcelebrated_by=self.who_recived)
        return len(result)

    def amount_of_first_masses_applied_by_a_priest(self):
        """
        Ilość 'pierwszych mszy' mszy odprawionych przez ks.
        :return: int
        """
        result = self.db_query.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="1")
        return len(result)

    def amount_of_bination_applied_by_a_priest(self):
        result = self.db_query.select_all_where_q_is(qcelebrated_by=self.who_recived, qfirst_mass="0")
        return len(result)

    def quota_for_priest(self):
        """
        (Quota) Iloraz ilości odprawionych mszy i średniej wartości intencji.
        :return: float
        """
        total_stipend = self.amount_of_first_masses_applied_by_a_priest() * self.mediana()
        return round(total_stipend, 2)

    def bination_quota_for_priest(self):
        """
        (Binacje) Iloraz ilości odprawionych (kolejnych w danym dniu mszy) i stałej wartości intencji "binacyjnej.
        :return: float
        """
        bination = self.amount_of_all_masses_applied_by_a_priest() - self.amount_of_first_masses_applied_by_a_priest()
        return round(float(bination * BINACJA), 2)

    def total_wage_for_priest(self):
        return round(self.quota_for_priest() + self.bination_quota_for_priest(), 2)
