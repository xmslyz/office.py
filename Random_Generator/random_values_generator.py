import random
from Income.stipend_income import MassStipend
from Counters.StipendsCounter import ComputingStipends


def random_value_list_generator(array_from, array_to):
    n = random.randint(array_from, array_to)  # zakres przyjętych w miesiącu mszy
    sack = []
    stipend_type = ["Stypendium mszalne"]
    year = 2022
    month = range(1, 13)
    day = range(1, 31)
    celebration_time = ["06:30", "07:00", "09:00", "10:30", "12:00", "14:00", "18:00", "19:30"]
    celebration_type = ["in loco", "extra", "gregorianas", "pro defunctis", "pro sponsos", "pro baptismatos"]
    amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
    priests = ["p1", "p2", "p3", "p4", "p5"]  # lista księży na parafii
    first_mass = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for _ in range(n):
        j = (
            stipend_type[0],
            random.choice(amounts),
            random.choice(priests),
            random.choice(priests),
            f'{year}-{random.choice(month):02}-{random.choice(day):02}',
            random.choice(celebration_time),
            random.choice(celebration_type),
            random.choice(first_mass)
        )
        print(j[4])
        if (j[4][5:7]) != "02":
            if (j[4][8:]) != "30":
                sack.append(j)
    print(f"AutoRandomGenerated: {len(sack)} rows")
    return sack


def table_reader(sack, priest):
    # n = random.randint(150, 220)  # zakres przyjętych w miesiącu mszy
    # sack = []
    # celebration_date = datetime.datetime.now()
    # celebration_type = ["in loco", "extra", "gregorianas", "pro defunctis", "pro sponsos", "pro baptismatos"]
    # amounts = [100, 50, 60, 70, 80]  # przykładowe ofiary za mszę
    # priests = ["q1", "q2", "q3", "q4", "q5"]  # lista księży na parafii
    #
    # # generator na potrzeby testu funkcji
    # for _ in range(n):
    #     j = MassStipend("Stypendium", random.choice(amounts), random.choice(priests), random.choice(priests),
    #                     celebration_date, random.choice(celebration_type))
    #     sack.append(j)

    print(f'Suma wszystkich stypendiów w tym miesiącu wynosi: {ComputingStipends.sum_all_stipends(sack)} zł')
    print(f'Ilość mszy w miesiącu wyniosła: {ComputingStipends.sum_of_masses(sack)}')
    print(f'{ComputingStipends.mediana_stipends(sack):.2f} zł')
    print("")

    # for x in priests:
    #     print(f'{x} przyjął stypendiów w kwocie {ComputingStipends.sum_stipends_recived_by_a_priest(sack, x)} zł')
    #     print(f'Lista przyjętych stypendiów {ComputingStipends.list_of_stipends_recieved_by_a_priest(sack, x)}')
    #     print(f'{x} odprawił {ComputingStipends.sum_of_applied_masses(sack, x)} mszy.')
    #     print(f'{ComputingStipends.quota(sack, x):.2f} zł')
    #     print()
