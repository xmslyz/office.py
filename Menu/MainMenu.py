import datetime
import os
import sqlite3
from Counters import StipendsCounter as sc
from Random_Generator.add_calendar import DatabaseCalendarFiller, Month
from Database.db_builder import DatabaseConstructor as dbbuilder


class MainMenu:
    def __init__():
        pass

    def intro_prompt():
        print('-' * 50)

    def final_prompt():
        print('-' * 50)
        print("Program zakończył działanie")

    def menu_main():

        exit_key = "0"
        counter = 3

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
            if word == '2':
                os.system('cls')
                MainMenu.raport_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()

    def db_menu():
        exit_key = "0"
        counter = 3

        while True:
            print(f'Wybierz opcje.')
            print('[1] Stwórz bazę danych')
            print('[2] Zapełnij losowo tabelę bazy danych')
            print('[3] Usuń tabelę z bazy danych')
            print('[4] Usuń bazę danych')
            print('\n[9] Wróć do poprzedniego menu')
            print('\n[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                os.system('cls')
                self.build_db.db_constructor()
                print(f"Gotowe.")
                print('\n')
                # MainMenu.db_menu()
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
                # MainMenu.db_menu()
            if word == '3':
                os.system('cls')
                # myDB.database_table_droper(os.__path.join(os.__path.abspath(os.getcwd()), "Files\\DatabaseConstructor\\default.db"))
                # myDB.database_table_droper()
                print(f"Gotowe.")
                print('\n')
                # MainMenu.db_menu()
            if word == '4':
                os.system('cls')
                # myDB.path_destroyer()
                # myDB.path_destroyer(os.__path.join(os.__path.abspath(os.getcwd()), "Files\\DatabaseConstructor\\"))
                print("Gotowe.")
                print('\n')
                # MainMenu.db_menu()
            if word == '9':
                os.system('cls')
                # MainMenu.menu_main()
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
        s_counter = sc.ComputingStipends("mass_intentions")
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
            print('[7] Ilość mszy gregoriańskich:')
            print('\n[9] Wróć do poprzedniego menu')
            print('[0] Opuść program')
            print('-' * 50)
            word = input("Enter number: ").lower()

            counter = counter - 1
            if word == '1':
                os.system('cls')
                print(f'{s_counter.amount_of_all_stipends_recived()} zł')
                print('\n')
                MainMenu.counter_menu()
            if word == '2':
                os.system('cls')
                print(s_counter.amount_of_all_paid_intentions())
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
                print(f'{s_counter.mediana_stipends()} zł')
                print('\n')
                MainMenu.counter_menu()
            if word == '7':
                os.system('cls')
                print(f'{s_counter.amount_of_all_gregorian_intentions()}')
                print('\n')
                MainMenu.counter_menu()
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
                print(father.amount_of_all_masses_applied_by_a_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '2':
                os.system('cls')
                print(father.amount_of_first_masses_applied_by_a_priest())
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '3':
                os.system('cls')
                print(f'{father.quota_for_priest()} zł')
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '4':
                os.system('cls')
                print(f'{father.bination_quota_for_priest()} zł')
                print('\n')
                MainMenu.priest_menu(priest)
            if word == '9':
                os.system('cls')
                MainMenu.raport_menu()
            if word == '0':
                exit()
            if word != exit_key and counter < 1:
                exit()
