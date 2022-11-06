import datetime
import re


class EmployeeIdentity:

    def __init__(self):
        self.__type = "Dane osobowe"
        self.__name = None
        self.__surname = None
        self.__shortname = None
        self.__abreviation = None
        self.__function = None
        self.__taxes = None

    def show_records(self):
        print(f"{self.__type}:\n"
              f"Imię i Nazwisko: {self.__name} {self.__surname} - {self.__function}\n"
              f"Alias: {self.__shortname} | inicjały [{self.__abreviation}]\n"
              f"Należności: {self.__taxes}")

    @property
    def type(self):
        return self.__type
    @type.getter
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name
    @name.getter
    def name(self):
        return self.__name
    @name.setter
    def name(self, value) -> str:
        self.__name = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def surname(self):
        return self.__surname
    @surname.getter
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value) -> str:
        self.__surname = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def abreviation(self):
        return self.__abreviation
    @abreviation.getter
    def abreviation(self):
        return self.__abreviation
    @abreviation.setter
    def abreviation(self, value) -> str:
        self.__abreviation = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def shortname(self):
        return self.__shortname
    @shortname.getter
    def shortname(self):
        return self.__shortname
    @shortname.setter
    def shortname(self, value) -> str:
        self.__shortname = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def function(self):
        return self.__function
    @function.getter
    def function(self):
        return self.__function
    @function.setter
    def function(self, value) -> str:
        self.__function = re.sub(r'[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+', '', str(value).strip())

    @property
    def taxes(self):
        return self.__taxes
    @taxes.getter
    def taxes(self):
        return self.__taxes
    @taxes.setter
    def taxes(self, value) -> str:
        self.__taxes = re.sub(r'[^0-9,.]+', '', str(value))


class EmployeeCollations:
    def __init__(self):
        self.__uniqueID = None
        self.__type = "CashFlow"
        self.__collation_date = None
        self.__intention_amount = None
        self.__intention_sum = None
        self.__bination_amount = None
        self.__bination_sum = None
        self.__pars = None
        self.__pretax = None
        self.__taxes = None
        self.__receival = None
        self.__net = None

    def show_records(self):
        print("")

    @property
    def type(self):
        return self.__type
    @type.getter
    def type(self):
        return self.__type

    @property
    def collation_date(self):
        return self.__collation_date
    @collation_date.getter
    def collation_date(self):
        formated_date = self.__collation_date
        return formated_date
    @collation_date.setter
    def collation_date(self, value):
        """
        "yyyy-mm" format
        """
        format = "%Y-%m"
        result = True
        if value is None:
            value = "2022-01"
        try:
            result = bool(datetime.datetime.strptime(value, format))
        except ValueError:
            result = False
        finally:
            print(result)
            if result:
                self.__collation_date = value
            else:
                print("Wrong [date] format")

    @property
    def intention_amount(self):
        return self.__intention_amount
    @intention_amount.getter
    def intention_amount(self):
        return self.__intention_amount
    @intention_amount.setter
    def intention_amount(self, value) -> str:
        self.__intention_amount = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def intention_sum(self):
        return self.__intention_sum
    @intention_sum.getter
    def intention_sum(self):
        return self.__intention_sum
    @intention_sum.setter
    def intention_sum(self, value) -> str:
        self.__intention_sum = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def bination_amount(self):
        return self.__bination_amount
    @bination_amount.getter
    def bination_amount(self):
        return self.__bination_amount
    @bination_amount.setter
    def bination_amount(self, value) -> str:
        self.__bination_amount = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def bination_sum(self):
        return self.__bination_sum
    @bination_sum.getter
    def bination_sum(self):
        return self.__bination_sum
    @bination_sum.setter
    def bination_sum(self, value) -> str:
        self.__bination_sum = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def pars(self):
        return self.__pars
    @pars.getter
    def pars(self):
        return self.__pars
    @pars.setter
    def pars(self, value) -> str:
        self.__pars = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def pretax(self):
        return self.__pretax
    @pretax.getter
    def pretax(self):
        return self.__pretax
    @pretax.setter
    def pretax(self, value) -> str:
        self.__pretax = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def taxes(self):
        return self.__taxes
    @taxes.getter
    def taxes(self):
        return self.__taxes
    @taxes.setter
    def taxes(self, value) -> str:
        self.__taxes = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def receival(self):
        return self.__receival
    @receival.getter
    def receival(self):
        return self.__receival
    @receival.setter
    def receival(self, value) -> str:
        self.__receival = re.sub(r'[^0-9,.]+', '', str(value))

    @property
    def net(self):
        return self.__net
    @net.getter
    def net(self):
        return self.__net
    @net.setter
    def net(self, value) -> str:
        self.__net = re.sub(r'[^0-9,.]+', '', str(value))
