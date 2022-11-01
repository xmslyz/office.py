import gc
import time

from Database import db_builder as dbb

path = "myPath"
dbname = "m+y-S*Q+L@b'a>s?ye.exe"
table_name = "mojatabelka"


def budowa_bazy_danych():
    mysql = (("type TEXT NOT NULL",),
             ("amount REAL",),
             ("priest_reciving TEXT",),
             ("celebrated_by TEXT",),
             ("celebration_date TEXT",),
             ("celebration_hour TEXT",),
             ("celebration_type TEXT",),
             ("first_mass INTEGER",))
    dbb.DatabaseBuilder.builder(path, dbname, table_name, mysql)


def destrukcja_bazydanych():
    dest = dbb.DatabaseDestructor(path, dbname, table_name)
    dest.database_table_droper()
    gc.collect()
    dest.file_destroyer()
    dest.path_destroyer()


def main():
    budowa_bazy_danych()
    # destrukcja_bazydanych()

    # mm.intro_prompt()
    # mm.menu_main()
    # mm.final_prompt()


if __name__ == '__main__':
    main()
