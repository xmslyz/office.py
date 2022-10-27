from Income.income import Income


class MassStipend(Income):

    def __init__(self, income_type, amount, who_recived, who_applied):
        self.type = income_type
        self.amount = amount
        self.priest_reciving = who_recived
        self.priest_applying = who_applied

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        # self.__amount = 0 if amount < 0 else self.__amount = amount
        self.__amount = amount

    def show_stipend(self):
        print(f"{self.type} w wysokości {self.amount} przyjął {self.priest_reciving}. Mszę odprawił {self.priest_applying}")

    def show_type(self):
        print(self.type)

    def amount_value(self):
        return self.__amount


class CountStipends(MassStipend):

    # zwraca listę przyjętych ofiar za msze przez konkretnego ks.
    def list_of_stipends_recieved_by_a_priest(sack, receiving_money):
        lista = []
        for stipend in sack:
            if stipend.priest_reciving == receiving_money:
                lista.append(stipend.amount)
        return lista

    # zwraca sumę przyjętych ofiar za msze przez konkretnego ks.
    def sum_stipends_recived_by_a_priest(sack, receiving_money):
        return sum(CountStipends.list_of_stipends_recieved_by_a_priest(sack, receiving_money))

    # zwraca sumę wszystkich przyjętych ofiar za msze
    def sum_all_stipends(sack):
        return sum([stipend.amount for stipend in sack])

    # zwraca ilość przyjętych mszy
    def sum_of_masses(sack):
        return len(sack)

    # zwraca średnią (stypendium)
    def mediana_stipends(sack):
        return CountStipends.sum_all_stipends(sack) / CountStipends.sum_of_masses(sack)

    # zwraca ilość odprawionych mszy przez danego ks.
    def sum_of_applied_masses(sack, applier):
        return len([stipend for stipend in sack if stipend.priest_applying == applier])

    # zwraca quotę za odprawione msze
    def quota(sack, applier):
        return CountStipends.mediana_stipends(sack) * CountStipends.sum_of_applied_masses(sack, applier)
