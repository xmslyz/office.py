import calendar


class Call:
    def __init__(self, year):
        self.year = year

    def addRecords(self):
        i = 1
        my_l = ''

        for x in range(1, 13):
            days_in_month = calendar.monthrange(self.year, x)
            for day in range(1, days_in_month[1] + 1):
                days_of_week = calendar.weekday(self.year, x, day)
                my_l += f'{i},' \
                       f'{self.year}-{x:02}-{day:02},' \
                       f'{days_of_week},' \
                       f'" "' \
                       f';\n'
                i += 1

        self.save_file(my_l)

    def save_file(self, cal_data):
        with open('textfile.txt', 'w') as f:
            f.write(cal_data)


def main():
    print("hi")
    Call(2022).addRecords()


if __name__ == '__main__':
    main()
