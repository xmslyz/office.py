from Database import db_searcher as dbs


class ComputingStipends:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_query = dbs.DatabaseSearcher()

    def list_of_stipends_recieved_by_a_priest(self, who_recived):
        """

        :param who_recived:
        :return:
        """
        sql_stmt = f'SELECT amount FROM {self.table_name} WHERE priest_reciving IS "{who_recived}"'
        return self.db_query.sql_querry(sql_stmt)

    def amount_of_all_stipends_recived(self):
        """
        Suma wszystkich przyjętych ofiar za msze.
        :return: int
        """
        sql_stmt = f'SELECT amount FROM {self.table_name};'
        suma = 0
        for _ in self.db_query.sql_querry(sql_stmt):
            if isinstance(_[0], float):
                suma += int(_[0])
            else:
                continue
        return suma

    def amount_of_all_paid_intentions(self):
        """
        Ilość opłaconych intencji mszalnych (intentia missae).
        :return: int
        """
        sql_stmt = f'SELECT amount FROM {self.table_name} WHERE amount IS NOT "";'
        return len(self.db_query.sql_querry(sql_stmt))

    def amount_of_all_gregorian_intentions(self):
        sql_stmt = f'SELECT celebration_type FROM {self.table_name} WHERE celebration_type IS "gregorianas";'
        return len(self.db_query.sql_querry(sql_stmt))

    def sum_of_aplicated_stipends(self):
        """
        Ilość odprawionych mszy (applicatio missae).
        :return: int
        """
        sql_stmt = f'SELECT celebrated_by FROM {self.table_name} WHERE celebrated_by IS NOT "";'
        return len(self.db_query.sql_querry(sql_stmt))

    def evaluate_paid_masses_vs_application(self):
        """
        Różnica w ilości przyjętch stypendiów i odprawionych mszy.
        N { 0 { M
        (N - ilość nieopłaconych stypendiów, M - ilość nieodprawionych mszy.
        :return:
        """
        return (self.amount_of_all_paid_intentions() + self.amount_of_all_gregorian_intentions()) - self.sum_of_aplicated_stipends()

    def bool_if_application(self):
        """
        Sprawdza, czy wszystkie opłacone msze zostały odprawione.
        :return:
        """
        return True if self.evaluate_paid_masses_vs_application() == 0 else False

    # zwraca średnią (stypendium)
    def mediana_stipends(self):
        assert self.sum_of_aplicated_stipends() > 0
        return round(self.amount_of_all_stipends_recived() / self.sum_of_aplicated_stipends(), 2)


class Priest(ComputingStipends):
    def __init__(self, table_name, priest):
        super().__init__(table_name)
        self.priest = priest

    def amount_of_all_masses_applied_by_a_priest(self):
        """
        Ilość wszystkich mszy odprawionych przez ks.
        :return: int
        """
        sql_stmt = f'SELECT first_mass FROM {self.table_name} WHERE celebrated_by IS "{self.priest}";'
        return len(self.db_query.sql_querry(sql_stmt))

    #
    def amount_of_first_masses_applied_by_a_priest(self):
        """
        Ilość 'pierwszych mszy' odprawionych przez ks.
        :return: int
        """
        sql_stmt = f'SELECT first_mass FROM {self.table_name} WHERE celebrated_by IS "{self.priest}";'
        suma = 0
        for _ in self.db_query.sql_querry(sql_stmt):
            if isinstance(_[0], int):
                suma += int(_[0])
            else:
                continue
        return suma

    def quota_for_priest(self):
        """
        (Quota) Iloraz ilości odprawionych mszy i średniej wartości intencji.
        :return: float
        """
        total_stipend = self.amount_of_first_masses_applied_by_a_priest() * self.mediana_stipends()
        return round(total_stipend, 2)

    def bination_quota_for_priest(self):
        """
        (Binacje) Iloraz ilości odprawionych (kolejnych w danym dniu mszy) i stałej wartości intencji "binacyjnej.
        :return: float
        """
        return (self.amount_of_all_masses_applied_by_a_priest() - self.amount_of_first_masses_applied_by_a_priest()) * 50.00

    def amount_of_binations(self):
        sql_stmt = f"SELECT celebro " \
                   f"FROM {self.table_name} " \
                   f"LEFT OUTER JOIN personal_data " \
                   f"ON {self.table_name}.celebro = personal_data.abrev " \
                   f"WHERE personal_data.abrev IS NULL " \
                   f"AND {self.table_name}.celebro IS NOT '' " \
                   f"AND {self.table_name}.celebro NOT LIKE '%+'"
        return len(self.db_query.sql_querry(sql_stmt))


# def number_of_second_mass():
#     return sqlQ.count_vlen(f"SELECT celebro FROM {self.__table_name} WHERE celebro LIKE '%+'")


# def number_of_masses_nonProfit():
#     return sqlQ.count_vlen(f"SELECT cuota FROM {self.__table_name} WHERE cuota IS NULL OR cuota IS '' AND tipo IS NOT 'gregorianka'")


# def number_of_masses_pokrytych_przez_parafie():
#     return sqlQ.count_vlen(f"SELECT cuota FROM {self.__table_name} WHERE recibio = 'KR'")


# def sum_of_all_stipends():
#     return sqlQ.count_and_return_its_int_sum(f"SELECT cuota FROM {self.__table_name} WHERE cuota IS NOT NULL AND cuota IS NOT '' OR tipo IS 'gregorianka'")


# def value_of_gregoriankas():
#     return sqlQ.count_and_return_its_int_sum(f"SELECT cuota FROM {self.__table_name} WHERE tipo IS 'gregorianka'")


# def number_of_gregoriankas():
#     return sqlQ.count_vlen(f"SELECT cuota FROM {self.__table_name} WHERE tipo IS 'gregorianka'")


# def avg_sum_gregoriankas():
#     if int(number_of_gregoriankas()) > 0:
#         return int(value_of_gregoriankas()) // int(number_of_gregoriankas())
#     else:
#         return 0


# def sum_of_all_extra_masses():
#     x = number_of_masses_extra()
#     y = zmpage.wcztaj_value_z_zmienne_json("zmienne.json", "int_g")
#     return int(x) * int(y)


# def sum_of_all_second_masses():
#     x = number_of_second_mass()
#     y = zmpage.wcztaj_value_z_zmienne_json("zmienne.json", "int_bin")
#     return int(x) * int(y)


# def sum_of_masses_netto():
#     return sum_of_all_stipends() - sum_of_all_extra_masses() - sum_of_all_second_masses()


# def number_of_all_masses_netto():
#     return int(number_of_masses()) - int(number_of_masses_extra()) - int(number_of_second_mass())


# def average_stipend():
#     return sum_of_masses_netto() / number_of_all_masses_netto() if number_of_all_masses_netto() > 0 else 0
