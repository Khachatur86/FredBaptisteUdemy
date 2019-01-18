class CyclicIterator:
  def __init__(self, lst):
    self.lst = lst
    self.i = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    result = self.lst[self.i % len(self.lst)]
    self.i += 1
    return result

iter_cycl = CyclicIterator("NSWE")
numbers = range(10)

print(list(zip(numbers, iter_cycl)))
# print(list(zip(iter_cycl, numbers))) - интересно
iter_cycl = CyclicIterator("NSWE")
n = 10
for i in range(1, n+1):
  direction = next(iter_cycl)
  print(f"{i}{direction}")

iter_cycl = CyclicIterator("NSWE")
n = 10
items = [f"{i}{next(iter_cycl)}" for i in range(1, n+1)]
print(items)

iter_cycl = CyclicIterator("NSWE")
n = 10
items = [str(number) + direction
       for number,direction in zip(range(1, n+1), iter_cycl)]

print("\n", items)

import itertools
iter_cycl = itertools.cycle("NSWE")
items = [f"{i}{next(iter_cycl)}" for i in range(1, n+1)]
print("asdf", items)