from BuisnessLayer.Database import ScanRecords as dbs


def db_path_getter():
    return "DatabaseLayer\\SQLDataBase\\"


def db_name_getter():
    return "sofa.db"


def db_tablename_getter(x):
    if x == 1:
        return "intentions"
    elif x == 2:
        return "employees"
    elif x == 2:
        return "collations"


def constants_getter(const):
    db_scanner = dbs.RecordsScanner(path="DatabaseLayer\\Constants\\constants.db")
    result = 0
    if const == "bin":
        result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
    elif const == "inv":
        result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
    return int(result[0][0])
