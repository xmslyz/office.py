import datetime
import PresentationLayer.temp.build as bdb
import PresentationLayer.temp.add as add
import PresentationLayer.temp.print as p


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()

    buduj = bdb.PLUG_database_operator()
    # buduj.budowa_bazy_danych_employee()
    # buduj.budowa_bazy_danych_collations()
    # buduj.budowa_bazy_danych_intentions()

    # buduj.usuniecie_tabeli_list()
    # buduj.usuniecie_tabeli_collations()
    # buduj.usuniecie_tabeli_intentions()

    # buduj.file_employee_destroyer()
    # buduj.file_masses_destroyer()

    # wstawia w tabeli [default.db] pojedynczy wiersz
    # add.single_record()

    #wstawia w tabeli [default.db] serię wierszy
    # add.multiple_record()

    # wyrzuca na konsolę wyniki z DB
    # p.wydruk_ogolny()
    # p.wydruk_osoba()
    # p.wypis_po_id(qid="12106")
    t2 = datetime.datetime.now()
    print(t2-t1)


if __name__ == '__main__':
    main()
