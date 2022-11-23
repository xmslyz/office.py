import buisness.Income.ManageOffice
import buisness.Database.Geter as getme
from buisness.Computing.kozi_computer import OutcomesComputer as oc
from gui.InsertTab import KOZI as kozi


class ParsComputer:

    def pars_for_one(self):
        cualified = self.get_cualified(
            getme.IntentionsColsGetter().get_list_to_pars())
        net_pars = self.get_net()

        return self.quotient(net_pars, cualified)

    def quotient(self, net, cualified):

        # return quotient
        if net > 0:
            if cualified > 0:
                return round(net / cualified, 2)
            else:
                raise ZeroDivisionError("Ilu do parsu "
                                        "nie może być liczbą ujemną.")
        else:
            return 0

    def get_cualified(self, employees):
        # geting factor from list
        if employees:
            return (len(employees[0]) * 2) + len(employees[1])
        else:
            return 0

    def get_gross(self):
        """ geting sum of incomes to pars """

        return sum(
            [x[0] for x in buisness.Income.ManageOffice.count_amount_to_pars()]
        )

    def get_net(self):

        # - fees and taxes
        ocom = oc()

        return self.get_gross() - \
               ocom.sum_kozi(kozi.get_monthly_burden()) - \
               ocom.count_food_and_cook()
