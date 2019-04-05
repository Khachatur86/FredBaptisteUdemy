d = {'a': 1, 'b': 2}

# Dinamyc strucutres
keys = d.keys() # behave like a set
values = d.values()
items = d.items()
print(keys)
print(values)
print(items)

d['a'] = 10

print(keys)
print(values)
print(items)

del d['b']
d['c'] = 100
print(keys)
print(values)
print(items)

s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}
print(f"s1 = {s1}, s2 = {s2}")
# union
print('union',s1 | s2)
# intersection
print('intersection', s1 & s2)
# difference
print('difference',s1 - s2)

# Coding exercise

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f"s1 = {s1}, s2 = {s2}")
# union
print('union',s1 | s2)
# intersection
print('intersection', s1 & s2)
# difference
print('difference',s1 - s2)


# Lets create 2 dicts 
from pprint import pprint
d1 = {'a': 1, 'b':2, 'c':3}
d2 = dict(zip('cde', [30, 4, 5]))
pprint(f"d1 = {d1}, d2 = {d2}")

# Iter in d.keys
for key in d1.keys():
  print(key)

# Iter in d.values
for value in d1.values():
  print(value)

# iter with d.items

for item in d1.items():
  print(item)


pprint(f"type(d1.keys())={type(d1.keys())}, d1.keys() - {d1.keys()}")
pprint(f"type(d2.keys())={type(d2.keys())}, d2.keys() - {d2.keys()}")

union = d1.keys() | d2.keys()
print('union - ', union)

intersection = d1.keys() & d2.keys()

print('intersection - ',intersection)

print('d1.items() | d2.items()  is \n', d1.items() | d2.items())

# Ex2 

d3 = {'a': [1, 2], 'b': [3, 4]}
d4 = {'b': [30, 40], 'c': [5, 6]}

# hash(d3) # unhashable dict
# in this case d3.items() d4.items does not work because of d3 and d4 are not hashable objects

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}

k1 = d1.keys()
k2 = d2.keys()

print(k1 & k2)

new_dict = {}
for key in d1.keys() & d2.keys():
  new_dict[key] = d1[key], d2[key]
print(new_dict)

new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)
#  Another example
d1 = {'a': 1, 'b':2, 'c': 3, 'd': 4}
d2 = {'a': 10,'b': 20, 'c': 30, 'e': 5}

union = d1.keys() | d2.keys()

print(union)

intersection = d1.keys() & d2.keys()

print(intersection)

print(union - intersection)

print(d1.keys() ^ d2.keys())

#  Another example
d1 = {'a': 1, 'b':2, 'c': 3, 'd': 4}
d2 = {'a': 10,'b': 20, 'c': 30, 'e': 5}

union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection
print(keys)
results = {}
for key in keys:
  results[key] = d1.get(key) or d2.get(key)

print(results)

