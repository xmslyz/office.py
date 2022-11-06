import gc
import os
from BuisnessLayer.Database import Operator as dbb, AtributesSetter as dbs


class PLUG_database_operator:

    def budowa_bazy_danych_intentions(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "intentions"
        mysql = f"CREATE TABLE IF NOT EXISTS {table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"type TEXT NOT NULL DEFAULT 'Stypendium mszalne', " \
                f"amount REAL DEFAULT 0," \
                f"priest_reciving TEXT," \
                f"celebrated_by TEXT," \
                f"celebration_date TEXT," \
                f"celebration_hour TEXT," \
                f"celebration_type TEXT," \
                f"gregorian INTEGER DEFAULT 0," \
                f"first_mass INTEGER DEFAULT 1);"
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")

    def budowa_bazy_danych_collations(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "collation"
        mysql = f"CREATE TABLE IF NOT EXISTS {table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Zestawienie', " \
                f"collation_date TEXT, " \
                f"intention_amount INTEGER, " \
                f"intention_sum REAL, " \
                f"bination_amount INTEGER, " \
                f"bination_sum REAL, " \
                f"pars REAL, " \
                f"pretax REAL, " \
                f"taxes REAL, " \
                f"receival REAL, " \
                f"net REAL);"
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")

    def budowa_bazy_danych_employee(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "employees"
        mysql = f"CREATE TABLE IF NOT EXISTS {table_name} " \
                f"(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                f"uniqueID INTEGER NOT NULL, " \
                f"type TEXT NOT NULL DEFAULT 'Dane osobowe', " \
                f"name TEXT, " \
                f"surname TEXT, " \
                f"shortname TEXT, " \
                f"abreviation TEXT, " \
                f"function TEXT, " \
                f"taxes TEXT);"
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")

    def usuniecie_tabeli_intentions(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "intentions"
        mysql = f'DROP TABLE IF EXISTS {table_name}'
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")
        gc.collect()

    def usuniecie_tabeli_collations(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "collation"
        mysql = f'DROP TABLE IF EXISTS {table_name}'
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")
        gc.collect()

    def usuniecie_tabeli_list(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        table_name = "employees"
        mysql = f'DROP TABLE IF EXISTS {table_name}'
        bu = dbb.DatabaseConstructor(path, dbname, table_name)
        bu.db_constructor(mysql, "")
        gc.collect()

    def file_employee_destroyer(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        seti = dbs.DBSettings()
        seti.db_path = path
        seti.db_name = dbname
        seti.db_full_path = ""
        try:
            os.remove(os.path.join(seti.db_full_path)) if os.path.exists(seti.db_full_path) else None
            print("Plik usunięty")
        except PermissionError:
            print("Plik nie może zostać usunięty, ponieważ nie można uzyskać dostępu do pliku.")

    def file_masses_destroyer(self):
        path = "DatabaseLayer\\SQLDataBase\\"
        dbname = "sofa"
        seti = dbs.DBSettings()
        seti.db_path = path
        seti.db_name = dbname
        seti.db_full_path = ""
        try:
            os.remove(os.path.join(seti.db_full_path)) if os.path.exists(seti.db_full_path) else None
            print("Plik usunięty")
        except PermissionError:
            print("Plik nie może zostać usunięty, ponieważ nie można uzyskać dostępu do pliku.")


