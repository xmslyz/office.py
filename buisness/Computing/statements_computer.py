import buisness.Database.Geter
import buisness.Database.SQLConnector
from buisness.Database.SQLConnector import Connection
import buisness.Computing.tax_computer
from buisness.Input import Caster as cast
from buisness.Computing.pars_computer import pars_na_osobe


class Collation(Connection):
    """Conn_details : "intentions" """

    BINATION = float(
        buisness.Database.SQLConnector.KeyGeter.constants_getter("bin")
    )
    GUEST = float(
        buisness.Database.SQLConnector.KeyGeter.constants_getter("inv")
    )

    def __init__(self, qdate):

        super().__init__()
        self.qdate = qdate
        self.counted_mediana = None

    def record_by_id(self, qid):
        """
        Looks for record by it's id

        :param qid: record's id.
        :return: database row: where [0] is qid.

        :exception when there's no id: "No record with this id"
        """

        qid = cast.string_2_string(qid)
        if qid:
            stmt = f'SELECT * FROM intentions WHERE id IS ("{qid}");'
            query = self.sql_querry(stmt)
            if query:
                return query
            else:
                raise Exception("No record with this id")
        else:
            raise Exception("Wrong input type")

    def records_in_qdate__list(self):
        """
        Searching for all records where "celebration_date" == queried date

        :return: list: complete row
        """

        stmt = "SELECT * FROM intentions;"

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def binations__list(self):
        """
        Searching for all binations where "celebration_date" == queried date

        :return: list: complete row
        """

        stmt = 'SELECT * FROM intentions WHERE first_mass IS ("0");'

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def gregorian__list(self):
        """
        Searching for all gregorian masses where "celebration_date" ==
        queried date

        :return: list: complete row
        """

        stmt = 'SELECT * FROM intentions WHERE gregorian IS ("1");'

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def aplicated_stipends__list(self):
        """
        Searching for all celebrated masses where "celebration_date" ==
        queried date

        :return: list: complete row
        """

        stmt = 'SELECT * FROM intentions WHERE celebrated_by IS NOT ("");'

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def paid_not_applicated__list(self):
        """
        Searching for all mases paid but not celebrated where
        "celebration_date" == queried date

        :return: list: complete row
        """

        stmt = (
            "SELECT * FROM intentions WHERE "
            'celebrated_by LIKE ("") '
            'AND amount LIKE ("%.%");'
        )

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def not_paid_but_aplicated__list(self):
        """
        Searching for all not paid mases but celebrated where
        "celebration_date" == queried date

        :return: list: complete row
        """

        stmt = (
            "SELECT * FROM intentions WHERE "
            'celebrated_by LIKE ("_%") '
            'AND amount IS ("")'
            'AND gregorian IS ("0");'
        )

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def not_paid_nor_aplicated__list(self):
        """
        Searching for all not paid and not celebrated masses where
        "celebration_date" == queried date

        :return: list: complete row
        """

        stmt = (
            "SELECT * FROM intentions WHERE "
            'celebrated_by IS ("") '
            'AND amount IS ("")'
            'AND gregorian IS ("0");'
        )

        return [
            x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)
        ]

    def amount_of_all_paid(self):
        """
        Amount of paid masses

        :return: int
        """

        stmt = "SELECT * FROM intentions WHERE " 'amount IS NOT ("");'

        return len(
            [x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)]
        )

    def amount_of_binations(self):
        """
        Amount of binations

        :return: int
        """

        return len(self.binations__list())

    def amount_of_all_gregorian(self):
        """
        Amount of gregorian masses

        :return: int
        """

        stmt = "SELECT * FROM intentions WHERE " 'gregorian IS ("1");'

        return len(
            [x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)]
        )

    def amount_of_guest_masses(self):
        """
        Amount of masses celebrated by guests

        :return: int
        """

        # gets all who celebrated but not in employees database
        uid = buisness.Database.Geter.GuestsGetter()
        uid.get_conn_details("intentions")
        result = uid.get_guests(self.qdate)

        return sum([int(x[1]) for x in result])

    def amount_of_aplicated(self):
        """
        Amount of all aplicated masses

        :return: int
        """

        return len(self.aplicated_stipends__list())

    def sum_of_all_recived(self):
        """
        Sum of all recived stipends

        :return: float
        """
        stmt = "SELECT * FROM intentions;"

        result = [
            x[2]
            for x in self.sql_querry(stmt)
            if x[5].startswith(self.qdate) and isinstance(x[2], float)
        ]
        return float(sum(result))

    def sum_of_all_gregorian(self):
        """
        Sum of recived gregorian stipends

        :return: float
        """
        stmt = "SELECT * FROM intentions " 'WHERE gregorian IS "1";'

        result = [
            x[2]
            for x in self.sql_querry(stmt)
            if x[5].startswith(self.qdate) and isinstance(x[2], float)
        ]
        return float(sum(result))


class Compute(Collation):
    """Conn_details : "intentions" """

    def mediana(self):
        """
        Computes average stipend

        :return: averege
        """

        # net sum
        netsum = (
            self.sum_of_all_recived()
            - self.sum_of_all_gregorian()
            - self.sum_of_binations()
            - self.sum_for_guests()
        )

        # adding gregorian sum
        total = netsum + self.gregorian_sum_of_medianas()

        # when is not negative raises exeptions
        if (self.amount_of_aplicated() - self.amount_of_binations()) < 0:
            raise Exception(
                "Ilość zaaplikowanych intencji nie może być ujemna"
            )
        else:
            divider = (
                self.amount_of_aplicated()
                - self.amount_of_binations()
                - self.amount_of_guest_masses()
            )
            if divider > 0:
                self.counted_mediana = round((total / divider), 2)
                return round((total / divider), 2)
            elif divider == 0:
                return 0
            else:
                raise ZeroDivisionError(
                    "Ilość zaaplikowanych intencji nie " "może być ujemna"
                )

    def sum_of_binations(self):
        """
        Takes amount of binantions and multipy by BINATION const.

        :return: float
        """

        return float(self.amount_of_binations() * self.BINATION)

    def gregorian_mediana(self):
        """
        Takes the sum of gregorian stipends and divides it by amount of
        celebrated gregorian masses

        :return: float
        """
        if self.amount_of_all_gregorian() > 0:
            return self.sum_of_all_gregorian() / self.amount_of_all_gregorian()
        elif self.amount_of_all_gregorian() == 0:
            return 0
        else:
            raise ZeroDivisionError("Nie może być ujemna")

    def gregorian_sum_of_medianas(self):
        """
        Multiplies gregorian mediana by amount of all gregorian

        :return: float
        """

        return self.gregorian_mediana() * self.amount_of_all_gregorian()

    def sum_for_guests(self):
        """
        Multiplies guest-celebrated masses by GUEST constant

        :return: float
        """

        return round((self.amount_of_guest_masses() * self.GUEST), 2)


class EmployeeCollation(Collation):
    """Collator for employee (lists, sums & ammounts).

    Conn_details : "intentions".
    """

    def __init__(self, qdate, who_recived):
        """
        Constructor

        :param qdate: date scope in "yyyy-mm" format
        :param who_recived: abreviations of "who recived" from intentions table
        """

        super().__init__(qdate)
        self.who_recived = who_recived

    def list_of_recieved_by_a_priest(self):
        """
        List of all intentions recived by employee

        :return: float
        """

        stmt = (
            f"SELECT * FROM intentions "
            f'WHERE priest_reciving IS ("{self.who_recived}");'
        )

        return [
            x
            for x in self.sql_querry(stmt)
            if x[5].startswith(self.qdate) and isinstance(x[2], float)
        ]

    def sum_of_recieved_by_a_priest(self):
        """
        Sum of all money recived

        :return: float
        """

        return sum([x[2] for x in self.list_of_recieved_by_a_priest()])

    def amount_of_all_masses_applied_by_a_priest(self):
        """
        Amount of all masses aplied in qdate scope

        :return: int
        """

        stmt = (
            f"SELECT * FROM intentions "
            f'WHERE celebrated_by IS ("{self.who_recived}");'
        )

        return len(
            [x for x in self.sql_querry(stmt) if x[5].startswith(self.qdate)]
        )

    def amount_of_first_masses_applied_by_a_priest(self):
        """
        Amount of all first mass in a day aplied in qdate scope

        :return: float
        """

        stmt = (
            f"SELECT * FROM intentions "
            f'WHERE celebrated_by IS ("{self.who_recived}") '
            f'AND first_mass IS "1";'
        )

        return len(
            [
                x[2]
                for x in self.sql_querry(stmt)
                if x[5].startswith(self.qdate)
            ]
        )

    def amount_of_bination_applied_by_a_priest(self):
        """
        Amount of all next masses in a day aplied in qdate scope

        :return: float
        """

        stmt = (
            f"SELECT * FROM intentions "
            f'WHERE celebrated_by IS ("{self.who_recived}") '
            f'AND first_mass IS "0";'
        )

        return len(
            [
                x[2]
                for x in self.sql_querry(stmt)
                if x[5].startswith(self.qdate)
            ]
        )


class ComputeEmployee(EmployeeCollation):
    """Computer for employee.

    Conn_details : "intentions".
    """

    def __init__(self, qdate, who_recived, compute=None):
        """

        :param qdate: date scope in "yyyy-mm" format
        :param who_recived: abreviations of "who recived" from intentions table
        :param compute: object of Compute class
        """

        super().__init__(qdate, who_recived)
        self.compute = compute

    def quota_for_priest(self):
        """
        Multiplication of first masses by mediana

        :return: float
        """

        med = self.compute.mediana()
        if med > 0:
            return round(
                self.amount_of_first_masses_applied_by_a_priest() * med, 2
            )
        else:
            raise Exception("Średnia intencja nie może być ujemna")

    def bination_quota_for_priest(self):
        """
        Multiplication of all binations and BINATION constant

        :return: float
        """

        bination = (
            self.amount_of_all_masses_applied_by_a_priest()
            - self.amount_of_first_masses_applied_by_a_priest()
        )

        return round(float(bination * self.BINATION), 2)

    def total_wage_for_priest(self):
        """
        Sum of quota and binations

        :return: float
        """

        return round(
            self.quota_for_priest() + self.bination_quota_for_priest(), 2
        )

    def net_for_priest(self):
        """
        Salary with 'pars' ('taxes' and 'recived' subtracted)

        :return: float
        """

        # geting unique id
        uid = buisness.Database.Geter.UniqueIDGetter()
        uid.get_conn_details("testemployees")

        # geting employee's total tax
        tax = buisness.Computing.tax_computer.GeneralStmt(self.qdate)
        tax.get_conn_details("testemployees")
        total_tax = tax.sum_taxes_for_employee(
            uid.get_uniqueID(self.who_recived)
        )

        # total (net) salary
        total = (
            self.total_wage_for_priest() + self.pars_for_priest() - total_tax
        ) - self.sum_of_recieved_by_a_priest()

        return round(total, 2)

    def pars_for_priest(self):
        """
        Counting pars for priest

        :return: float
        """
        return pars_na_osobe()
