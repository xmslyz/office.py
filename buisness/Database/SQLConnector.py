import sqlite3
from buisness.Database import AtributesSetter


class Connection:
    def __init__(self):
        self.path = None
        self.db_name = None
        self.file_path = None
        self.table_name = None

    def __repr__(self):
        return (
            f"Connection:\n\t"
            f"PATH: {self.path}\n\t"
            f"FILE PATH: {self.file_path}\n\t"
            f"DATABASE NAME: {self.db_name}\n\t"
            f"TABLE NAME: {self.table_name}\n"
        )

    def get_conn_details(self, dblink):
        val = KeyGeter().uncode(dblink)

        rs = AtributesSetter.DBSettings()
        rs.db_path = val["path"]
        rs.db_name = val["db_name"]
        rs.db_file_path = val["file"]
        rs.db_table_name = val["table_name"]

        self.path = rs.db_path
        self.db_name = rs.db_name
        self.table_name = rs.db_table_name
        self.file_path = rs.db_file_path

    def __open_connection(self, dblink=None):
        if dblink:
            self.get_conn_details(dblink)

        self.__con = sqlite3.connect(self.file_path)
        self.__cur = self.__con.cursor()

    def sql_querry(self, sql_stmt, value=None, dblink=None) -> str:
        if dblink:
            self.__open_connection(dblink)
        else:
            self.__open_connection()

        try:
            if value:
                self.__cur.execute(sql_stmt, value)
            else:
                self.__cur.execute(sql_stmt)
            return self.__cur.fetchall()
        except:
            raise Exception("No such table. Program will close up now.")
        finally:
            self.__close_conection()

    def __close_conection(self):
        self.__con.commit()
        self.__cur.close()


class KeyGeter:
    as_dic = {
        "constants": {
            "path": "DatabaseLayer\\Constants",
            "db_name": "constants.db",
            "table_name": "constants",
            "file": "",
        },
        "intentions": {
            "path": "DatabaseLayer\\SQLDataBase",
            "db_name": "sofa.db",
            "table_name": "intentions",
            "file": "",
        },
        "employees": {
            "path": "DatabaseLayer\\SQLDataBase",
            "db_name": "sofa.db",
            "table_name": "employees",
            "file": "",
        },
        "monthly_stmt": {
            "path": "DatabaseLayer\\SQLDataBase",
            "db_name": "sofa.db",
            "table_name": "monthly_stmt",
            "file": "",
        },
        "general_stmt": {
            "path": "DatabaseLayer\\SQLDataBase",
            "db_name": "sofa.db",
            "table_name": "general_stmt",
            "file": "",
        },
        "office": {
            "path": "DatabaseLayer\\SQLDataBase",
            "db_name": "sofa.db",
            "table_name": "office",
            "file": "",
        },
        "testintentions": {
            "path": "DatabaseLayer\\TestDataBase",
            "db_name": "sofa.db",
            "table_name": "intentions",
            "file": "",
        },
        "testemployees": {
            "path": "DatabaseLayer\\TestDataBase",
            "db_name": "sofa.db",
            "table_name": "employees",
            "file": "",
        },
        "testmonthly_stmt": {
            "path": "DatabaseLayer\\TestDataBase",
            "db_name": "sofa.db",
            "table_name": "monthly_stmt",
            "file": "",
        },
        "testgeneral_stmt": {
            "path": "DatabaseLayer\\TestDataBase",
            "db_name": "sofa.db",
            "table_name": "general_stmt",
            "file": "",
        },
        "testpars": {
            "path": "DatabaseLayer\\TestDataBase",
            "db_name": "sofa.db",
            "table_name": "pars",
            "file": "",
        },
    }

    def uncode(self, keyname):
        if keyname in self.as_dic:
            return self.as_dic[keyname]
        else:
            raise Exception("Nie ma takiego klucza")

    def constants_getter(const):
        # db = buisness.Database.ScanRecords.Connection()
        # db.get_conn_details(2, 2, 0)
        # result = 0
        if const == "bin":
            # result = db.sql_querry('SELECT value FROM constants '
            #                        'WHERE name IS "binacja";')
            return "50"
        elif const == "inv":
            # result = db.sql_querry('SELECT value FROM constants '
            #                        'WHERE name IS "invited";')
            return "60"
        # return int(result[0][0])
