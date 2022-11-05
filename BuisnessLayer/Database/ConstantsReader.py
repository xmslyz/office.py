from BuisnessLayer.Database import ScanRecords as dbs


def second_mass_constant():
    db_scanner = dbs.RecordsScanner(path="DatabaseLayer\\Constants\\constants.db")
    result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
    return int(result[0][0])


def invited_constant():
    db_scanner = dbs.RecordsScanner(path="DatabaseLayer\\Constants\\constants.db")
    result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
    return int(result[0][0])


