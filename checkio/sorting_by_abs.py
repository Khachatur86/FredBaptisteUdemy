def checkio(numbers_array: tuple) -> list:

    """
    Сортировка по абсолютному (модулю) значению
    :param numbers_array:
    :return:
    """
    return sorted(numbers_array, key=lambda x: abs(x))

