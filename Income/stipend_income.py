from Income.income import Income


class MassStipend(Income):
    def __init__(self, income_type, amount, who_recived, who_applied, celebration_date, celebration_type):
        self.type = income_type
        self.amount = amount
        self.priest_reciving = who_recived
        self.priest_applying = who_applied
        self.celebration_date = celebration_date
        self.celebration_type = celebration_type

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = 0 if amount < 0 else amount

    def show_stipend(self):
        print(f"{self.type} w wysokości {self.amount} przyjął {self.priest_reciving}. "
              f"Mszę {self.celebration_type} odprawił {self.priest_applying} dnia {self.celebration_date}")

    def show_type(self):
        print(self.type)

    def amount_value(self):
        return self.__amount
