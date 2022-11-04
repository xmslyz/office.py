import datetime

import PresentationLayer.temp.add as add
import PresentationLayer.temp.print as p


def main():
    print("Hi World!")
    t1 = datetime.datetime.now()

    # wstawia w tabeli [default.db] pojedynczy wiersz
    # add.single_record()

    #wstawia w tabeli [default.db] serię wierszy
    # add.multiple_record()

    # wyrzuca na konsolę wyniki z DB
    p.wydruk_ogolny()
    p.wydruk_osoba()
    # p.wypis_po_id(qid="12106")
    t2 = datetime.datetime.now()
    print(t2-t1)


if __name__ == '__main__':
    main()
