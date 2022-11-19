import datetime

import buisness.Database.Filter
import buisness.Database.Geter
from buisness.Database import SQLConnector as dbs
from buisness.Database.Builder import DBConnector


class CreateNewStipend(DBConnector):
    def __init__(self):
        super().__init__()

    def insert_record(self, val, *, amount=1):
        """ Wstawia tyle wierszy ile amount, data celebracji += 1 dzień """
        assert amount > 0
        if self.is_first_checker(val) == 0:
            val.is_first = True
        else:
            val.is_first = False
        for x in range(0, amount):
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
            self.create_connection(0, sql_stmt, values)

    def day_aumenter(self, x, val):
        """ Dodaje +1 dzień do daty celebracji """
        first_day = datetime.datetime.strptime(val.date_of_celebration, "%Y-%m-%d")
        next_day = first_day + datetime.timedelta(days=x)
        next_day.strftime("%Y-%m-%d")
        return next_day.strftime("%Y-%m-%d")

    def is_first_checker(self, val):
        """ Sprawdzam czy to pierwsza msza w tym dniu danego księdza """
        dbsearcher = buisness.Database.Filter.Filter()
        dbsearcher.get_conn_details("intentions")
        who_celebrated_query = val.celebrating_priest
        celebration_day_query = val.date_of_celebration
        return len(dbsearcher.select_all_where_q_is(qcelebrated_by=who_celebrated_query,
                                                    qcelebration_date=celebration_day_query
                                                    ))


class UpdateMassStipend(DBConnector):
    def __init__(self):
        super().__init__()

    def will_be_first(self, val):
        """
        Sprawdzam czy już w danym dniu figuruje celebrated_by. Jeśli tak to first_mass = False
        """
        sql_stmt = f"SELECT celebrated_by, celebration_hour, celebration_date, first_mass FROM intentions " \
                   f"WHERE celebration_date IS ('{val.date_of_celebration}');"
        con = dbs.Connection()
        con.get_conn_details("intentions")
        query = con.sql_querry(sql_stmt)

        i = 0
        if query:
            for _ in query:
                if _[0] == val.celebrating_priest:
                    i += 1
        return i

    def update(self, val, id_num):
        """
        Aktualizacja wiersza w tabeli intencje
        """
        # jeśli aktualizowany ksiądz odprawiał mszę, first_mass = False
        if self.will_be_first(val) > 0:
            val.is_first = False
        else:
            val.is_first = True

        values = (val.amount,
                  val.reciving_priest,
                  val.celebrating_priest,
                  val.date_of_celebration,
                  val.hour_of_celebration,
                  val.type_of_mass,
                  val.is_gregorian,
                  val.is_first)
        sql_stmt = (f"UPDATE {self.table_name} SET "
                    f"amount = ?, "
                    f"priest_reciving = ?, "
                    f"celebrated_by = ?, "
                    f"celebration_date = ?, "
                    f"celebration_hour = ? , "
                    f"celebration_type = ?, "
                    f"gregorian = ?,"
                    f"first_mass = ? WHERE id = '{id_num}';")
        self.create_connection(0, sql_stmt, values)


class DeleteMassStipend(DBConnector):
    def __init__(self):
        super().__init__()

    def delete(self, sqlid):
        sql_stmt = f"DELETE FROM intentions WHERE id = '{sqlid}';"
        self.sql_querry(sql_stmt)

    def delete_last_record(self):
        eachid = buisness.Database.Geter.IntentionsColsGetter()
        eachid.get_conn_details("employees")
        this = eachid.get_one("id")
        sql_stmt = f"DELETE FROM intentions WHERE id = '{max(this)[0]}';"
        self.sql_querry(sql_stmt)
