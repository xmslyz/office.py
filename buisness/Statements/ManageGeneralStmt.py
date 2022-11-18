import buisness.Database.Geter
import buisness.Employee.Identity
from buisness.Database.Builder import DBConnector


# class Update_general_stmt_for_all:
#     def __init__(self):
#         conn = buisness.Database.Geter.IntentionsColsGetter()
#         conn.get_conn_details(1, 1, 2)
#         self.on_duty = conn.get_abreviations()
#
#     def update(self, when):
#         for _ in self.on_duty:
#             Update_monthly_stmt_for_one(when, _).update_value(_)


class NewGenStmt(DBConnector):
    def __init__(self):
        super().__init__()

    def insert_all(self, stmt_date):
        conn = buisness.Database.Geter.UniqueIDGetter().get_list_uniqueID_when_on_duty()
        for _ in conn:
            self.fill_general_stmt(stmt_date, _)

    def fill_general_stmt(self, stmt_date, who):
        # w tej chwili gen jest uzależniony od monthly.
        # zmienić tak, aby nieazleżnie od tego czy jest miesięczny, wypełniał gen.
        # inna sprawa, to czy w ogóle jest potrzeba takiej bazy danych, jeśli wszystko można w sek pozyskać za pomocą kwerendy
        # może przemyśleć to i zamiast zapisywać zestawienia,
        # opracować lepszy system pozyskiwania danych i ich porównywania lub filtrowania

        mocker = (0, '12345678-abcd-efgh-ijkl-1234567890mn', 'Zestawienie miesięczne', '1900-01', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        stmt = buisness.Database.Geter.MonthlyStmtGeter().get_monthly_stmt_by_uniqueID(when=stmt_date, uniID=who)
        gen_stmt = buisness.Database.Geter.MonthlyStmtGeter().get_general_stmt_by_uniqueID_and_date(when=stmt_date, uniID=who)

        if len(gen_stmt) == 0:
            gen_stmt = mocker
        if len(stmt) == 0:
            stmt = mocker

        ispresent = gen_stmt[1] == stmt[1] and gen_stmt[3] == stmt[3]
        if not ispresent:
            val = buisness.Employee.Identity.EmployeeCollations()
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


