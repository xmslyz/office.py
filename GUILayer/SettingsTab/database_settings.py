from BuisnessLayer.Database import ScanRecords as dbs


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
        return "collations"
    elif x == 4:
        return "pars"
    elif x == 5:
        return "general_collation"
    elif x == 6:
        return "x"
    elif x == 7:
        return "y"
    else:
        return x


def constants_getter(const):
    db_scanner = dbs.RecordsScanner(tbl_num=1, dbnm_num=2, path_num=2)
    result = 0
    if const == "bin":
        result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
    elif const == "inv":
        result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
    return int(result[0][0])
