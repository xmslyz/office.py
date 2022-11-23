from buisness.Solids.Fees import KOZI


def input_update_kozi():
    # noinspection PyDictCreation
    val = {"const": 0}

    val['BK'] = 10
    val['BO'] = 0
    val['BZ'] = 0
    val['BI'] = 0
    val['MK'] = 120
    val['MO'] = 200
    val['MZ'] = 70
    val['MI'] = 60
    val['FK'] = 30
    val['FO'] = 120
    val['FZ'] = 70
    val['FI'] = 60
    KOZI().update_kozi(val)


def get_monthly_burden():
    burdenBK = 1
    burdenBO = 1
    burdenBZ = 1
    burdenBI = 1
    burdenMK = 1
    burdenMO = 1
    burdenMZ = 1
    burdenMI = 1
    burdenFK = 1
    burdenFO = 1
    burdenFZ = 1
    burdenFI = 1
    return (burdenBK, burdenBO, burdenBZ, burdenBI), \
           (burdenMK, burdenMO, burdenMZ, burdenMI), \
           (burdenFK, burdenFO, burdenFZ, burdenFI)
