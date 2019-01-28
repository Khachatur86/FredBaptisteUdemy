l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

# for gen in l1, l2, l3:
#   for item in gen:
#     print(item)

def chain_iterables(*iterables):
  for iterable in iterables:
    yield from iterable

l4 = chain_iterables(l1, l2, l3)
print(list(l4))

from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

for item in chain.from_iterable([l1, l2, l3]):
  print(item)

# def squares():
#   print("yielding 1st item")
#   yield (i**2 for i in range(4))
#   print("yielding 2nd item")
#   yield (i**2 for i in range(4,8))
#   print("yielding 3rd item")
#   yield (i**2 for i in range(8,12))

# for item in chain(squares()):
#   print(item)

# for item in chain(*squares()):
#   print(item)

# def read_values(*values):
#   print("Finished reading values")

# read_values(*squares())