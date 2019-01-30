import itertools

def matrix(n):
  for i in range(1, n+1):
    for j in range(1, n+1):
      yield f"{i} x {j} = {i*j}"


print(list(itertools.islice(matrix(10), 10, 20)))

l1 = ["x1", "x2", "x3", "x4"]
l2 = ["y1", "y2", "y3"]
for x in l1:
  for y in l2:
    print((x, y), end=" ")
  print('')

for el in itertools.product(l1, l2):
  print(el)

def matrix(n):
  for i in range(1, n+1):
    for j in range(1, n+1):
      yield (i, j, i*j)

print(list(matrix(5)))

def matrix(n):
  yield from itertools.product(range(1, n+1), range(1, n+1))

print(list(matrix(7)))

def matrix(n):
  return ((i, j, i*j) 
  for i, j in itertools.product(range(1, n+1), range(1, n+1)))

print(list(matrix(4)))

from itertools import tee

def matrix(n):
  return ((i, j, i*j) 
            for i, j in itertools.product(*tee(range(1, n+1), 2)))

print(list(matrix(8)))


def grid(min_val, max_val, step, *, num_dimensions=2):
  axis = itertools.takewhile(lambda x: x<= max_val,
                      itertools.count(min_val, step))
  axes = itertools.tee(axis, num_dimensions)
  return itertools.product(*axes)
  

print(list(grid(-1, 1, 0.5)))

sample_space = list(itertools.product(range(1,7), range(1,7)))

print(list(itertools.product([1, 2, 3], [4, 5], [6])))

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))

print(outcomes)
print(len(outcomes))
l1 = 'abc'
print(list(itertools.permutations(l1)))

print(list(itertools.combinations([1, 2, "da", 4], 2)))

SUITS = "SHDC"
RANKS = tuple(map(str, range(2, 11))) + tuple("JQKA")

dec = [rank + suit for suit in SUITS for rank in RANKS]

print(list(itertools.product(SUITS, RANKS)))

from fractions import Fraction
from collections import namedtuple
Card = namedtuple('Card', "rank suit")

deck = (Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS))
sample_space = itertools.combinations(deck, 4)
total = 0
acceptable =0
for outcome in sample_space:
  total += 1
  for card in outcome:
    if card.rank != "A":
      break
    else:
      acceptable += 1

print(f"total={total}, acceptable={acceptable}")
print("odds = {}".format(Fraction(acceptable, total)))
print("odds = {:10f}".format(acceptable/total))