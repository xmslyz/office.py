import os
import sqlite3
import datetime
import BuisnessLayer.Database.ScanRecords as dbs


class StipendEntries:
    def __init__(self, path="DatabaseLayer\\SQLDataBase\\default.db"):
        self.__path = path
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), self.__path)

    def __open_connection(self):
        self.__con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()

    def __close_conection(self):
        self.__con.commit()
        self.__cur.close()

    def single_entry(self, table_name, val):
        if self.is_first_checker(val) == 0:
            val.is_first = True
        else:
            val.is_first = False
        self.__open_connection()
        values = (val.type,
                  val.amount,
                  val.reciving_priest,
                  val.celebrating_priest,
                  val.date_of_celebration,
                  val.hour_of_celebration,
                  val.type_of_mass,
                  val.is_gregorian,
                  val.is_first)
        self.__cur.execute(f"INSERT INTO {table_name} "
                           f"(type, "
                           f"amount, "
                           f"priest_reciving, "
                           f"celebrated_by, "
                           f"celebration_date, "
                           f"celebration_hour, "
                           f"celebration_type, "
                           f"gregorian, "
                           f"first_mass) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        self.__close_conection()

    def is_first_checker(self, val):
        dbsearcher = dbs.RecordsScanner()
        who_celebrated_query = val.celebrating_priest
        celebration_day_query = val.date_of_celebration
        return len(dbsearcher.select_all_where_q_is(qcelebrated_by=who_celebrated_query,
                                                    qcelebration_date=celebration_day_query
                                                    ))

    def day_aumenter(self, x, val):
        first_day = datetime.datetime.strptime(val.date_of_celebration, "%Y-%m-%d")
        next_day = first_day + datetime.timedelta(days=x)
        next_day.strftime("%Y-%m-%d")
        return next_day.strftime("%Y-%m-%d")

    def compound_entry(self, table_name, val, repeat):
        if self.is_first_checker(val) == 0:
            val.is_first = True
        else:
            val.is_first = False
        self.__open_connection()
        for x in range(0, repeat):
            values = (val.type,
                      val.amount,
                      val.reciving_priest,
                      val.celebrating_priest,
                      self.day_aumenter(x, val),
                      val.hour_of_celebration,
                      val.type_of_mass,
                      val.is_gregorian,
                      val.is_first
                      )
            self.is_first_checker(val)
            self.__cur.execute(f"INSERT INTO {table_name} "
                               f"(type, "
                               f"amount, "
                               f"priest_reciving, "
                               f"celebrated_by, "
                               f"celebration_date, "
                               f"celebration_hour, "
                               f"celebration_type, "
                               f"gregorian, "
                               f"first_mass) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        self.__close_conection()
