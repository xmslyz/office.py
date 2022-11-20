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

    def __repr__(self):
        print(
            f"EmployeeIdentity:\n"
            f"type -> {self.__type}\t\n"
            f"name -> {self.__name}\t\n"
            f"surname -> {self.__surname}\t\n"
            f"shortname -> {self.__shortname}\t\n"
            f"abreviation -> {self.__abreviation}\t\n"
            f"function -> {self.__function}\t\n"
            f"taxes -> {self.__taxes}\t\n"
        )

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
        self.__name = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def surname(self):
        return self.__surname

    @surname.getter
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value) -> str:
        self.__surname = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def abreviation(self):
        return self.__abreviation

    @abreviation.getter
    def abreviation(self):
        return self.__abreviation

    @abreviation.setter
    def abreviation(self, value) -> str:
        self.__abreviation = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def shortname(self):
        return self.__shortname

    @shortname.getter
    def shortname(self):
        return self.__shortname

    @shortname.setter
    def shortname(self, value) -> str:
        self.__shortname = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def function(self):
        return self.__function

    @function.getter
    def function(self):
        return self.__function

    @function.setter
    def function(self, value) -> str:
        self.__function = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value).strip()
        )

    @property
    def taxes(self):
        return self.__taxes

    @taxes.getter
    def taxes(self):
        return self.__taxes

    @taxes.setter
    def taxes(self, value) -> str:
        self.__taxes = re.sub(r"[^0-9,.]+", "", str(value))


class EmployeeCollations:
    def __init__(self):
        self.__uniqueID = None
        self.__type = "CashFlow"
        self.__monthly_stmt_date = None
        self.__intention_amount = None
        self.__intention_sum = None
        self.__bination_amount = None
        self.__bination_sum = None
        self.__pars = None
        self.__pretax = None
        self.__taxes = None
        self.__receival = None
        self.__net = None

    def __repr__(self):
        print(
            f"EmployeeCollations:\n"
            f"uniqueID -> {self.__uniqueID}\t\n"
            f"type -> {self.__type}\t\n"
            f"collation_date -> {self.__monthly_stmt_date}\t\n"
            f"intention_amount -> {self.__intention_amount}\t\n"
            f"intention_sum -> {self.__intention_sum}\t\n"
            f"bination_amount -> {self.__bination_amount}\t\n"
            f"bination_sum -> {self.__bination_sum}\t\n"
            f"pars -> {self.__pars}\t\n"
            f"pretax -> {self.__pretax}\t\n"
            f"taxes -> {self.__taxes}\t\n"
            f"receival -> {self.__receival}\t\n"
            f"net -> {self.__net}"
        )

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value) -> str:
        self.__type = re.sub(
            r"[^-\' A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", str(value)
        )

    @type.getter
    def type(self):
        return self.__type

    @property
    def monthly_stmt_date(self):
        return self.__monthly_stmt_date

    @monthly_stmt_date.getter
    def monthly_stmt_date(self):
        formated_date = self.__monthly_stmt_date
        return formated_date

    @monthly_stmt_date.setter
    def monthly_stmt_date(self, value):
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
            if result:
                self.__monthly_stmt_date = value
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
        self.__intention_amount = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def intention_sum(self):
        return self.__intention_sum

    @intention_sum.getter
    def intention_sum(self):
        return self.__intention_sum

    @intention_sum.setter
    def intention_sum(self, value) -> str:
        self.__intention_sum = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def bination_amount(self):
        return self.__bination_amount

    @bination_amount.getter
    def bination_amount(self):
        return self.__bination_amount

    @bination_amount.setter
    def bination_amount(self, value) -> str:
        self.__bination_amount = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def bination_sum(self):
        return self.__bination_sum

    @bination_sum.getter
    def bination_sum(self):
        return self.__bination_sum

    @bination_sum.setter
    def bination_sum(self, value) -> str:
        self.__bination_sum = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def pars(self):
        return self.__pars

    @pars.getter
    def pars(self):
        return self.__pars

    @pars.setter
    def pars(self, value) -> str:
        self.__pars = re.sub(r"[^0-9,.-]+", "", str(value))

    @property
    def pretax(self):
        return self.__pretax

    @pretax.getter
    def pretax(self):
        return self.__pretax

    @pretax.setter
    def pretax(self, value) -> str:
        self.__pretax = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def taxes(self):
        return self.__taxes

    @taxes.getter
    def taxes(self):
        return self.__taxes

    @taxes.setter
    def taxes(self, value) -> str:
        self.__taxes = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def receival(self):
        return self.__receival

    @receival.getter
    def receival(self):
        return self.__receival

    @receival.setter
    def receival(self, value) -> str:
        self.__receival = re.sub(r"[^0-9,.]+", "", str(value))

    @property
    def net(self):
        return self.__net

    @net.getter
    def net(self):
        return self.__net

    @net.setter
    def net(self, value) -> str:
        self.__net = re.sub(r"[^0-9,.-]+", "", str(value))
