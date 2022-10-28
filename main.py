import datetime
import random
import time

import Database.db_builder as db
import Database.db_filler as dbf
from Random_Generator import random_values_generator as rvg


def main():

    # myDB = db.Database()
    # myDB.show_db_details()
    # myDB.database_creator()

    myDBfiller = dbf.DatabaseFiller()
    myDBfiller.make_connection(myDBfiller.filler_with_dbObject)


if __name__ == '__main__':
    main()
