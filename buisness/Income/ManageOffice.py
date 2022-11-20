from buisness.Database.SQLConnector import Connection
from buisness.Income.Office import OfficeRecord as offrec

def create_office_table():
    """Creates office table"""

    stmt = (
        "CREATE TABLE IF NOT EXISTS office "
        "(o_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
        "o_type TEXT, "
        "o_amount REAL, "
        "o_reciving TEXT, "
        "o_reciving_date TEXT, "
        "o_what_for TEXT, "
        "o_book_ref TEXT, "
        "o_celebration_date TEXT);"
    )
    conn = Connection()
    conn.sql_querry(stmt, dblink="office")

    return None


def find_in_office(column_name, value):
    """Searches in 'office' table where [column_name] is [value]"""

    stmt = f'SELECT * FROM office WHERE {column_name} IS ("{value}")'
    return Connection().sql_querry(stmt, dblink="office")


def count_amount_to_pars():
    """Searches in 'office' table where [column_name] is [value]"""

    stmt = f'SELECT o_amount FROM office WHERE ' \
           f'o_amount IS NOT ("");'
    return Connection().sql_querry(stmt, dblink="office")


def delete_last_form_office():
    """Deletes las record in table

    :exception Raises: "Table is empty"
    """

    # gets list od id's
    get_id = Connection().sql_querry(
        f"SELECT oid FROM office;", dblink="office"
    )

    # deletes the last from the id list
    if get_id:
        stmt = f"DELETE FROM office WHERE o_id = '{max(get_id)[0]}'"
        Connection().sql_querry(stmt, dblink="office")
    else:
        raise Exception("Table is empty")

    return None


def delete_from_office_by_id(oid) -> str:
    """
    Deletes row from office table with given o_id.

    :param oid:
    :return: None
    """

    conn = Connection()
    stmt = f'DELETE FROM office WHERE o_id = "{int(oid)}";'
    conn.sql_querry(stmt, dblink="office")

    return None


def update_office(oid, val):
    """
    Updates office table with given id
    :param oid: record id to update
    :param val: tuple with updates
    :return: None
    """

    conn = Connection()
    # val = ("ty24pe", 4, "reci4v2", "dat24e", "wh42at", "b4o2ok", "c4e2l")
    stmt = (
        f"UPDATE office SET "
        f"o_type = ?, "
        f"o_amount = ?, "
        f"o_reciving = ?, "
        f"o_reciving_date = ?, "
        f"o_what_for = ?, "
        f"o_book_ref = ?, "
        f"o_celebration_date = ? "
        f'WHERE o_id = "{oid}";'
    )
    conn.sql_querry(stmt, value=val, dblink="office")

    return None


def insert_to_office(val):
    """
    Inserts record to office table
    :param val: tuple with record data
    :return: None
    """

    conn = Connection()
    # val = ("type", 1, "reciv", "date", "what", "book", "cel")
    stmt = (
        "INSERT INTO office ("
        "o_id, "
        "o_type, "
        "o_amount, "
        "o_reciving, "
        "o_reciving_date, "
        "o_what_for, "
        "o_book_ref, "
        "o_celebration_date) "
        "VALUES (NULL,?,?,?,?,?,?,?);"
    )
    conn.sql_querry(stmt, value=val, dblink="office")

    return None


def office_income_record(amount, reciving, date_of_r, kind, ref, date_of_c):

    income = offrec()
    income.amount = amount
    income.reciving_priest = reciving
    income.date_of_reciving = date_of_r
    income.kind = kind
    income.reference = ref
    income.date_of_celebration = date_of_c

    val = (
        income.type,
        income.amount,
        income.reciving_priest,
        income.date_of_reciving,
        income.kind,
        income.reference,
        income.date_of_celebration
    )

    return val







