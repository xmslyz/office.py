import datetime
import re
import pandas as pd


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
    def amount(self, value):
        if value[0] == "-":
            raise Exception("Kwota nie może być mniejsza od zera")
        amount = str(re.sub(r'[^0-9.]+', '', str(value).strip()))
        amount = 0.0 if amount == "" else float(amount)
        self.__amount = amount
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
        """
        First letter of name and surname. Max. 3 chars (in case of similar abrev.)
        :param value:
        :return:
        """
        if len(value) > 3:
            raise Exception("Przekroczono dopuszczalną ilość znaków (3).")
        result = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())
        self.__celebrated_by = result.upper()[:3]

    @property
    def date_of_celebration(self):
        return self.__celebration_date
    @date_of_celebration.getter
    def date_of_celebration(self):
        formated_date = self.__celebration_date
        return formated_date
    @date_of_celebration.setter
    def date_of_celebration(self, value):
        """
        Dopuszczalny format daty: "yyyy-mm-dd" lub "dd-mm-yyyy"

        """

        value = str(re.sub(r'[^0-9-]+', '', str(value).strip()))
        ymd = re.compile('^\d{4}-\d{2}-\d{2}')
        dmy = re.compile('^\d{2}-\d{2}-\d{4}')
        if ymd.match(value) is not None or dmy.match(value) is not None:
            try:
                if value[4] == "-" and value[7]:
                    isNaT = pd.to_datetime(value, format="%Y-%m-%d", errors='coerce')
                    if isNaT is pd.NaT:
                        raise Exception("Nie ma takiej daty")
                elif value[2] == "-" and value[5]:
                    ddmmyyyy = value
                    value = ddmmyyyy[6:] + "-" + ddmmyyyy[3:5] + "-" + ddmmyyyy[:2]
                    isNaT = pd.to_datetime(value, format="%Y-%m-%d", errors='coerce')
                    if isNaT is pd.NaT:
                        raise Exception("Nie ma takiej daty")
            finally:
                self.__celebration_date = value
        else:
            raise Exception("Podaj właściwy format daty")


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
