import math

def factorials(n):
  for i in range(n):
    yield math.factorial(i)

facts = factorials(100)

def slice_(iterable, start, stop):
  for _ in range(0, start):
    next(iterable)
  for _ in range(start, stop):
    yield next(iterable)

from itertools import islice

print(list(islice(factorials(100), 0, 10, 5)))
print(type(slice_(factorials(10), 3, 10)))
def factorials():
  index = 0
  while True:
    print(f"yielding factorial({index})...")
    yield math.factorial(index)
    index += 1

facts = factorials()

for _ in range(0, 5):
  print(next(facts))

print(islice(factorials(), 3, 10))
print(list(islice(factorials(), 3, 10)))