import BuisnessLayer.Accounts.MonthlyStatementsComputer as msc
import BuisnessLayer.Income.stipend_income
from BuisnessLayer.Database import ScanRecords as dbs


def wydruk_ogolny(qdate):
    db_query = dbs.RecordsScanner(path_num=1, dbnm_num=1, tbl_num=1)
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


def wypis_po_id(qid):
    db_query = dbs.RecordsScanner(path_num=1, dbnm_num=1, tbl_num=1)
    return msc.GeneralStmt(table_name="intentions", scanner=db_query, qdate="").record_by_id(qid=qid)


def wydruk_osoba(qdate):
    myscan = dbs.RecordsScanner(path_num=1, dbnm_num=1, tbl_num=1)
    qdata = f"{qdate}-__"
    res = myscan.select_all_where_q_like(qcelebrated_by="%_", qcelebration_date=qdata)
    mylist = []
    for _ in res:
        mylist.append(_[3])
    kto = list(set(mylist))
    for x in kto:
        #  intencje
        sp = msc.PriestStmt("intentions", scanner=myscan, who_recived=f"{x}", qdate=qdate)

        print(f"{x}")
        print('1. list_of_recieved_by_a_priest -> ', sp.list_of_recieved_by_a_priest())
        print('2. sum_of_recieved_by_a_priest -> ', sp.sum_of_recieved_by_a_priest())
        print('3. amount_of_all_masses_applied_by_a_priest -> ', sp.amount_of_all_masses_applied_by_a_priest())
        print('4. amount_of_first_masses_applied_by_a_priest -> ', sp.amount_of_first_masses_applied_by_a_priest())
        print('5. amount_of_bination_applied_by_a_priest -> ', sp.amount_of_bination_applied_by_a_priest())
        print('6. quota_for_priest -> ', sp.quota_for_priest())
        print('7. bination_quota_for_priest -> ', sp.bination_quota_for_priest())
        print('8. total_wage_for_priest -> ', sp.total_wage_for_priest())
        print("\n")
