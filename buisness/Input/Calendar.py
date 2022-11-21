

class Calendar:
    def __init__(self, cal_date):
        self.cal_date = cal_date
        self.hours = None
        self.day_type = None
        self.name = None

    def __repr__(self):
        print(
            f'{self.name}: {self.cal_date} ({self.day_type})\n'
            f'{self.hours}'
        )

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def drop_all(self):
        pass



