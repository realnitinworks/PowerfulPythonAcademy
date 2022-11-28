import sys


def house_records(filename):
    with open(filename) as f:
        try:
            while True:
                address_line, area_line, price_line = next(f), next(f), next(f)
                yield dict(
                    (
                        address_line.strip().split(": "),
                        area_line.strip().split(": "),
                        price_line.strip().split(": "),
                    )
                )
                next(f)
        except StopIteration:
            return


if __name__ == "__main__":
    filename = sys.argv[1]
    for house in house_records(filename=filename):
        print(house)
