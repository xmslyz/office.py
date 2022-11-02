import datetime
import os
import sqlite3

import main
from Counters import StipendsCounter as sc
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month


class MainMenu:
    """
    TA KLASA JEST TYLKO I WYŁĄCZNIE TYMCZASOWA. MA USPRAWNIĆ TESTOWANIE MODUŁÓW I SPRAWDZANIE WYNIKÓW.
    JAK SIĘ NAUCZĘ ROBIĆ TESTY TO BĘDZIE USUNIĘTA.
    NA RAZIE MUSZĘ SOBIE RADZIĆ TAK :)
    """
    def __init__():
        pass

    def intro_prompt():
        print('-' * 50)

    def final_prompt():
        print('-' * 50)
        print("Program zakończył działanie")

    def menu_main():

        exit_key = "0"
        counter = 2
        while True:
            print(f'Wybierz opcje.')
            print('[1] Baza danych')
            print('[2] Raporty')
            print('\n[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()
            counter = counter - 1

            if word == '1':
                os.system('cls')
                MainMenu.db_menu()
            if word == '2':
                os.system('cls')
                MainMenu.raport_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def db_menu():
        my_path = "Files\\Databases\\default.db"
        my_table = "intentions"

        assert my_path == "Files\\Databases\\default.db"
        assert my_table == "intentions"

        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybierz opcje.')
            print('[1] Stwórz bazę danych')
            print('[2] Zapełnij losowo tabelę bazy danych')
            print('[3] Usuń bazy danych')
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                os.system('cls')
                main.budowa_bazy_danych()
                MainMenu.db_menu()
            if word == '2':
                os.system('cls')
                print("Opercja może trwać kilka sekund.")
                timebefore = datetime.datetime.now()
                database = DatabaseCalendarFiller(my_path)
                try:
                    Month(2022, 11).addRecords(my_table, database, 2, 4)
                except sqlite3.OperationalError:
                    print("Tabela nie znajduje się w bazie danych.")

                timeafter = datetime.datetime.now()
                print(f"Gotowe. Wykonano w {timeafter - timebefore} s.")
                print('\n')
                MainMenu.db_menu()
            if word == '3':
                os.system('cls')
                main.destrukcja_bazydanych()
                print(f"Gotowe.")
                print('\n')
                MainMenu.menu_main()
            if word == '9':
                os.system('cls')
                MainMenu.menu_main()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def raport_menu():
        exit_key = "0"
        counter = 3
        while True:
            print(f'Wybierz opcje.')
            print('[1] Wykaz ogólny')
            print('[2] Wykaz szczegółowy')
            print('\n[9] Wróć do poprzedniego menu')
            print('\n[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                MainMenu.counter_menu()
            if word == '2':
                MainMenu.detailed_menu()
            if word == '0':
                exit()
            if word == '9':
                os.system('cls')
                MainMenu.raport_menu()
            if word != exit_key and counter < 1:
                exit()

    def counter_menu():
        table_name = "intentions"
        assert table_name == "intentions"

        s_counter = sc.ComputingStipends(table_name)
        exit_key = "0"
        counter = 3

        while True:
            print(f'{s_counter.sum_of_all_recived()} zł')
            print(s_counter.amount_of_all_paid())
            print(s_counter.amount_of_aplicated())
            print(s_counter.paid_not_applicated())
            print(f'{s_counter.mediana()} zł')
            print(f'{s_counter.amount_of_all_gregorian()}')
            print('-' * 50)
            print('-' * 50)
            print(f'Wybierz opcje.')
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()
            counter = counter - 1
            if word == '9':
                os.system('cls')
                MainMenu.raport_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def detailed_menu():
        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybierz księdza.')
            print('[1] p1')
            print('[2] p2')
            print('[3] p3')
            print('[4] p4')
            print('[5] p5')
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()
            counter = counter - 1
            if word == '1':
                os.system('cls')
                MainMenu.priest_menu(f'p{word}')
            if word == '2':
                os.system('cls')
                MainMenu.priest_menu(f'p{word}')
            if word == '3':
                os.system('cls')
                MainMenu.priest_menu(f'p{word}')
            if word == '4':
                os.system('cls')
                MainMenu.priest_menu(f'p{word}')
            if word == '5':
                os.system('cls')
                MainMenu.priest_menu(f'p{word}')
            if word == '9':
                os.system('cls')
                MainMenu.detailed_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def priest_menu(queried_priest):
        table_name = "intentions"
        assert table_name == "intentions"
        exit_key = "0"
        counter = 3
        while True:
            print(f'Wybrano księdza "{queried_priest}".')
            pc = sc.Priest(table_name, "p1")
            print(pc.amount_of_all_masses_applied_by_a_priest())
            print(pc.amount_of_first_masses_applied_by_a_priest())
            print(pc.amount_of_bination_applied_by_a_priest())
            print(pc.quota_for_priest())
            print(pc.bination_quota_for_priest())
            print(pc.total_wage_for_priest())
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()
            counter = counter - 1
            if word == '9':
                os.system('cls')
                MainMenu.raport_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()
