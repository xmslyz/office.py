from unittest import TestCase
from buissnes.Income import Stipend as St


class TestAmount(TestCase):

    def test_amount__lessthanzero(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = '-23.12'
        self.assertTrue('Kwota nie może być mniejsza od zera' in str(context.exception))

    def test_amount__nonalfanumeric(self):
        stip = St.StipendRecord()
        stip.amount = '$12.98'
        assert stip.amount == 12.98

    def test_amount__nonalfanumeric2(self):
        stip = St.StipendRecord()
        stip.amount = '$-12.98'
        assert stip.amount == 12.98

    def test_amount__nonalfanumeric3belowzero(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = '-23.12$'
        self.assertTrue('Kwota nie może być mniejsza od zera' in str(context.exception))

    def test_amount__string(self):
        stip = St.StipendRecord()
        stip.amount = 'qaz'
        assert stip.amount == 0.0

    def test_amount__empty(self):
        stip = St.StipendRecord()
        stip.amount = ''
        assert stip.amount == 0.0

    def test_amount__boll(self):
        stip = St.StipendRecord()
        stip.amount = False
        assert stip.amount == 0.0

    def test_amount__int(self):
        stip = St.StipendRecord()
        stip.amount = "12"
        assert stip.amount == 12.0


class TestCelebratingAbrev(TestCase):

    def test_celebrating_pr__morethan3(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.celebrating_priest = 'ABCD'
        self.assertTrue('Przekroczono dopuszczalną ilość znaków (3).' in str(context.exception))

    def test_celebrating_pr__nonalfabetchar(self):
        stip = St.StipendRecord()
        stip.celebrating_priest = 'P4L'
        assert stip.celebrating_priest == "PL"

    def test_celebrating_pr__empty(self):
        stip = St.StipendRecord()
        stip.celebrating_priest = ''
        assert stip.celebrating_priest == " "

    def test_celebrating_pr__nums(self):
        stip = St.StipendRecord()
        stip.celebrating_priest = '123'
        assert stip.celebrating_priest == ""


class TestDateOfCelebration(TestCase):
    def test_wrong_date_format(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '12-12-202'
        self.assertTrue('Podaj właściwy format daty' in str(context.exception))

    def test_wrong_date_order(self):
        stip = St.StipendRecord()
        stip.date_of_celebration = '31-12-2022'
        assert stip.date_of_celebration == "2022-12-31"

    def test_not_a_day(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022-02-31'
        self.assertTrue('Nie ma takiej daty' in str(context.exception))

    def test_not_a_month(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022-13-01'
        self.assertTrue('Nie ma takiej daty' in str(context.exception))

    def test_123(self):
        stip = St.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022 12 12'
        self.assertTrue("Podaj właściwy format daty" in str(context.exception))