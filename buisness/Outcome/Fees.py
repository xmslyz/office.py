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
            'b_k INTEGER,'
            'b_o INTEGER,'
            'b_z INTEGER,'
            'b_i INTEGER,'
            'm_k INTEGER,'
            'm_o INTEGER,'
            'm_z INTEGER,'
            'm_i INTEGER,'
            'f_k INTEGER,'
            'f_o INTEGER,'
            'f_z INTEGER,'
            'f_i INTEGER);'
        )
        self.conn.sql_querry(stmt, dblink="builder")
        self.__set_kozi_const()

    def __set_kozi_const(self):
        values = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        stmt = (
            'INSERT INTO kozi ('
            'const,'
            'b_k, b_o, b_z, b_i,'
            'm_k, m_o, m_z, m_i,'
            'f_k, f_o, f_z, f_i) '
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
            f'b_k = {val.get("b_k")},' 
            f'b_o = {val.get("b_o")},' 
            f'b_z = {val.get("b_z")},' 
            f'b_i = {val.get("b_i")},' 
            f'm_k = {val.get("m_k")},' 
            f'm_o = {val.get("m_o")},' 
            f'm_z = {val.get("m_z")},' 
            f'm_i = {val.get("m_i")},' 
            f'f_k = {val.get("f_k")},' 
            f'f_o = {val.get("f_o")},' 
            f'f_z = {val.get("f_z")},' 
            f'f_i = {val.get("f_i")} '
            f'WHERE const IS ("0");'
        )
        self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")