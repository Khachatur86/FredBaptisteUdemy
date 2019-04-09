d = {'a': 1, 'b':2, 'c': 3}

d['b'] = 200

print(d)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d1.update(d2)

print(d1)

d1.update(b=20, x=40, c=30)
print(d1)

d1.update([('h', 6), ('k', 78)])
from pprint import pprint
pprint(d1)

d1 = {'a': 4}

# dict.update(iterable - object)
d1.update((k, ord(k)) for k in 'python')

pprint(d1)

# Another method for updating **

d1 = {'a': 1, 'b': 2}
d2 = {'c':3, 'd': 4}

d = {**d1, **d2}

print(d)

# Last wins

d1 = {'a': 1, 'b': 2}
d2 = {'b':25, 'd': 4}

d = {**d1, **d2}

print(d)

conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)

conf_global = {'port': 5432, 'database': 'deepdive'}

conf_def = {
  'host': 'localhost', 
  'user': 'test', 
  'pwd': 'test'
}

conf_prod = {
  'host': 'prodpg.deepdive.com', 
  'user': '$prod_user',
  'pwd': '$prod_pwd',
  'database': 'deepdive_prod'
}

# conf --> global --> dev/prod

conf = {**conf_defaults, **conf_global, **conf_def}

pprint(conf)

conf = {**conf_defaults, **conf_global, **conf_prod}

pprint(conf)

def my_func(*, kw1, kw2, kw3):
  print(kw1, kw2, kw3)

d = {'kw2': 20, 'kw1': 10, 'kw3': 30}

my_func(**d)

def my_func(**kwargs):
  for k, v in kwargs.items():
    print(k, v)


my_func(a=1, b=2)

my_func(b=1, a=2)

my_func(**d)

d = {
  'a': [1, 2],
  'b': [3, 4]
}

# Shallow copy
d1 = d.copy()

pprint(d)
pprint(d1)
print('d is d1 - ',d is d1)
print("d['a'] is d1['a'] - ", d['a'] is d1['a'])

d['a'].append(12)
print(d1)

d['x'] = 100
print('d=',d)
print('d1=',d1)

del d['a']
print('d=',d)
print('d1=',d1)


# deepcopy

from copy import deepcopy

d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }

d1 = deepcopy(d)

d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)

print('d=',d)
print('d1=',d1)


# Unpacking is shallowcopy

d1 = {
  'a': [1, 2], 
  'b': [3, 4]
}

d = {**d1, 'c':100}

print(d)

print(d['a'] is d1['a']) #Unpacking is a shallowcopy


d1 = {
  'a': [1, 2],
  'b': [3, 4]
}

d = {k: v for k,v in d1.items()} # this also is shallow copiing

print(d1['a'] is d['a'])


from random import randint

big_d = {k: randint(1, 100) for k in range(1_000_000)}

# print(len(big_d))

def copy_unpacking(d):
    d1 = {**d}
    
def copy_copy(d):
    d1 = d.copy()

def copy_create(d):
    d1 = dict(d)
    
def copy_comprehension(d):
    d1 = {k: v for k, v in d.items()}

def copy_deepcopy(d):
  d1 = deepcopy(d)

from timeit import timeit

print('unpacking',timeit('copy_unpacking(big_d)', globals=globals(), number=100))
print('copy()',timeit('copy_copy(big_d)', globals=globals(), number=100))

print('dict()',timeit('copy_create(big_d)', globals=globals(), number=100))

print('comprehension',timeit('copy_comprehension(big_d)', globals=globals(), number=100))

print('deepcopy',timeit('copy_deepcopy(big_d)', globals=globals(), number=100))

