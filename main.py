import random
from Income.stipendIncome import massPayment, count_stipends


def main():
    n = random.randint(150, 220)
    i = 0
    sack = []
    priests = ["p1", "p2", "p3", "p4", "p5"]

    while i < n:
        rand_stipend_amount = random.choice([50, 60, 70])
        rand_priest = random.choice(priests)
        rand_reciever = random.choice(priests)
        j = massPayment(rand_stipend_amount, rand_reciever, rand_priest)
        sack.append(j)
        i += 1

    for x in priests:
        print(f'{x} przyjął stypendiów w kwocie {count_stipends.sum_stipends_for_reciver(sack, x)} zł')
        print(count_stipends.list_of_stipends_for_reciever(sack, x))
        print(count_stipends.sum_of_applied_masses(sack, x))
        print(f'{count_stipends.payment_title_mass(sack, x):.2f} zł')
        print("---")

    print(f'Suma wszystkich stypendiów w tym miesiącu wynosi: {count_stipends.sum_all_stipends(sack)} zł')
    print(f'Ilość mszy w miesiącu wyniosła: {count_stipends.sum_of_masses(sack)}')
    print(f'{count_stipends.mediana_stipends(sack):.2f} zł')


if __name__ == '__main__':
    main()
