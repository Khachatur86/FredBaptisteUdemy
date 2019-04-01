from pprint import pprint

a = {'k1': 100, 'k2': 200} # literally
print(type(a))

print('hash', hash((1, 2, 2)))
# print('hash', hash([1, 3]))

def my_func(a, b, c):
  print(a, b, c)

hash(my_func)

d = {my_func: [10, 20, 30]}
print(d)

def fn_add(a, b):
  return a + b

def fn_inv(a):
  return 1 / a

def fn_mult(a, b):
  return a * b

funcs = {
  fn_add: (10, 20),
  fn_inv: (2, ),
  fn_mult: (20, 40)
}

# print(funcs)
for f in funcs:
  print(f)

for f in funcs:
  result = f(*funcs[f])
  print(f.__name__, "result is", result)

for f, values in funcs.items():
  print(f(*values))

d = dict(x=100, a=200)

print(d)

d = dict([['a', 34], {'g', 12}, (5, 10)])
print(d)

d = {'a': 100, 'b': 200}
print(id(d))
d1 = dict(d)
print(id(d1))

d = {'a': 100, 'b': {'x': 1, 'y': 2}, 'c': [1, 2, 3]}

d1 = dict(d)

print(id(d))
print(id(d1))

print(d['b'] is d1['b'])
d1['b'] = 1212

print(d)
print(d1)

d = {'a': 100, 'b': {'x': 1, 'y': 2}, 'c': [1, 2, 3]}

d1 = dict(d)

d1['b']['z'] = 122
print(d1)
print(d)

keys = ['a', 'b', 'c']
values = (1, 2, 3)
d={}

for k, v in zip(keys, values):
  d[k]=v

print(d)

keys = 'abcd'
values = range(1, 5)

d = {k:v for k, v in zip(keys, values) if v % 2 ==0}
print(d)

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [ (x, y)
         for x in x_coords
         for y in y_coords
]

pprint(grid)


import math

print(math.hypot(1, 1))

grid_extended = [(x, y, math.hypot(x, y))
                  for x, y in grid]

pprint(grid_extended)

grid_extended = {(x, y): math.hypot(x, y)
                  for x, y in grid}

pprint(grid_extended)

counters = dict.fromkeys(['a', 'b', 'd'], 0)

pprint(counters)