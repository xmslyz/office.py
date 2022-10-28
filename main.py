import time

import Database.db_builder as db
import Database.db_filler as dbf
from Random_Generator import random_values_generator as rvg


def main():
    # rvg.random_values_generator()

    # myDB = db.Database()
    # myDB.show_db_details()
    # myDB.database_creator()

    myDBfiller = dbf.DatabaseFiller()
    myDBfiller.make_connection(myDBfiller.qqq)


if __name__ == '__main__':
    main()
