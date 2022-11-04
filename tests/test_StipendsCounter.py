from unittest import TestCase
import BuisnessLayer.Accounts.MonthlyStatementsComputer
from BuisnessLayer.Database import ScanRecords as dbs


class TestComputingStipends(TestCase):

    def test_sum_of_all_recived(self):
        db_query = dbs.RecordsScanner(path="tests\\test.db", table_name="test")
        ssc = BuisnessLayer.Accounts.MonthlyStatementsComputer.GeneralStmt("test", scanner=db_query, qdate="2022-05")
        assert ssc.sum_of_all_recived() == 1

    def test_amount_of_all_paid(self):
        self.fail()

    def test_mediana(self):
        self.fail()

    def test_list_of_binations(self):
        self.fail()

    def test_amount_of_binations(self):
        self.fail()

    def test_sum_of_binations(self):
        self.fail()

    def test_list_of_all_gregorian(self):
        self.fail()

    def test_amount_of_all_gregorian(self):
        self.fail()

    def test_sum_of_all_gregorian(self):
        self.fail()

    def test_gregorian_mediana(self):
        self.fail()

    def test_gregorian_sum_of_medianas(self):
        self.fail()

    def test_list_of_aplicated_stipends(self):
        self.fail()

    def test_amount_of_aplicated(self):
        self.fail()

    def test_paid_not_applicated(self):
        self.fail()

    def test_not_paid_aplicated(self):
        self.fail()

    def test_not_paid_not_aplicated(self):
        self.fail()
