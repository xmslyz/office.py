import PresentationLayer.temp.add as add
import PresentationLayer.temp.print as p


def main():
    print("Hi World!")

    # wstawia w tabeli [default.db] pojedynczy wiersz
    add.single_record()

    #wstawia w tabeli [default.db] serię wierszy
    add.multiple_record()

    # wyrzuca na konsolę wyniki z DB
    p.wydruk()


if __name__ == '__main__':
    main()
