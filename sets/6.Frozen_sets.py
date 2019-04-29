s1 = {'a', 'b', 'c'}
print(type(s1))
s2 = frozenset('abc')
print(s2)
print(type(s2))
hash(s2)
# frozensets are hash objects

s2 = {frozenset({'a', 'b'}), frozenset({1, 2, 3})}
# Sets are not hashable
# print(hash(s1))
t1 = (1, 2, [3, 4])
# print(hash(t1))
t2 = tuple(t1)
print(t1 is t2)
l1 = [1, 3]
l2 = list(l1)
l1.append('af')
print(l2)
s1 = {1, 2, 3}
s2 = set(s1)
print(id(s1), id(s2))
s1 = frozenset([1, 2, 3])
print(s1)
s2 = frozenset(s1)
print(id(s1), id(s2))
from copy import deepcopy

s2 = deepcopy(s1)
print(id(s1) , id(s2))
s1 = frozenset('ab')
s2 = {1, 2}
s3 = s1 | s2
print(s3)
s4 = s2 | s1
print(s4)

s1 = {1, 2, 3, 5}
s2 = frozenset(s1)
print(s1, s2)
print(s1 is s2)
print(s1 == s2)
# print(hash(1), hash(1.0))

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def __repr__(self):
    return f"Person(name={self._name}, age={self._age})"
  
  @property
  def name(self):
    return self._name
  
  @property
  def age(self):
    return self._age

  def key(self):
    return frozenset({self.name, self.age})

p1 = Person('John',78)
p2 = Person('Eric', 75)
d = {p1.key():p1, p2.key():p2}
print(d)
print(d[frozenset(['John', 78])])

from functools import lru_cache

@lru_cache()
def my_func(*, a, b):
  print('calculating a+b...')
  return a + b

print(my_func(a=1, b=2))
print(my_func(a=1, b=2))
print(my_func(a=2, b=1))
print(my_func(a=2, b=1))
print(my_func(a='a', b='b'))
print(my_func(a='a', b='b'))

def my_func2(*, a, b):
  print('calculating a+b...')
  return a + b

print(my_func2(a=[1, 2, 3], b=[3,4,5]))
# print(my_func(a=[1, 2, 3], b=[3,4,5]))

def memoizer(fn):
  cache = {}

  def inner(*args, **kwargs):
    key = (*args, frozenset(kwargs.items()))
    # if key in cache:
    #   return cache[key]
    # else:
    #   result = fn(*args, **kwargs)
    #   cache[key] = result
    #   return cache[key]
    if key not in cache:
      result = fn(*args, **kwargs)
      cache[key] = result
    return cache[key]
  return inner

@memoizer
def my_func(*, a, b):
  print('calculating a + b ...')
  return a + b
print('=====================')
print(my_func(a=1, b=2))
print(my_func(a=1, b=2))
print('======================')
print(my_func(a=2, b=1))


def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner
  
@memoizer
def adder(*args):
  print('calculating ....')
  return sum(args)

print(adder(1, 2, 3))
print(adder(1, 3, 2))