import calendar
import datetime
import random
import time

from Counters import StipendsCounter as sc
import Database.db_builder as dbb
import Database.db_filler as dbf
import Database.db_searcher as dbs
from Random_Generator import random_values_generator as rvg
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month


def main():
    print("---------------------------------------------------------")
    """ Tworzenie bazy danych """
    # myDB = dbb.Database()
    # myDB.database_creator()

    """ Wypełnianie tabeli randomowymi danymi """
    # database = DatabaseCalendarFiller()
    # Month(2022, 11).addRecords(database, 8, 6)

    s_counter = sc.ComputingStipends()
    print(s_counter.sum_all_stipends())
    print(s_counter.sum_of_paid_intentions())
    print(s_counter.sum_of_aplicated_stipends())
    print(s_counter.bool_if_application())
    print(s_counter.evaluate_paid_masses_vs_application())
    print(s_counter.mediana_stipends())

    print("---------------------------------------------------------")
    print("Program zakończył działanie")


if __name__ == '__main__':
    main()
