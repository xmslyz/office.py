import datetime
import random


def random_data():  # na potrzeby testów
    amount = random.choice([50, 60, 70, 80, 100])
    reciving_priest = random.choice(["PK", "TO", "DC", "WM", "MS"])
    celebrating_priest = random.choice(["PK", "TO", "DC", "WM", "MS", "SOL"])
    hour_of_celebration = random.choice(["06:30:00", "07:00:00", "18:00:00"])
    date_of_celebration = datetime.datetime.now().strftime("%Y-%m-%d")
    type_of_mass = ""
    is_gregorian = False
    return amount, reciving_priest, celebrating_priest, hour_of_celebration, date_of_celebration, type_of_mass, is_gregorian
