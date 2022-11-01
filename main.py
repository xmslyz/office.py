from Database import db_builder as dbb


def main():
    # mm.intro_prompt()
    # mm.menu_main()
    # mm.final_prompt()

    path = "myPath"
    dbname = "m+y-S*Q+L@b'a>s?e.exe"
    table_name = "mojatabelka"

    mysql = (("type TEXT NOT NULL",),
             ("amount REAL",),
             ("priest_reciving TEXT",),
             ("celebrated_by TEXT",),
             ("celebration_date TEXT",),
             ("celebration_hour TEXT",),
             ("celebration_type TEXT",),
             ("first_mass INTEGER",))
    dbb.DatabaseBuilder.builder(path, dbname, table_name, mysql)


if __name__ == '__main__':
    main()
