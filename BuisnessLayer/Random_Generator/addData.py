import sqlite3
from datetime import datetime
# from ui_MainWindow import Ui_Form as uF


class Database:
    INSERT_COMMAND = 'insert into ksiega (data, hora, tipo, recibio, cuota, celebro) values (?,?,?,?,?,?)'

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        # self.ui = uF()
        # self.ui.setupUi(uF)

    def addRecord(self, year, month, day, autoCommit=False):
        self.cursor.execute(self.INSERT_COMMAND, (f'{year}-{month:02}-{day:02}', '', '', '', '', ''))
        if autoCommit:
            self.connection.commit()

    def getData(self):
        result = self.connection.execute('select * from ksiega')
        return [row for row in result]

    def commit(self):
        self.connection.commit()


class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def isSunday(self, day):
        return datetime(self.year, self.month, day).weekday() == 6

    def numberOfDays(self):
        if self.month == 2:
            return 29 if self.year % 4 == 0 else 28
        elif self.month % 2 + (self.month // 7) == 0:
            return 30
        else:
            return 31

    def addRecords(self, database, days1to6, days7):
        for day in range(1, self.numberOfDays() + 1):
            for recordIdx in range(days7 if self.isSunday(day) else days1to6):
                database.addRecord(self.year, self.month, day)
        database.commit()

# aplikacja
# database = DatabaseConstructor('person.db')
# Month(2022,5).addRecords(database, 4, 3)

# odczyt
# r = database.getData()
# print(r)
