import datetime
import random
from Income.stipend_income import MassStipend, CountStipends


def random_value_list_generator(array_from, array_to):
    n = random.randint(array_from, array_to)  # zakres przyjętych w miesiącu mszy
    sack = []
    celebration_date = datetime.datetime.now()
    celebration_type = ["in loco", "extra", "gregorianas", "pro defunctis", "pro sponsos", "pro baptismatos"]
    amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
    priests = ["p1", "p2", "p3", "p4", "p5"]  # lista księży na parafii

    for _ in range(n):
        j = ("Stypendium", random.choice(amounts), random.choice(priests), random.choice(priests), celebration_date, random.choice(celebration_type))
        sack.append(j)
    print(f"Wygenerowano {len(sack)} pozycji")
    return sack


def random_values_generator():
    n = random.randint(150, 220)  # zakres przyjętych w miesiącu mszy
    sack = []
    celebration_date = datetime.datetime.now()
    celebration_type = ["in loco", "extra", "gregorianas", "pro defunctis", "pro sponsos", "pro baptismatos"]
    amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
    priests = ["q1", "q2", "q3", "q4", "q5"]  # lista księży na parafii

    # generator na potrzeby testu funkcji
    for _ in range(n):
        j = MassStipend("Stypendium", random.choice(amounts), random.choice(priests), random.choice(priests), celebration_date, random.choice(celebration_type))
        sack.append(j)

    print(f'Suma wszystkich stypendiów w tym miesiącu wynosi: {CountStipends.sum_all_stipends(sack)} zł')
    print(f'Ilość mszy w miesiącu wyniosła: {CountStipends.sum_of_masses(sack)}')
    print(f'{CountStipends.mediana_stipends(sack):.2f} zł')
    print("")
    for x in priests:
        print(f'{x} przyjął stypendiów w kwocie {CountStipends.sum_stipends_recived_by_a_priest(sack, x)} zł')
        print(f'Lista przyjętych stypendiów {CountStipends.list_of_stipends_recieved_by_a_priest(sack, x)}')
        print(f'{x} odprawił {CountStipends.sum_of_applied_masses(sack, x)} mszy.')
        print(f'{CountStipends.quota(sack, x):.2f} zł')
        print()
