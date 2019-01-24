from itertools import count, cycle, repeat, islice

# count 

g = count(10)

print(list(islice(g, 4)))
g = count(10, 0.5)
print(list(islice(g, 5)))

#with complex numbers
g = count(1+1j, 1+2j)

print(list(islice(g, 5)))

# with decimal
from decimal import Decimal

g = count(Decimal('0'), Decimal('0.1'))
print(list(islice(g, 5)))

# cycle
g = cycle(("red", "green", "blue"))

print(list(islice(g, 5)))

def colors():
  yield 'red'
  yield 'green'
  yield 'blue'

cols = colors()

print(list(cols))
print(list(cols))

cols = colors()
g = cycle(cols)

print(list(islice(g, 10)))
from collections import namedtuple
Card = namedtuple("Card", "rank suit")

def card_deck():
  ranks = tuple(str(num) for num in range(2,11)) + tuple("JQKA")
  suits = ("Spades", "Hearts", "Diamonds", "Clubs")
  for suit in suits:
    for rank in ranks:
      yield Card(rank, suit)

print(list(islice(card_deck(), 10)))

hands = [list() for _ in range(4)]
print(hands)
index = 0
for card in card_deck():
  index = index % 4
  hands[index].append(card)
  index += 1

print(hands[0], "\n", hands[1])