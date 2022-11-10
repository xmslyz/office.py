import datetime
import re


class StipendRecord:

    def __init__(self):
        self.__type = "Stypendium mszalne"
        self.__amount = 0
        self.__priest_reciving = None
        self.__celebrated_by = None
        self.__celebration_date = None
        self.__celebration_hour = None
        self.__celebration_type = None
        self.__gregorian = False
        self.__first_mass = True

    def show_income(self):
        print(f"{self.__type}:\n"
              f"Msza [{self.__celebration_type}] {self.__celebration_date} o godz. {self.__celebration_hour}\n"
              f"Intencję w wysokości {self.__amount} przyjął {self.__priest_reciving}\n"
              f"Odprawił {self.__celebrated_by}\n"
              f"'greg': {self.__gregorian}\n"
              f"'first': {self.__first_mass}")

    @property
    def type(self):
        return self.__type
    @type.getter
    def type(self):
        return self.__type

    @property
    def amount(self):
        return self.__amount
    @amount.getter
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, value) -> float:
        self.__amount = float(re.sub(r'[^0-9.]+', '', str(value).strip()))

    @property
    def reciving_priest(self):
        return self.__priest_reciving
    @reciving_priest.getter
    def reciving_priest(self):
        return self.__priest_reciving
    @reciving_priest.setter
    def reciving_priest(self, value) -> str:
        self.__priest_reciving = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def celebrating_priest(self):
        return self.__celebrated_by
    @celebrating_priest.getter
    def celebrating_priest(self):
        return self.__celebrated_by
    @celebrating_priest.setter
    def celebrating_priest(self, value) -> str:
        self.__celebrated_by = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def date_of_celebration(self):
        return self.__celebration_date
    @date_of_celebration.getter
    def date_of_celebration(self):
        formated_date = self.__celebration_date
        return formated_date
    @date_of_celebration.setter
    def date_of_celebration(self, value):
        format = "%Y-%m-%d"
        result = True
        try:
            result = bool(datetime.datetime.strptime(value, format))
        except ValueError:
            result = False
        finally:
            if result:
                self.__celebration_date = value
            else:
                print("Wrong [date] format")

    @property
    def hour_of_celebration(self):
        return self.__celebration_hour
    @hour_of_celebration.getter
    def hour_of_celebration(self):
        return self.__celebration_hour
    @hour_of_celebration.setter
    def hour_of_celebration(self, value):
        format = "%H:%M:%S"
        result = True
        try:
            result = bool(datetime.datetime.strptime(value, format))
        except ValueError:
            result = False
        finally:
            if result:
                n_val = value
                self.__celebration_hour = n_val[0:5]
            else:
                print("Wrong [time] format")

    @property
    def type_of_mass(self):
        return self.__celebration_type
    @type_of_mass.getter
    def type_of_mass(self):
        return self.__celebration_type
    @type_of_mass.setter
    def type_of_mass(self, value) -> str:
        self.__celebration_type = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def is_gregorian(self):
        return self.__gregorian
    @is_gregorian.getter
    def is_gregorian(self):
        return self.__gregorian
    @is_gregorian.setter
    def is_gregorian(self, value) -> bool:
        if isinstance(value, bool):
            self.__gregorian = value
        else:
            print("[is_gregorian]: Wrong format")

    @property
    def is_first(self):
        return self.__first_mass
    @is_first.getter
    def is_first(self):
        return self.__first_mass
    @is_first.setter
    def is_first(self, value) -> bool:
        if isinstance(value, bool):
            self.__first_mass = value
        else:
            print("Wrong format")
