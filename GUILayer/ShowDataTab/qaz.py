import BuisnessLayer.Accounts.MonthlyStatementsComputer as msc
from BuisnessLayer.Database import ScanRecords as dbs


def wydruk_ogolny(qdate):
    db_query = dbs.RecordsScanner(1, 1, 1)

    ssc = msc.GeneralStmt(table_name="intentions", scanner=db_query, qdate=qdate)
    print('1.  sum_of_all_recived -> ', ssc.sum_of_all_recived())
    print('2.  list_of_all_recived -> ', ssc.list_of_all_recived())
    print('3.  amount_of_aplicated -> ', ssc.amount_of_aplicated())
    print('4.  amount_of_all_paid -> ', ssc.amount_of_all_paid())
    print('5.  mediana -> ', ssc.mediana())
    print('6.  amount_of_binations -> ', ssc.amount_of_binations())
    print('7.  list_of_binations -> ', ssc.list_of_binations())
    print('8.  sum_of_binations -> ', ssc.sum_of_binations())
    print('9.  list_of_all_gregorian -> ', ssc.list_of_all_gregorian())
    print('10. amount_of_all_gregorian -> ', ssc.amount_of_all_gregorian())
    print('11. sum_of_all_gregorian -> ', ssc.sum_of_all_gregorian())
    print('12. gregorian_mediana -> ', ssc.gregorian_mediana())
    print('13. gregorian_sum_of_medianas -> ', ssc.gregorian_sum_of_medianas())
    print('14. list_of_aplicated_stipends -> ', ssc.list_of_aplicated_stipends())
    print('15. amount_of_aplicated -> ', ssc.amount_of_aplicated())
    print('16. list_not_paid_aplicated -> ', ssc.list_not_paid_aplicated())
    print('17. list_not_paid_aplicated -> ', ssc.list_not_paid_aplicated())
    print('18. list_not_paid_not_aplicated -> ', ssc.list_not_paid_not_aplicated())
    print("\n")