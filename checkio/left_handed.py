# One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.
# You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.
# Input: A sequence of strings as a tuple of strings (unicode).
# Output: The text as a string.
# Precondition:
# 0 < len(phrases) < 42
from functools import reduce
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    phrase_transform = reduce(lambda x, y: x + y, (phrase.split() for phrase in phrases))
    return ",".join((str.replace("right", "left") for str in phrase_transform))