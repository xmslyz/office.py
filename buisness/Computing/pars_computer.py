import buisness.Income.ManageOffice
import buisness.Database.Geter
from buisness.Computing.kozi_computer import OutcomesComputer as oc
from gui.InsertTab import KOZI as kozi


def pars_na_osobe():
    # geting sum of incomes to pars
    pars_income = sum(
        [x[0] for x in buisness.Income.ManageOffice.count_amount_to_pars()]
    )

    # - fees and taxes
    ocom = oc()
    what_is_left_from_pars = pars_income - \
                             ocom.sum_kozi(kozi.get_monthly_burden()) - \
                                ocom.count_food_and_cook()

    # geting list of who is cualified to pars
    cualified_empployees = buisness.Database.Geter.IntentionsColsGetter()\
        .get_list_to_pars()

    # geting factor from list
    amount_cualified = (len(cualified_empployees[0]) * 2) + \
                        len(cualified_empployees[1])

    # return quotient
    if what_is_left_from_pars > 0:
        if amount_cualified > 0:
            return round(what_is_left_from_pars / amount_cualified, 2)
        else:
            raise ZeroDivisionError("Ilu do parsu nie może być liczbą ujemną.")
    else:
        return 0
