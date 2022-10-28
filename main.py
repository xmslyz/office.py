import datetime
import random
import time

import Database.db_builder as dbb
import Database.db_filler as dbf
import Database.db_searcher as dbs
from Random_Generator import random_values_generator as rvg


def main():
    """ Odkomentować, aby utworzyć bazę danych i tabelę. """
    # myDB = dbb.Database()
    # myDB.show_dbb_details()
    # myDB.database_creator()

    # myDBfiller = dbf.DatabaseFiller()
    # myDBfiller.make_connection(myDBfiller.filler_with_dbObject)

    myDBsearher = dbs.DatabaseSearcher()
    myDBsearher.make_connection(myDBsearher.sql_querry_SELECT__FROM__WHERE__IS__, "amount", "main_table", "celebrated", "p2")


if __name__ == '__main__':
    main()
