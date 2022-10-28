import time

import Database.db_builder as db
from Random_Generator import random_values_generator as rvg


def main():
    # rvg.random_values_generator()
    myDB = db.Database()
    myDB.show_db_details()
    myDB.database_creator()


if __name__ == '__main__':
    main()
