import re
from collections import Counter


def checkio(text: str) -> str:
    text = re.sub('\W|\d', '', text).lower()
    if len(text) == len(set(text)):
        return sorted(text)[0]
    counter_dict = dict(Counter(text))
    sorted_counter_dict = sorted(counter_dict.items(), \
                                 key=lambda x: x[1], reverse=True)
    max_num_of_char = max(sorted_counter_dict, key=lambda x: x[1])[1]

    filtred_sorted_dict = [char for char in sorted_counter_dict \
                           if char[1] == max_num_of_char]

    return sorted(filtred_sorted_dict, key=lambda x: x[0])[0][0]


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