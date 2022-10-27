from Income.income import Income


class massStipend(Income):

    def __init__(self, income_type, amount, who_recived, who_applied):
        self.type = income_type
        self.amount = amount
        self.recived = who_recived
        self.applied = who_applied

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        if amount < 0:
            self.__amount = 0
        else:
            self.__amount = amount

    def show_stipend(self):
        print(f"{self.type} w wysokości {self.amount} przyjął {self.recived}. Mszę odprawił {self.applied}")

    def show_type(self):
        print(self.type)

    def amount_value(self):
        return self.__amount


class count_stipends(massStipend):

    # zwraca sumę przyjętych ofiar za msze przez konkretnego ks.
    def sum_stipends_for_reciver(sack, receiver):
        suma = 0
        for stipends in sack:
            if stipends.recived == receiver:
                suma += stipends.amount
        return suma

    # zwraca listę przyjętych ofiar za msze przez konkretnego ks.
    def list_of_stipends_for_reciever(sack, receiver):
        lista = []
        for stipends in sack:
            if stipends.recived == receiver:
                lista.append(stipends.amount)
        return lista

    # zwraca sumę wszystkich przyjętych ofiar za msze
    def sum_all_stipends(sack):
        suma = 0
        for stipends in sack:
            suma += stipends.amount
        return suma

    # zwraca ilość przyjętych mszy
    def sum_of_masses(sack):
        return len(sack)

    # zwraca średnią (stypendium)
    def mediana_stipends(sack):
        return count_stipends.sum_all_stipends(sack) / count_stipends.sum_of_masses(sack)

    # zwraca ilość odprawionych mszy przez danego ks.
    def sum_of_applied_masses(sack, applier):
        suma = 0
        for stipends in sack:
            if stipends.applied == applier:
                suma += 1
        return suma

    # zwraca quotę za odprawione msze
    def quota(sack, applier):
        return count_stipends.mediana_stipends(sack) * count_stipends.sum_of_applied_masses(sack, applier)
