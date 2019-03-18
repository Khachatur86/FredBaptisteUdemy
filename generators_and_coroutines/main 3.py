def gen(s):
  for c in s:
    yield c

g = gen('abc')
# print(next(g))
# print(next(g))
# print(next(g))

from inspect import getgeneratorstate

print(getgeneratorstate(g))
next(g)
print(getgeneratorstate(g))

def gen(s):
  for c in s:
    print(getgeneratorstate(global_gen))
    yield c
global_gen = gen('abc')

next(global_gen)

def gen(s):
  for c in s:
    yield c
    print('.....')

g = gen('abc')
print(next(g))
print(next(g))
print(next(g))
