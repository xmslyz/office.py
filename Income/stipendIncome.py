from Income.income import Income


class massPayment(Income):

    def __init__(self, amount, who_recived, who_applied):
        self.amount = amount
        self.recived = who_recived
        self.applied = who_applied

    def show_payment(self):
        print(f"Stypendium w wysokości {self.amount} przyjął {self.recived}.\nMszę odprawił {self.applied}")


class count_stipends(massPayment):

    def sum_stipends_for_reciver(sack, recived_money):
        suma = 0
        for stipends in sack:
            if stipends.recived == recived_money:
                suma += stipends.amount
        return suma

    def list_of_stipends_for_reciever(sack, reciever):
        lista = []
        for stipends in sack:
            if stipends.recived == reciever:
                lista.append(stipends.amount)
        return lista

    def sum_all_stipends(sack):
        suma = 0
        for stipends in sack:
            suma += stipends.amount
        return suma

    def sum_of_masses(sack):
        return len(sack)

    def mediana_stipends(sack):
        return count_stipends.sum_all_stipends(sack) / count_stipends.sum_of_masses(sack)

    def sum_of_applied_masses(sack, applier):
        suma = 0
        for stipends in sack:
            if stipends.applied == applier:
                suma += 1
        return suma

    def payment_title_mass(sack, applier):
        return count_stipends.mediana_stipends(sack) * count_stipends.sum_of_applied_masses(sack, applier)
