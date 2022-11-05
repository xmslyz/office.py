import os
import sqlite3
from sqlite3 import Error

import BuisnessLayer.Database.AtributesSetter


class DBConnector:
    def __init__(self, path, dbname, table_name):
        setup_db = BuisnessLayer.Database.AtributesSetter.DBSettings()
        setup_db.db_path = path
        setup_db.db_name = dbname
        setup_db.db_table_name = table_name
        setup_db.db_full_path = ""

        self.path = setup_db.db_path
        self.dbname = setup_db.db_name
        self.table_name = setup_db.db_table_name
        self.full_path = setup_db.db_full_path
        assert self.path == "DatabaseLayer\\SQLDataBase\\"

    def is_path(self) -> str:
        db_dir = os.path.join(os.path.abspath(os.getcwd()), self.path)
        return True if os.path.exists(db_dir) else False

    def make_path(self):
        db_dir = os.path.join(os.path.abspath(os.getcwd()), self.path)
        os.makedirs(db_dir, mode=0o700, exist_ok=True)
        db_dir = os.path.join(db_dir, self.dbname)
        return db_dir

    def create_connection(self, sql_stmt, val):
        if not self.is_path():
            self.make_path()
        result = ()
        try:
            conn = sqlite3.connect(self.full_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cur = conn.cursor()
            cur.execute(sql_stmt, val)
            result = cur.fetchall()
            conn.commit()
            cur.close()
        except Error as e:
            print(e)
        return result
