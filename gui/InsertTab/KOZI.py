from buisness.Outcome.Fees import KOZI


def input_update_kozi():
    # noinspection PyDictCreation
    val = {"const": 0}

    val['b_k'] = 100
    val['b_o'] = 0
    val['b_z'] = 0
    val['b_i'] = 0
    val['m_k'] = 120
    val['m_o'] = 200
    val['m_z'] = 70
    val['m_i'] = 60
    val['f_k'] = 30
    val['f_o'] = 120
    val['f_z'] = 70
    val['f_i'] = 60
    KOZI().update_kozi(val)
