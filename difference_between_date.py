from datetime import date


def diff_dates(date1, date2):
    return abs(date2 - date1).days


def main():
    d1 = date(2021, 12, 1)
    d2 = date(2021, 12, 25)
    result = diff_dates(d2, d1)

    print(f"ci sono {result} giorni tra {d1} e {d2}")

    # per ottenere la stessa stampa
    # print('{} days between {} and {}'.format(result, d1, d2))


main()
