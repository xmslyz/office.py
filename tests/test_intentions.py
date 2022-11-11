from unittest import TestCase
from buissnes.Income import Stipend


class TestAmount(TestCase):

    def test_amount__below0(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = '-23.12'
        self.assertTrue('Kwota nie może być mniejsza od zera' in str(context.exception))

    def test_amount__nonnumeric(self):
        stip = Stipend.StipendRecord()
        stip.amount = '$12.98'
        assert stip.amount == 12.98

    def test_amount__nonnumericbelow0(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = '$-23.12'
        self.assertTrue('Kwota nie może być mniejsza od zera' in str(context.exception))

    def test_amount__nonnumericbelow0_2(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = '-23.12$'
        self.assertTrue('Kwota nie może być mniejsza od zera' in str(context.exception))

    def test_amount__string(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = "qaz"
        self.assertTrue("Wprowadzana wartość nie jest liczbą" in str(context.exception))

    def test_amount__empty(self):
        stip = Stipend.StipendRecord()
        stip.amount = ''
        assert stip.amount == 0.0

    def test_amount__boll(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = False
        self.assertTrue("Podano wartość logiczną." in str(context.exception))

    def test_amount__int(self):
        stip = Stipend.StipendRecord()
        stip.amount = "12"
        assert stip.amount == 12.0

    def test_amount__None(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.amount = None
        self.assertTrue("Wprowadzana wartość nie jest liczbą" in str(context.exception))


class TestCelebratingAbrev(TestCase):
    # reviving_priest is the same case.

    def test_celebrating_pr__morethan3(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.celebrating_priest = 'ABCD'
        self.assertTrue('Przekroczono dopuszczalną ilość znaków (3).' in str(context.exception))

    def test_celebrating_pr__nonalfabetchar(self):
        stip = Stipend.StipendRecord()
        stip.celebrating_priest = 'P4L'
        assert stip.celebrating_priest == "PL"

    def test_celebrating_pr__empty(self):
        stip = Stipend.StipendRecord()
        stip.celebrating_priest = ''
        assert stip.celebrating_priest == ""

    def test_celebrating_pr__nums(self):
        stip = Stipend.StipendRecord()
        stip.celebrating_priest = '123'
        assert stip.celebrating_priest == ""


class TestDateOfCelebration(TestCase):
    def test_wrong_date_format(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '12-12-202'
        self.assertTrue('Podaj właściwy format daty' in str(context.exception))

    def test_wrong_date_order(self):
        stip = Stipend.StipendRecord()
        stip.date_of_celebration = '31-12-2022'
        assert stip.date_of_celebration == "2022-12-31"

    def test_not_a_day(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022-02-31'
        self.assertTrue('Nie ma takiej daty' in str(context.exception))

    def test_not_a_month(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022-13-01'
        self.assertTrue('Nie ma takiej daty' in str(context.exception))

    def test_spaces(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.date_of_celebration = '2022 12 12'
        self.assertTrue("Podaj właściwy format daty" in str(context.exception))


class TestCelebrationHour(TestCase):
    def test_not_an_hour(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.hour_of_celebration = "25:12:00"
        self.assertTrue("Podaj właściwy format godziny" in str(context.exception))

    def test_None_hour(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.hour_of_celebration = None
        self.assertTrue("Podaj właściwy format godziny" in str(context.exception))

    def test_not_numeric(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.hour_of_celebration = "HH:mm:ss"
        self.assertTrue("Podaj właściwy format godziny" in str(context.exception))

    def test_no_sec(self):
        stip = Stipend.StipendRecord()
        stip.hour_of_celebration = "12:00"
        assert stip.hour_of_celebration == "12:00"

    def test_no_sec_no_hour(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.hour_of_celebration = "34:00"
        self.assertTrue("Podaj właściwy format godziny" in str(context.exception))


class TestType(TestCase):

    def test_type__logic(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.type_of_mass = False
        self.assertTrue("Podano wartość logiczną." in str(context.exception))

    def test_OK(self):
        stip = Stipend.StipendRecord()
        stip.type_of_mass = 'Typ'
        assert stip.type_of_mass == "Typ"

    def test_empty(self):
        stip = Stipend.StipendRecord()
        stip.type_of_mass = ''
        assert stip.type_of_mass == ""

    def test_alfanum(self):
        stip = Stipend.StipendRecord()
        stip.type_of_mass = '123'
        assert stip.type_of_mass == ""

    def test_None(self):
        stip = Stipend.StipendRecord()
        stip.type_of_mass = None
        assert stip.type_of_mass == ""


class TestIsGregorian(TestCase):
    def test_boolean(self):
        stip = Stipend.StipendRecord()
        stip.is_gregorian = True
        assert stip.is_gregorian == True

    def test_not_boolean(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_gregorian = "False"
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))

    def test_int_type(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_gregorian = 1
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))

    def test_None_type(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_gregorian = None
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))


class TestIsFirst(TestCase):
    def test_boolean(self):
        stip = Stipend.StipendRecord()
        stip.is_first = True
        assert stip.is_first == True

    def test_not_boolean(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_first = "False"
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))

    def test_int_type(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_first = "False"
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))

    def test_None_type(self):
        stip = Stipend.StipendRecord()
        with self.assertRaises(Exception) as context:
            stip.is_first = "False"
        self.assertTrue("Nie boolowski typ danych" in str(context.exception))
