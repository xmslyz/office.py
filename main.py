import buissnes.Computing.statements_computer
from buissnes import *
from gui import *


def main():

    # comp = buissnes.Computing.statements_computer.ComputeMonthlyStmt("2022-10")
    emp = buissnes.Computing.statements_computer.ComputeEmployeeStmt("2022-10", "PK")
    print(emp.net_for_priest())


if __name__ == '__main__':
    main()
