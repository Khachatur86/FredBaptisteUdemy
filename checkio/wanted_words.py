def checkio(text: str) -> str:
    text = "".join([x for x in text if 64 < ord(x) < 123]).lower()
    char_count_dict = {key: value for key, value in zip(text, [text.count(x) for x in text])}
    max_values = max(char_count_dict.values())
    new_dict = {}
    for elem in char_count_dict:
        if char_count_dict[elem] == max_values:
            new_dict[elem] = max_values
    return min(new_dict)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")