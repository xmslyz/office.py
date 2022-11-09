from buissnes.Database import ScanRecords as dbs
import buissnes.Database.ScanRecords


def db_path_getter(x):
    if x == 1:
        return "DatabaseLayer\\SQLDataBase\\"
    if x == 2:
        return "DatabaseLayer\\Constants\\"


def db_name_getter(x):
    if x == 1:
        return "sofa.db"
    if x == 2:
        return "constants.db"
    else:
        return f"{x}.db"


def db_tablename_getter(x):
    if x == 0:
        return "constants"
    elif x == 1:
        return "intentions"
    elif x == 2:
        return "employees"
    elif x == 3:
        return "monthly_stmt"
    elif x == 4:
        return "general_stmt"
    elif x == 5:
        return "pars"
    elif x == 6:
        return "x"
    elif x == 7:
        return "y"
    else:
        return x


def constants_getter(const):
    db = buissnes.Database.ScanRecords.Connection()
    db.get_conn_details(2, 2, 0)
    result = 0
    if const == "bin":
        result = db.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
    elif const == "inv":
        result = db.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
    return int(result[0][0])
