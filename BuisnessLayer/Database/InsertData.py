import datetime
import uuid
import BuisnessLayer.Database.Geter
import BuisnessLayer.Employees.Employee
import BuisnessLayer.Database.ScanRecords as dbs
from BuisnessLayer.Database.Connector import DBConnector


class GeneralStmt(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def insert_monthly_stmt(self, stmt_date, who):
        mocker = (0, '12345678-abcd-efgh-ijkl-1234567890mn', 'Zestawienie miesięczne', '1900-01', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        stmt = BuisnessLayer.Database.Geter.MonthlyStmtGeter(1, 1, 3).get_monthly_stmt_by_uniqueID(when=stmt_date, uniID=who)
        gen_stmt = BuisnessLayer.Database.Geter.MonthlyStmtGeter(1, 1, 4).get_general_stmt_by_uniqueID_and_date(when=stmt_date, uniID=who)

        if len(gen_stmt) == 0:
            gen_stmt = mocker
        if len(stmt) == 0:
            stmt = mocker

        ispresent = gen_stmt[1] == stmt[1] and gen_stmt[3] == stmt[3]
        if not ispresent:
            val = BuisnessLayer.Employees.Employee.EmployeeCollations()
            val.uniqueID = f'{stmt[1]}'
            val.type = f'{stmt[2]} miesięczne'
            val.monthly_stmt_date = f'{stmt[3]}'
            val.intention_amount = f'{stmt[4]}'
            val.intention_sum = f'{stmt[5]}'
            val.bination_amount = f'{stmt[6]}'
            val.bination_sum = f'{stmt[7]}'
            val.pars = f'{stmt[8]}'
            val.pretax = f'{stmt[9]}'
            val.taxes = f'{stmt[10]}'
            val.receival = f'{stmt[11]}'
            val.net = f'{stmt[12]}'

            values = (val.uniqueID,
                      val.type,
                      val.monthly_stmt_date,
                      val.intention_amount,
                      val.intention_sum,
                      val.bination_amount,
                      val.bination_sum,
                      val.pars,
                      val.pretax,
                      val.taxes,
                      val.receival,
                      val.net)

            sql_stmt = (f"INSERT INTO {self.table_name}"
                        f"(uniqueID, type, monthly_stmt_date,"
                        f"intention_amount, intention_sum, "
                        f"bination_amount, bination_sum, "
                        f"pars, pretax, taxes, receival, net) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);")
            self.create_connection(0, sql_stmt, values)


class MassRecord(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def insert_record(self, val, *, amount=1):
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
        first_day = datetime.datetime.strptime(val.date_of_celebration, "%Y-%m-%d")
        next_day = first_day + datetime.timedelta(days=x)
        next_day.strftime("%Y-%m-%d")
        return next_day.strftime("%Y-%m-%d")

    def is_first_checker(self, val):
        dbsearcher = dbs.RecordsScanner(path_num=1, dbnm_num=1, tbl_num=1)
        who_celebrated_query = val.celebrating_priest
        celebration_day_query = val.date_of_celebration
        return len(dbsearcher.select_all_where_q_is(qcelebrated_by=who_celebrated_query,
                                                    qcelebration_date=celebration_day_query
                                                    ))


class PersonalData(DBConnector):
    def __init__(self, path, dbname, table_name):
        super().__init__(path, dbname, table_name)

    def new_employee(self, employee):
        uniqueID = str(uuid.uuid4())
        employee.uniqueID = uniqueID
        self.__introduce_new_employee(employee)
        self.__introduce_new_empees_cashflow(uniqueID)

    def __introduce_new_employee(self, val):
        sql_stmt = (f"INSERT INTO {self.table_name} "
                    f"(uniqueID,type,name,surname,shortname,abreviation,function,taxes) "
                    f"VALUES (?,?,?,?,?,?,?,?);")
        values = (val.uniqueID,
                  val.type,
                  val.name,
                  val.surname,
                  val.shortname,
                  val.abreviation,
                  val.function,
                  val.taxes)
        self.create_connection(0, sql_stmt, values)
        return val

    def __introduce_new_empees_cashflow(self, uniqueID):
        colldb = BuisnessLayer.Database.InsertData.PersonalData(1, 1, 3)
        coll = BuisnessLayer.Employees.Employee.EmployeeCollations()
        coll.uniqueID = uniqueID
        coll.monthly_stmt = None
        sql_stmt = (f"INSERT INTO {colldb.table_name}"
                    f"(uniqueID, stmt_date) VALUES (?,?);")
        values = (coll.uniqueID,
                  coll.monthly_stmt)
        self.create_connection(0, sql_stmt, values)

    def update_value(self, *, column, value, qid):
        sql_stmt = f"UPDATE {self.table_name} SET {column} = '{value}' WHERE uniqueID IS '{qid}';"
        self.create_no_val_connection(sql_stmt)
