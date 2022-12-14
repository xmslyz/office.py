from buisness.Database.SQLConnector import Connection


class ConstantBuilder:
    def __init__(self):
        self.conn = Connection()

    def build_constants_table(self):
        self.__drop_constants()
        stmt = (
            'CREATE TABLE IF NOT EXISTS constants ('
            'const INTEGER,'
            'BIN INTEGER,'
            'INV INTEGER);'
        )
        self.conn.sql_querry(stmt, dblink="constants")
        self.__set_constants()

    def __set_constants(self):
        values = (0, 0, 0)
        stmt = (
            'INSERT INTO constants (const, BIN, INV) VALUES(?,?,?);'
        )
        self.conn.sql_querry(stmt, value=values, dblink="constants")

    def __drop_constants(self):
        stmt = (
            'DROP TABLE IF EXISTS constants'
        )
        self.conn.sql_querry(stmt, dblink="constants")

    def update_constants(self, val):
        stmt = (
            f'UPDATE constants SET '
            f'BIN = {val.get("BIN")}, ' 
            f'INV = {val.get("INV")} ' 
            f'WHERE const IS ("0");'
        )
        self.conn.sql_querry(sql_stmt=stmt, dblink="constants")
