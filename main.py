from buisness.Computing.tax_computer import GeneralStmt as GS


def main():
    print("hi")
    gs = GS("2022-10")
    gs.get_conn_details("employees")
    print(gs.sum_taxes_for_employee("2cd896c4-d670-4ee7-92c2-8ab9b9a3ee8a"))


if __name__ == '__main__':
    main()
