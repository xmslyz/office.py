import BuisnessLayer.Database.Builder
import BuisnessLayer.Income.stipend_income
import BuisnessLayer.Database.InsertData
import BuisnessLayer.Employees.Employee


def update_value():
    gui_column = "pars"
    gui_value = "200"
    guiqid = "d6b538c1-a7b6-43ac-bd49-43a38d666ea3"

    # wrzuca dane z obiektu do tabeli
    stip = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
    stip.__repr__()
    stip.update_value(column=gui_column, value=gui_value, qid=guiqid)
