from Database import db_searcher as dbs


class ComputingStipends:
    def __init__(self):
        self.db_query = dbs.DatabaseSearcher()

    def list_of_stipends_recieved_by_a_priest(self, sql_stmt):
        return self.db_query.sql_querry(sql_stmt)

    # zwraca sumę wszystkich przyjętych ofiar za msze
    def sum_all_stipends(self):
        pass

    # zwraca ilość przyjętych mszy
    def sum_of_masses(self):
        pass

    # zwraca średnią (stypendium)
    def mediana_stipends(self):
        pass

    # zwraca ilość odprawionych mszy przez danego ks.
    def sum_of_applied_masses(self):
        pass

    # zwraca quotę za odprawione msze
    def quota(self):
        pass
