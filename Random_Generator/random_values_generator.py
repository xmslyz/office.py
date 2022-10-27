import random
from Income.stipendIncome import MassStipend, CountStipends


def random_values_generator():
    n = random.randint(150, 220)  # zakres przyjętych w miesiącu mszy
    i = 0
    sack = []
    amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
    priests = ["p1", "p2", "p3", "p4", "p5"]  # lista księży na parafii

    # generator na potrzeby testu funkcji
    for _ in range(n):
        j = MassStipend("Stypendium", random.choice(amounts), random.choice(priests), random.choice(priests))
        sack.append(j)
        i += 1

    # do konsoli
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
