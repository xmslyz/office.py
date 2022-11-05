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

    def show_personal_data(self):
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
