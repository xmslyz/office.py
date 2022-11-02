from Database import db_searcher as dbs


def second_mass_constant():
    db_scanner = dbs.DatabaseSearcher()
    result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "binacja";')
    return int(result[0][0])


def invited_constant():
    db_scanner = dbs.DatabaseSearcher()
    result = db_scanner.sql_querry('SELECT value FROM constants WHERE name IS "invited";')
    return int(result[0][0])


