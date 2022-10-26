import random
from Income.stipendIncome import massPayment, count_stipends


def main():
    #  Dane do generatora
    n = random.randint(150, 220)  # zakres przyjętych w miesiącu mszy
    i = 0
    sack = []
    amounts = [50, 60, 70, 80]  # przykładowe ofiary za mszę
    priests = ["p1", "p2", "p3", "p4", "p5"]  # lista księży na parafii

    # generator na potrzeby testu funkcji
    while i < n:
        j = massPayment(random.choice(amounts), random.choice(priests), random.choice(priests))
        sack.append(j)
        i += 1

    # do konsoli
    for x in priests:
        print(f'{x} przyjął stypendiów w kwocie {count_stipends.sum_stipends_for_reciver(sack, x)} zł')
        print(count_stipends.list_of_stipends_for_reciever(sack, x))
        print(count_stipends.sum_of_applied_masses(sack, x))
        print(f'{count_stipends.quota(sack, x):.2f} zł')
        print("---")

    print(f'Suma wszystkich stypendiów w tym miesiącu wynosi: {count_stipends.sum_all_stipends(sack)} zł')
    print(f'Ilość mszy w miesiącu wyniosła: {count_stipends.sum_of_masses(sack)}')
    print(f'{count_stipends.mediana_stipends(sack):.2f} zł')


if __name__ == '__main__':
    main()
