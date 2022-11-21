import gui.FilterTab.Filter


def main():
    print("hi")
    z = gui.FilterTab.Filter.IntentionsFilter()
    print(z.filter_who_notcelebrated_today("2022-10-31"))


if __name__ == '__main__':
    main()
