d = {'a': 1, 'b':2}
keys = d.keys()
values = d.values()
items = d.items()
print('keys', keys)
print('values', values)
print('items', items)
print(f"id(keys)-{id(keys)}")
print(f"id(values)-{id(values)}")
print(f"id(items)-{id(items)}")
d['z'] = 10

print('=====After=====')
print('keys', keys)
print('values', values)
print('items', items)
print(f"id(keys)-{id(keys)}")
print(f"id(values)-{id(values)}")
print(f"id(items)-{id(items)}")
print('\n=====Ex2=====\n')
d = dict(zip('abc', range(1,4)))
for k,v in d.items():
  print(k,v)
  # del d[k] # runtime error

print('\n=====Ex3=====\n')
d = dict(zip('abc', range(1,4)))
for k, v in d.items():
  print(k,v)
  # d['z'] = 10 # runtime error

print('\n=====Ex4=====\n')
d = dict(zip('abc', range(1,4)))
for k, v in d.items():
  print(k,v)
  d[k] = 1000
print(d)

print('\n=====Ex5=====\n')
d = dict(zip('abc', range(1,4)))
for k, v in d.items():
  print(k,v)
  d['c'] = 1000
print(d)

print('\n=====Ex6=====\n')
d = dict(zip('abc', range(1,4)))
for k, v in d.items():
  print(k,v)
  # del d[k] # runtime error
print(d)


d = dict.fromkeys('python', 0)

for k in d:
  print(k)


d_iter = iter(d)
for k in d_iter:
  print(k)

from timeit import timeit
from random import randint

d = {k: randint(0, 100) for k in range(10_000)}
keys = d.keys()

def iter_direct(d):
    for k in d:
        pass
    
def iter_view(d):
    for k in d.keys():
        pass

def iter_view_direct(view):
    for k in view:
        pass
    
print(timeit('iter_direct(d)', globals=globals(), number=20_000))
print(timeit('iter_view(d)', globals=globals(), number=20_000))
print(timeit('iter_view_direct(keys)', globals=globals(), number=20_000))



d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
  print(k, d[k])

d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
  print(k, v)


d = {k: randint(0, 100) for k in range(10_000)}
items = d.items()

def iterate_view(view):
    for k, v in view:
        pass
    
def iterate_clunky(d):
    for k in d:
        d[k]
        
print(timeit('iterate_view(items)', globals=globals(), number=5_000))
print(timeit('iterate_clunky(d)', globals=globals(), number=5_000))

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v ** 2)
    # del d[k] # runtime error


print(d)