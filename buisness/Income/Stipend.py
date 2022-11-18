import datetime
import re
import pandas


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
    def amount(self, value) -> str:
        if isinstance(value, bool):
            raise Exception("Podano wartość logiczną.")
        if value == '':
            value = "0.0"
        if str(re.sub(r'[^-0-9.]+', '', str(value).strip())) == "":
            raise Exception("Wprowadzana wartość nie jest liczbą")
        else:
            amount = str(re.sub(r'[^-0-9.]+', '', str(value).strip()))
            if float(amount) < 0:
                raise Exception("Kwota nie może być mniejsza od zera")
            self.__amount = float(amount)
    @property
    def reciving_priest(self):
        return self.__priest_reciving
    @reciving_priest.getter
    def reciving_priest(self):
        return self.__priest_reciving
    @reciving_priest.setter
    def reciving_priest(self, value) -> str:
        """
                First letter of name and surname. Max. 3 chars (in case of similar abrev.)
                :param value:
                :return:
                """
        if len(value) > 3:
            raise Exception("Przekroczono dopuszczalną ilość znaków (3).")
        result = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())
        self.__priest_reciving = result.upper()[:3]

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
    def date_of_celebration(self, value) -> str:
        """
        Dopuszczalny format daty: "yyyy-mm-dd" lub "dd-mm-yyyy"

        """
        value = str(re.sub(r'[^0-9-]+', '', str(value).strip()))
        ymd = re.compile(r'^(\d){4}-(\d){2}-(\d){2}')
        dmy = re.compile(r'^(\d){2}-(\d){2}-(\d){4}')
        if ymd.match(value) is not None or dmy.match(value) is not None:
            try:
                if value[4] == "-" and value[7]:
                    isNaT = pandas.to_datetime(value, format="%Y-%m-%d", errors='coerce')
                    if isNaT is pandas.NaT:
                        raise Exception("Nie ma takiej daty")
                elif value[2] == "-" and value[5]:
                    ddmmyyyy = value
                    value = ddmmyyyy[6:] + "-" + ddmmyyyy[3:5] + "-" + ddmmyyyy[:2]
                    isNaT = pandas.to_datetime(value, format="%Y-%m-%d", errors='coerce')
                    if isNaT is pandas.NaT:
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
    def hour_of_celebration(self, value) -> str:
        """
        Dopuszczalny format czasu: "HH:MM:SS" lub "HH:MM"

        """
        value = str(re.sub(r'[^0-9:]+', '', str(value).strip()))
        result = True
        dformat = 'hhmmss'
        HHmm = re.compile(r'^(\d){2}:(\d){2}')
        HHmmss = re.compile(r'^(\d){2}:(\d){2}:(\d){2}')
        if HHmm.match(value) is not None or HHmmss.match(value) is not None:
            try:
                if len(value) == 8:
                    result = bool(datetime.datetime.strptime(value, "%H:%M:%S"))
                elif len(value) == 5:
                    dformat = "hhmm"
                    result = bool(datetime.datetime.strptime(value, "%H:%M"))
            except ValueError:
                result = False
            finally:
                if result:
                    if dformat == "hhmm":
                        self.__celebration_hour = value
                    else:
                        self.__celebration_hour = value[0:6]
                else:
                    raise Exception("Podaj właściwy format godziny")
        else:
            raise Exception("Podaj właściwy format godziny")

    @property
    def type_of_mass(self):
        return self.__celebration_type
    @type_of_mass.getter
    def type_of_mass(self):
        return self.__celebration_type
    @type_of_mass.setter
    def type_of_mass(self, value) -> str:
        if isinstance(value, bool):
            raise Exception("Podano wartość logiczną.")
        if value is None:
            value = ""
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
            raise Exception("Nie boolowski typ danych")

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
            raise Exception("Nie boolowski typ danych")
