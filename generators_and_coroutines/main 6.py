def coroutine(gen_fn):
  def inner():
    gen = gen_fn()
    next(gen)
    return gen
  return inner

@coroutine
def echo():
  while True:
    received = yield
    print(received)

e = echo()
from inspect import getgeneratorstate

# print(getgeneratorstate(e))
# e.send('hello')

def coroutine(gen_fn):
  def inner(*args, **kwargs):
    gen = gen_fn(*args, **kwargs)
    next(gen)
    return gen
  return inner

import math
@coroutine
def power_up(p):
  result = None
  while True:
    received = yield result
    result = math.pow(received, p)

# squares = power_up(2)
# cubes = power_up(3)

# print(squares.send(2))
# print(cubes.send(3))
# squares.send('abs')

@coroutine
def power_up(p):
  result = None
  while True:
    received = yield result
    try:
      result = math.pow(received, p)
    except TypeError:
      result = None


# squares = power_up(2)

# print(squares.send(2))

# print(squares.send('adb'))

@coroutine
def power_up(p):
  result = None
  while True:
    received = yield result
    try:
      result = math.pow(received, p)
    except TypeError:
      result = None

squares = power_up(3)
print(squares.send(3))