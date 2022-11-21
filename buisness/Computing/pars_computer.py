import buisness.Income.ManageOffice
import buisness.Database.Geter


def pars_na_osobe():
    pars_total = sum(
        [x[0] for x in buisness.Income.ManageOffice.count_amount_to_pars()]
    )

    cualified_list = buisness.Database.Geter.IntentionsColsGetter()\
        .get_list_to_pars()

    amount_cualified = (len(cualified_list[0]) * 2) + len(cualified_list[1])

    if pars_total > 0:
        if amount_cualified > 0:
            return round(pars_total / amount_cualified, 2)
        else:
            raise ZeroDivisionError("Ilu do parsu nie może być liczbą ujemną.")
    else:
        return 0
