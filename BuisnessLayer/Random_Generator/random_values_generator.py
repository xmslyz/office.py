import random


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
