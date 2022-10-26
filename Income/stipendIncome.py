from Income.income import Income


class massPayment(Income):

    def __init__(self, amount, who_recived, who_applied):
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

    def show_payment(self):
        print(f"Stypendium w wysokości {self.amount} przyjął {self.recived}. Mszę odprawił {self.applied}")


class count_stipends(massPayment):

    # zwraca sumę przyjętych ofiar za msze przez konkretnego ks.
    def sum_stipends_for_reciver(sack, reciever):
        suma = 0
        for stipends in sack:
            if stipends.recived == reciever:
                suma += stipends.amount
        return suma

    # zwraca listę przyjętych ofiar za msze przez konkretnego ks.
    def list_of_stipends_for_reciever(sack, reciever):
        lista = []
        for stipends in sack:
            if stipends.recived == reciever:
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
