import sqlite3
import datetime
import BuisnessLayer.Database.ScanRecords as dbs
from BuisnessLayer.Database.Connector import DBConnector


class StipendEntries(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def single_entry(self, val):
        if self.is_first_checker(val) == 0:
            val.is_first = True
        else:
            val.is_first = False
        sql_stmt = (f"INSERT INTO {self.table_name} "
                           f"(type, "
                           f"amount, "
                           f"priest_reciving, "
                           f"celebrated_by, "
                           f"celebration_date, "
                           f"celebration_hour, "
                           f"celebration_type, "
                           f"gregorian, "
                           f"first_mass) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)")
        values = (val.type,
                  val.amount,
                  val.reciving_priest,
                  val.celebrating_priest,
                  val.date_of_celebration,
                  val.hour_of_celebration,
                  val.type_of_mass,
                  val.is_gregorian,
                  val.is_first)
        self.create_connection(sql_stmt, values)

    def compound_entry(self, val, repeat):
        if self.is_first_checker(val) == 0:
            val.is_first = True
        else:
            val.is_first = False
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
            sql_stmt = (f"INSERT INTO {self.table_name} "
                               f"(type, "
                               f"amount, "
                               f"priest_reciving, "
                               f"celebrated_by, "
                               f"celebration_date, "
                               f"celebration_hour, "
                               f"celebration_type, "
                               f"gregorian, "
                               f"first_mass) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)")
            self.create_connection(sql_stmt, values)

    def day_aumenter(self, x, val):
        first_day = datetime.datetime.strptime(val.date_of_celebration, "%Y-%m-%d")
        next_day = first_day + datetime.timedelta(days=x)
        next_day.strftime("%Y-%m-%d")
        return next_day.strftime("%Y-%m-%d")

    def is_first_checker(self, val):
        dbsearcher = dbs.RecordsScanner()
        who_celebrated_query = val.celebrating_priest
        celebration_day_query = val.date_of_celebration
        return len(dbsearcher.select_all_where_q_is(qcelebrated_by=who_celebrated_query,
                                                    qcelebration_date=celebration_day_query
                                                    ))
