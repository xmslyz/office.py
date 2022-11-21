import re
import pandas


class OfficeRecord:
    def __init__(self):
        self.__o_type = "Opłata kancelaryjna"
        self.__o_amount = 0
        self.__o_reciving = None
        self.__o_reciving_date = None
        self.__o_what_for = None
        self.__o_book_ref = None
        self.__o_celebration_date = None

    @property
    def type(self):
        return self.__o_type

    @type.getter
    def type(self):
        return self.__o_type

    @property
    def amount(self):
        return self.__o_amount

    @amount.getter
    def amount(self):
        return self.__o_amount

    @amount.setter
    def amount(self, value) -> str:
        if isinstance(value, bool):
            raise Exception("Podano wartość logiczną.")
        if value == "":
            value = "0.0"
        if str(re.sub(r"[^-0-9.]+", "", str(value).strip())) == "":
            raise Exception("Wprowadzana wartość nie jest liczbą")
        else:
            amount = str(re.sub(r"[^-0-9.]+", "", str(value).strip()))
            if float(amount) < 0:
                raise Exception("Kwota nie może być mniejsza od zera")
            self.__o_amount = float(amount)

    @property
    def reciving_priest(self):
        return self.__o_reciving

    @reciving_priest.getter
    def reciving_priest(self):
        return self.__o_reciving

    @reciving_priest.setter
    def reciving_priest(self, value) -> str:
        """
        First letter of name and surname.

        Max. 3 chars (in case of similar abrev.)

        :param value:
        :return:
        """
        if len(value) > 3:
            raise Exception("Przekroczono dopuszczalną ilość znaków (3).")
        result = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )
        self.__o_reciving = result.upper()[:3]

    @property
    def date_of_celebration(self):
        return self.__o_celebration_date

    @date_of_celebration.getter
    def date_of_celebration(self):
        formated_date = self.__o_celebration_date
        return formated_date

    @date_of_celebration.setter
    def date_of_celebration(self, value) -> str:
        """
        Dopuszczalny format daty: "yyyy-mm-dd" lub "dd-mm-yyyy"

        """
        value = str(re.sub(r"[^0-9-]+", "", str(value).strip()))
        ymd = re.compile(r"^(\d){4}-(\d){2}-(\d){2}")
        dmy = re.compile(r"^(\d){2}-(\d){2}-(\d){4}")
        if ymd.match(value) is not None or dmy.match(value) is not None:
            try:
                if value[4] == "-" and value[7]:
                    isNaT = pandas.to_datetime(
                        value, format="%Y-%m-%d", errors="coerce"
                    )
                    if isNaT is pandas.NaT:
                        raise Exception("Nie ma takiej daty")
                elif value[2] == "-" and value[5]:
                    ddmmyyyy = value
                    value = (
                        ddmmyyyy[6:] + "-" + ddmmyyyy[3:5] + "-" + ddmmyyyy[:2]
                    )
                    isNaT = pandas.to_datetime(
                        value, format="%Y-%m-%d", errors="coerce"
                    )
                    if isNaT is pandas.NaT:
                        raise Exception("Nie ma takiej daty")
            finally:
                self.__o_celebration_date = value
        else:
            raise Exception("Podaj właściwy format daty")

    @property
    def date_of_reciving(self):
        return self.__o_reciving_date

    @date_of_reciving.getter
    def date_of_reciving(self):
        formated_date = self.__o_reciving_date
        return formated_date

    @date_of_reciving.setter
    def date_of_reciving(self, value) -> str:
        """
        Dopuszczalny format daty: "yyyy-mm-dd" lub "dd-mm-yyyy"

        """
        value = str(re.sub(r"[^0-9-]+", "", str(value).strip()))
        ymd = re.compile(r"^(\d){4}-(\d){2}-(\d){2}")
        dmy = re.compile(r"^(\d){2}-(\d){2}-(\d){4}")
        if ymd.match(value) is not None or dmy.match(value) is not None:
            try:
                if value[4] == "-" and value[7]:
                    isNaT = pandas.to_datetime(
                        value, format="%Y-%m-%d", errors="coerce"
                    )
                    if isNaT is pandas.NaT:
                        raise Exception("Nie ma takiej daty")
                elif value[2] == "-" and value[5]:
                    ddmmyyyy = value
                    value = (
                            ddmmyyyy[6:] + "-" + ddmmyyyy[
                                                 3:5] + "-" + ddmmyyyy[:2]
                    )
                    isNaT = pandas.to_datetime(
                        value, format="%Y-%m-%d", errors="coerce"
                    )
                    if isNaT is pandas.NaT:
                        raise Exception("Nie ma takiej daty")
            finally:
                self.__o_reciving_date = value
        else:
            raise Exception("Podaj właściwy format daty")

    @property
    def kind(self):
        return self.__o_what_for

    @kind.getter
    def kind(self):
        return self.__o_what_for

    @kind.setter
    def kind(self, value) -> str:
        if isinstance(value, bool):
            raise Exception("Podano wartość logiczną.")
        if value is None:
            value = ""
        self.__o_what_for = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def reference(self):
        return self.__o_book_ref

    @reference.getter
    def reference(self):
        return self.__o_book_ref

    @reference.setter
    def reference(self, value) -> str:
        if isinstance(value, bool):
            raise Exception("Podano wartość logiczną.")
        if value is None:
            value = ""
        self.__o_book_ref = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ/0-9]+", "", str(value).strip()
        )
