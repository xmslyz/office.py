from collections import Counter

from buisness.Database.SQLConnector import Connection


class KOZI:
    def __init__(self):
        self.conn = Connection()

    def get_office_incomes(self):
        stmt = (
            'SELECT * FROM office '
        )

        result = self.conn.sql_querry(stmt, dblink="office")

        c = [x[5] for x in result]
        print(Counter(c))

        print(sum([x[2] for x in result]))

    def build_kozi_table(self):
        self.__drop_kozi()
        stmt = (
            'CREATE TABLE IF NOT EXISTS kozi ('
            'const INTEGER,'
            'BK INTEGER,'
            'BO INTEGER,'
            'BZ INTEGER,'
            'BI INTEGER,'
            'MK INTEGER,'
            'MO INTEGER,'
            'MZ INTEGER,'
            'MI INTEGER,'
            'FK INTEGER,'
            'FO INTEGER,'
            'FZ INTEGER,'
            'FI INTEGER);'
        )
        self.conn.sql_querry(stmt, dblink="builder")
        self.__set_kozi_const()

    def __set_kozi_const(self):
        values = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        stmt = (
            'INSERT INTO kozi ('
            'const,'
            'BK, BO, BZ, BI,'
            'MK, MO, MZ, MI,'
            'FK, FO, FZ, FI) '
            'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'
        )
        self.conn.sql_querry(stmt, value=values, dblink="kozi")

    def __drop_kozi(self):
        stmt = (
            'DROP TABLE IF EXISTS kozi'
        )
        self.conn.sql_querry(stmt, dblink="kozi")

    def update_kozi(self, val):
        stmt = (
            f'UPDATE kozi SET '
            f'BK = {val.get("b_k")},' 
            f'BO = {val.get("b_o")},' 
            f'BZ = {val.get("b_z")},' 
            f'BI = {val.get("b_i")},' 
            f'MK = {val.get("m_k")},' 
            f'MO = {val.get("m_o")},' 
            f'MZ = {val.get("m_z")},' 
            f'MI = {val.get("m_i")},' 
            f'FK = {val.get("f_k")},' 
            f'FO = {val.get("f_o")},' 
            f'FZ = {val.get("f_z")},' 
            f'FI = {val.get("f_i")} '
            f'WHERE const IS ("0");'
        )
        self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")


class Kitchen:
    def __init__(self):
        self.conn = Connection()

    def get_home_outcomes(self):
        stmt = (
            'SELECT * FROM home_outcomes'
        )

        result = self.conn.sql_querry(stmt, dblink="home_outcomes")

        return result

    def build_home_outcome_table(self):
        self.__drop_home_outcome()
        stmt = (
            'CREATE TABLE IF NOT EXISTS home_outcomes ('
            'const INTEGER,'
            'food INTEGER,'
            'cook INTEGER);'
        )
        self.conn.sql_querry(stmt, dblink="home_outcomes")
        self.__set_home_outcome()

    def __set_home_outcome(self):
        values = (0, 0, 0)
        stmt = (
            'INSERT INTO home_outcomes ('
            'const,'
            'food, cook) '
            'VALUES(?,?,?);'
        )
        self.conn.sql_querry(stmt, value=values, dblink="home_outcomes")

    def __drop_home_outcome(self):
        stmt = (
            'DROP TABLE IF EXISTS home_outcomes'
        )
        self.conn.sql_querry(stmt, dblink="home_outcomes")

    def update_home_outcome(self, val):
        stmt = (
            f'UPDATE home_outcomes SET '
            f'food = {val.get("food")},' 
            f'cook = {val.get("cook")} ' 
            f'WHERE const IS ("0");'
        )
        self.conn.sql_querry(sql_stmt=stmt, dblink="home_outcomes")
