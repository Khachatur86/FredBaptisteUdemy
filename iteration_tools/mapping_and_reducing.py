maps = map(lambda x: x**2, range(5))
print(list(maps))
from itertools import starmap

def add(t):
  return t[0] + t[1]

print(list(map(add, [(0, 0), [1, 1], range(2,4)])))

def add(x, y):
  return x + y

t = (2, 2)
print(add(*t))

# print(list(map(add, [(0, 0), [1, 1], range(2,5)])))

print([add(*t) for t in [(0, 0), [1, 1], range(2,4)]])

print(list(starmap(add,  [(0, 0), [1, 1], range(2,4)])))

from functools import reduce

print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))

def sum_(iterable):
  it = iter(iterable)
  acc = next(it)
  yield acc
  for item in it:
    acc += item
    yield acc

for item in sum_([1, 3, 4, 6]):
  print(item)

def running_reduce(fn, iterable, start=None):
  it = iter(iterable)
  if start is None:
    acc = next(it)
  else:
    acc = start
  yield acc

  for item in it:
    acc = fn(acc, item)
    yield acc

print(list(running_reduce(lambda x, y: x+y, [10, 20,30])))