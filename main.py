import Database.db_builder as dbb
from Counters import StipendsCounter as sc
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month


def main():
    print("---------------------------------------------------------")

    """ Tworzenie bazy danych """
    # myDB = dbb.Database()
    # myDB.database_creator()

    """ Wypełnianie tabeli randomowymi danymi """
    # database = DatabaseCalendarFiller()
    # Month(2022, 11).addRecords(database, 2, 4)

    """ Wyliczenia generalne """
    s_counter = sc.ComputingStipends()
    print("suma przyjętych stypendiów: ", s_counter.sum_all_stipends())
    print("ilość opłaconych mszy: ", s_counter.sum_of_paid_intentions())
    print("ilość odprawionych mszy: ", s_counter.sum_of_aplicated_stipends())
    print("zgodność: ", s_counter.bool_if_application())
    print("różnica w 'zgodności': ", s_counter.evaluate_paid_masses_vs_application())
    print("średnie stypendium: ", s_counter.mediana_stipends())

    """ Wyliczenia dla konkretnego księdza """
    father1 = sc.Priest("p5")
    print("ilość wszystkich odprawionych mszy", father1.number_of_all_masses_applied_by_a_priest())
    print("ilość 'pierwszych':", father1.number_of_first_masses_applied_by_a_priest())
    print("całkowite stypendium: ", father1.quota_for_priest())
    print("binacje", father1.bination_quota_for_priest())

    print("---------------------------------------------------------")
    print("Program zakończył działanie")


if __name__ == '__main__':
    main()
