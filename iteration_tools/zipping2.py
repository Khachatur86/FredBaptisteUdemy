from itertools import zip_longest

def squares():
  i = 0
  while True:
    yield i**2
    i += 1

def cubes():
  i = 0
  while True:
    yield i**3
    i += 1
iter1, iter2 = squares(), cubes()

print(list(zip(iter1, iter2)))