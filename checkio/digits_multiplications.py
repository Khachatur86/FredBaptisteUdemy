from functools import reduce


def checkio(number: int) -> int:
    return reduce(lambda x, y: int(x) * int(y) if x != "0" and y != "0" else int(x), str(number))