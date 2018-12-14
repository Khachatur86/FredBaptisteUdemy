def checkio(text: str) -> str:

    return {key: value for key, value in zip(text,[text.count(x) for x in text])}


print(checkio("Hello World!!"))
print(checkio("one"))
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio("Hello World!"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert  == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#     print("The local tests are done.")