from buisness.Database.SQLConnector import Connection


class OutcomesGeter:

    def __init__(self):
        self.conn = Connection()
        self.bin = self.inv = 0
        self.cook = self.food = 0
        self.BK = self.BO = self.BZ = self.BI = 0
        self.MK = self.MO = self.MZ = self.MI = 0
        self.FK = self.FO = self.FZ = self.FI = 0
        self.__get_const()
        self.__get_kithen()
        self.__get_kozi()

    def __get_const(self):
        stmt = (
            'SELECT * FROM constants WHERE const IS "0";'
        )
        self.bin = self.conn.sql_querry(sql_stmt=stmt, dblink="constants")[0][
            1]
        self.inv = self.conn.sql_querry(sql_stmt=stmt, dblink="constants")[0][
            2]

        return None

    def __get_kithen(self):
        stmt = (
            'SELECT * FROM home_outcomes WHERE const IS "0";'
        )
        self.cook = \
            self.conn.sql_querry(sql_stmt=stmt, dblink="home_outcomes")[0][
                1]
        self.food = self.conn.sql_querry(sql_stmt=stmt,
                                         dblink="home_outcomes")[0][
            2]

    def __get_kozi(self):
        stmt = (
            'SELECT * FROM kozi WHERE const IS "0";'
        )
        self.BK = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][1]
        self.BO = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][2]
        self.BZ = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][3]
        self.BI = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][4]
        self.MK = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][5]
        self.MO = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][6]
        self.MZ = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][7]
        self.MI = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][8]
        self.FK = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][9]
        self.FO = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][10]
        self.FZ = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][11]
        self.FI = self.conn.sql_querry(sql_stmt=stmt, dblink="kozi")[0][12]


class OutcomesComputer:
    def __init__(self):
        self.og = OutcomesGeter()

    def __repr__(self):
        print(
            self.og.BK, self.og.BO, self.og.BZ, self.og.BI,
            self.og.MK, self.og.MO, self.og.MZ, self.og.MI,
            self.og.FK, self.og.FO, self.og.FZ, self.og.FI
        )

    def sum_kozi(self, *args):
        return self.count_B(args[0][0]) + \
               self.count_M(args[0][1]) + \
               self.count_F(args[0][2])

    def count_B(self, *args):
        if args:
            result = self.og.BK * args[0][0] + \
                   self.og.BO * args[0][1] + \
                   self.og.BZ * args[0][2] + \
                   self.og.BI * args[0][3]
            return result
        else:
            return None

    def count_M(self, *args):
        if args:
            result = self.og.MK * args[0][0] + \
                   self.og.MO * args[0][1] + \
                   self.og.MZ * args[0][2] + \
                   self.og.MI * args[0][3]
            return result
        else:
            return None

    def count_F(self, *args):
        if args:
            result = self.og.FK * args[0][0] + \
                   self.og.FO * args[0][1] + \
                   self.og.FZ * args[0][2] + \
                   self.og.FI * args[0][3]
            return result
        else:
            return None

    def count_food_and_cook(self):
        return self.og.food + self.og.cook
