import datetime
import os
import sqlite3
import Database.db_builder as dbb
from Counters import StipendsCounter as sc
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month


class MainMenu:
    # def __init__(self):
    #     pass

    def intro_prompt():
        print('-' * 50)

    def final_prompt():
        print('-' * 50)
        print("Program zakończył działanie")

    def main_options():
        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybierz opcje.')
            print('[1] Stwórz bazę danych')
            print('[2] Zapełnij losowo tabelę bazy danych')
            print('[3] Usuń tabelę z bazy danych')
            print('[4] Usuń bazę danych')
            print('[5] Menu: Wykaz ogólny')
            print('[6] Menu: Wykaz szczegółowy')
            print('\n[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                os.system('cls')
                myDB = dbb.Database()
                myDB.database_creator()
                print(f"Gotowe.")
                print('\n')
                MainMenu.main_options()
            if word == '2':
                os.system('cls')
                print("Opercja może trwać kilka sekund.")
                timebefore = datetime.datetime.now()
                database = DatabaseCalendarFiller()
                try:
                    Month(2022, 11).addRecords(database, 2, 4)
                except sqlite3.OperationalError:
                    print("Tabela nie znajduje się w bazie danych.")
                timeafter = datetime.datetime.now()
                print(f"Gotowe. Wykonano w {timeafter - timebefore} s.")
                print('\n')
                MainMenu.main_options()
            if word == '3':
                os.system('cls')
                dbb.Database.database_table_droper(os.path.join(os.path.abspath(os.getcwd()), "Files\\Database\\default.db"))
                print(f"Gotowe.")
                print('\n')
                MainMenu.main_options()
            if word == '4':
                os.system('cls')
                dbb.Database.path_destroyer(os.path.join(os.path.abspath(os.getcwd()), "Files\\Database\\"))
                print("Gotowe.")
                print('\n')
                MainMenu.main_options()
            if word == '5':
                MainMenu.counter_menu()
            if word == '6':
                MainMenu.detailed_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def counter_menu():
        s_counter = sc.ComputingStipends()
        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybierz opcje.')
            print('[1] Suma przyjętych stypendiów')
            print('[2] Ilość opłaconych mszy')
            print('[3] Ilość odprawionych mszy:')
            print('[4] Zgodność:')
            print('[5] Różnica w "zgodności":')
            print('[6] Średnie stypendium:')
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                os.system('cls')
                print(s_counter.sum_all_stipends())
                print('\n')
                MainMenu.counter_menu()
            if word == '2':
                os.system('cls')
                print(s_counter.sum_of_paid_intentions())
                print('\n')
                MainMenu.counter_menu()
            if word == '3':
                os.system('cls')
                print(s_counter.sum_of_aplicated_stipends())
                print('\n')
                MainMenu.counter_menu()
            if word == '4':
                os.system('cls')
                print(s_counter.bool_if_application())
                print('\n')
                MainMenu.counter_menu()
            if word == '5':
                os.system('cls')
                print(s_counter.evaluate_paid_masses_vs_application())
                print('\n')
                MainMenu.counter_menu()
            if word == '6':
                os.system('cls')
                print(s_counter.mediana_stipends())
                print('\n')
                MainMenu.counter_menu()
            if word == '9':
                os.system('cls')
                MainMenu.main_options()
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

    def priest_menu(priest):
        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybrano księdza "{priest}".')
            print('[1] Ilość wszystkich odprawionych mszy')  #
            print('[2] Ilość "pierwszych" mszy')  #
            print('[3] Całkowite stypendium')  #
            print('[4] Binacje')  #
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()
            father = sc.Priest(priest)
            counter = counter - 1
            if word == '1':
                os.system('cls')
                print(father.number_of_all_masses_applied_by_a_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '2':
                os.system('cls')
                print(father.number_of_first_masses_applied_by_a_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '3':
                os.system('cls')
                print(father.quota_for_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '4':
                os.system('cls')
                print(father.bination_quota_for_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '9':
                os.system('cls')
                MainMenu.main_options()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()
