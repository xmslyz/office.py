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
    # myDB.show_db_details()
    # myDB.database_creator()

    """ Tworzenie tabeli """
    # myDBfiller = dbf.DatabaseFiller()
    # myDBfiller.filler_with_dbObject(1, 4)

    """ Wypełnianie tabeli randomowymi danymi """
    # database = DatabaseCalendarFiller()
    # Month(2022, 11).addRecords(database, 8, 6)
    # print(database.getData())

    s_counter = sc.ComputingStipends()
    suma = 0
    for _ in s_counter.list_of_stipends_recieved_by_a_priest('SELECT amount FROM main_table WHERE priest_reciving IS "p1"'):
        suma += sum(_)
    print(suma)

    print("---------------------------------------------------------")
    print("Program zakończył działanie")


if __name__ == '__main__':
    main()
