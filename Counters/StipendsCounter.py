from Database import db_searcher as dbs


class ComputingStipends:
    def __init__(self):
        self.db_query = dbs.DatabaseSearcher()

    def list_of_stipends_recieved_by_a_priest(self, who_recived):
        """

        :param who_recived:
        :return:
        """
        sql_stmt = f'SELECT amount FROM main_table WHERE priest_reciving IS "{who_recived}"'
        return self.db_query.sql_querry(sql_stmt)

    def sum_all_stipends(self):
        """
        Suma wszystkich przyjętych ofiar za msze.
        :return: int
        """
        sql_stmt = f'SELECT amount FROM main_table;'
        suma = 0
        for _ in self.db_query.sql_querry(sql_stmt):
            if isinstance(_[0], float):
                suma += int(_[0])
            else:
                continue
        return suma

    def sum_of_paid_intentions(self):
        """
        Ilość opłaconych intencji mszalnych (intentia missae).
        :return: int
        """
        sql_stmt = f'SELECT amount FROM main_table WHERE amount IS NOT "";'
        return len(self.db_query.sql_querry(sql_stmt))

    def sum_of_aplicated_stipends(self):
        """
        Ilość odprawionych mszy (applicatio missae).
        :return: int
        """
        sql_stmt = f'SELECT celebrated_by FROM main_table WHERE celebrated_by IS NOT "";'
        return len(self.db_query.sql_querry(sql_stmt))

    def evaluate_paid_masses_vs_application(self):
        """
        Różnica w ilości przyjętch stypendiów i odprawionych mszy.
        N { 0 { M
        (N - ilość nieopłaconych stypendiów, M - ilość nieodprawionych mszy.
        :return:
        """
        return self.sum_of_paid_intentions() - self.sum_of_aplicated_stipends()

    def bool_if_application(self):
        """
        Sprawdza, czy wszystkie opłacone msze zostały odprawione.
        :return:
        """
        return True if self.sum_of_aplicated_stipends() == self.sum_of_paid_intentions() else False

    # zwraca średnią (stypendium)
    def mediana_stipends(self):
        assert self.sum_of_aplicated_stipends() > 0
        return round(self.sum_all_stipends() / self.sum_of_aplicated_stipends(), 2)

    # zwraca ilość odprawionych mszy przez danego ks.
    def __sum_of_applied_masses(self):
        pass

    # zwraca quotę za odprawione msze
    def __quota(self):
        pass
