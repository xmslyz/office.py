import gc
import sqlite3

import Counters.StipendsCounter
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month
from Database import db_builder as dbb
from Database import db_searcher as dbs


class DBhelper:
    # DEFAULTOWE NAZWY BAZY DANEJ, TABELI I KATAOGÓW
    path = "Files\\Databases"
    dbname = "default"
    table_name = "intentions"
    def budowa_bazy_danych(self):
        mysql = (("type TEXT NOT NULL DEFAULT 'Stypendium mszalne'",),
                 ("amount REAL DEFAULT 0",),
                 ("priest_reciving TEXT",),
                 ("celebrated_by TEXT",),
                 ("celebration_date TEXT",),
                 ("celebration_hour TEXT",),
                 ("celebration_type TEXT",),
                 ("celebration_type TEXT",),
                 ("gregorian INTEGER DEFAULT 0",),
                 ("first_mass INTEGER DEFAULT 1",))
        dbb.DatabaseBuilder.builder(self.path, self.dbname, self.table_name, mysql)

    def wypelnienie_bd(self, my_path, my_table):
        database = DatabaseCalendarFiller(my_path)
        try:
            Month(2022, 11).addRecords(my_table, database, 2, 3)
        except sqlite3.OperationalError:
            print("Tabela nie znajduje się w bazie danych.")

    def destrukcja_bazydanych(self):
        dest = dbb.DatabaseDestructor(self.path, self.dbname, self.table_name)
        dest.database_table_droper()
        gc.collect()
        dest.file_destroyer()
        dest.path_destroyer()


def main():
    print("Hi World!")
    db_query = dbs.DatabaseSearcher(path="tests\\test.db", table_name="test")
    ssc = Counters.StipendsCounter.ComputingStipends("test", scanner=db_query)
    print(ssc.sum_of_all_recived())
    print(ssc.list_of_all_recived())
    print(ssc.amount_of_aplicated())
    print(ssc.amount_of_all_paid())
    print(ssc.mediana())
    print(ssc.amount_of_binations())
    print(ssc.list_of_binations())
    print(ssc.sum_of_binations())
    print(ssc.list_of_all_gregorian())
    print(ssc.amount_of_all_gregorian())
    print(ssc.sum_of_all_gregorian())
    print(ssc.gregorian_mediana())
    print(ssc.gregorian_sum_of_medianas())
    print(ssc.list_of_aplicated_stipends())
    print(ssc.amount_of_aplicated())
    print(ssc.not_paid_aplicated())
    print(ssc.not_paid_aplicated())
    print(ssc.not_paid_not_aplicated())
    print("\n")

    for x in range(1, 6):
        sp = Counters.StipendsCounter.Priest("test", scanner=db_query, who_recived=f"p{x}")

        print(f"p{x}")
        print(sp.list_of_recieved_by_a_priest())
        print(sp.sum_of_recieved_by_a_priest())
        print(sp.amount_of_all_masses_applied_by_a_priest())
        print(sp.amount_of_first_masses_applied_by_a_priest())
        print(sp.amount_of_bination_applied_by_a_priest())
        print(sp.quota_for_priest())
        print(sp.bination_quota_for_priest())
        print(sp.total_wage_for_priest())
        print("\n")


if __name__ == '__main__':
    main()
