import calendar
import os
import random
import sqlite3
from datetime import datetime


class DatabaseCalendarFiller:
    """
    Jak pisałem mój pierwszy program, to Michał (@MIchalPiotrK) z TT mi wtedy pomógł z poprawniem/napisaniem kodu,
    który miał wypełniać bazę danych dniami miesiąca.
    Także, ta klasa to jeszcze nie moja klasa znajomości pythona.
    Choć dziś już umiem go modfikować i naprawiać usterki.
    Orginalny plik: Random_Generator.addData
    """
    __INSERT_COMMAND = "INSERT INTO main_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    __SELECT_COMMAND = "SELECT * FROM main_table"

    def __init__(self, path="Files\\Database\\default.db"):
        self.__path = path
        self.__full_path = os.path.join(os.path.abspath(os.getcwd()), self.__path)

    def __open_connection(self):
        self.__con = sqlite3.connect(self.__full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.__cur = self.__con.cursor()

    def __close_conection(self):
        self.__con.commit()
        self.__cur.close()

    def addRecord(self, year, month, day):
        """
        A random row filler in a database.
        :param year:
        :param month:
        :param day:
        :return:
        """
        self.__open_connection()

        stipend_type = ["Stypendium mszalne"]
        celebration_time = ["06:30", "07:00", "09:00", "10:30", "12:00", "14:00", "18:00", "19:30"]
        celebration_type = ["in loco", "extra", "gregorianas", "pro defunctis", "pro sponsos", "pro baptismatos"]
        amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
        priests = ["p1", "p2", "p3", "p4", "p5"]  # lista księży na parafii
        first_mass = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.__cur.execute(self.__INSERT_COMMAND,
                           (stipend_type[0],
                            float(random.choice(amounts)),
                            random.choice(priests),
                            random.choice(priests),
                            f'{year}-{month:02}-{day:02}',
                            random.choice(celebration_time),
                            random.choice(celebration_type),
                            random.choice(first_mass)))
        self.__close_conection()

    def getData(self):
        self.__open_connection()
        try:
            result = self.__con.execute(self.__SELECT_COMMAND)
            return [row for row in result]
        finally:
            self.__close_conection()


class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def isSunday(self, day):
        return datetime(self.year, self.month, day).weekday() == 6

    def addRecords(self, qdatabase, days1to6, days7):
        """
        For each day, put in database number of rows, according to the type of day of the week.
        :param qdatabase: Where to put data.
        :param days1to6: Amount of masses in days of the week in a parish.
        :param days7: Amount of masses in Sunday in a parish.
        :return: None
        """
        days_in_month = calendar.monthrange(self.year, self.month)
        for day in range(1, days_in_month[-1] + 1):
            for recordIdx in range(days7 if self.isSunday(day) else days1to6):
                qdatabase.addRecord(self.year, self.month, day)
