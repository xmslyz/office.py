from unittest import TestCase
import buisness.Computing.pars_computer as pc


class TestParsComputer(TestCase):

    def test_quotient__ok(self):
        net_pars = 2000
        cualified = 4
        result = pc.ParsComputer().quotient(net_pars, cualified)
        assert result == 500

    def test_quotient__zero_cualified(self):
        net_pars = 2000
        cualified = 0
        with self.assertRaises(Exception) as context:
            pc.ParsComputer().quotient(net_pars, cualified)
        self.assertTrue("Ilu do parsu nie może być liczbą ujemną."
                        in str(context.exception))

    def test_quotient__no_money_to_divide(self):
        net_pars = -200
        cualified = 4
        result = pc.ParsComputer().quotient(net_pars, cualified)
        assert result == 0

    def test_cualified__empty_list(self):
        employees = []
        assert pc.ParsComputer().get_cualified(employees) == 0

    def test_cualified__list1(self):
        employees = ([("a",), ], [("b",), ("c",), ("d",)])
        assert pc.ParsComputer().get_cualified(employees) == 5

    def test_cualified__list2(self):
        employees = (["a"], ["b", "c", "d"])
        assert pc.ParsComputer().get_cualified(employees) == 5

    def test_cualified__list3(self):
        employees = (["a"], [])
        assert pc.ParsComputer().get_cualified(employees) == 2
