def long_repeat(line):
    count = 1
    max_count = 0
    for index in range(len(line) - 1):
        if line[index] == line[index + 1]:
            count += 1
        if count > max_count:
            max_count = count
        if line[index] != line[index + 1]:
            count = 1
    return max_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
