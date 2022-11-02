import datetime
import gc
from Database import db_searcher as dbs
from Counters import StipendsCounter
from Menu import MainMenu as mm
from Database import db_builder as dbb

# DEFAULTOWE NAZWY BAZY DANEJ, TABELI I KATAOGÓW
path = "Files\\Databases"
dbname = "default"
table_name = "intentions"


def budowa_bazy_danych():
    assert path == "Files\\Databases"
    assert dbname == "default"
    assert table_name == "intentions"

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
    mm.MainMenu.intro_prompt()
    mm.MainMenu.menu_main()
    mm.MainMenu.final_prompt()

    timebefore = datetime.datetime.now()
    # test
    timeafter = datetime.datetime.now()
    print(f"Wykonano w {timeafter - timebefore} s.")


if __name__ == '__main__':
    main()
