def echo():
  while True:
    recieved = yield
    print('You said:', recieved)

e = echo()
from inspect import getgeneratorstate

print(getgeneratorstate(e))

next(e)
e.send('python')
print(getgeneratorstate(e))
e.send('hello')

def squares(n):
  for i in range(n):
    yield i**2

sq = squares(5)

print(next(sq))
print(sq.send('python'))
print(sq.send('python'))
# print(sq.send(None))

e = echo()
e.send(None)
a = e.send(99)
# e.send(1919)
# print(a)

def squares(n):
  for i in range(n):
    received = yield i**2
    print('Recieve value',received)

sq = squares(7)
next(sq)
next(sq)
next(sq)
print('After next')
sq.send('python')
sq.send('python')
next(sq)
# print(next(sq))
# print(next(sq))
# print('After next')
# print(sq.send('python'))
# print(sq.send('python'))
print('\n _____________________')
def echo(max_times):
  for _ in range(max_times):
    received = yield 
    print('You said:', received)
  print('that\'s all folks!')

e = echo(3)
e.__next__()
e.send('python')
e.send('is')
# e.send('awesome')

def averager():
  total = 0
  count = 0
  def inner(value):
    nonlocal total
    nonlocal count
    total += value
    print('value',value)
    print('total',total)
    count += 1
    print('count',count)
    return total / count
  return inner

def running_averages(iterable):
  avg = averager()
  for value in iterable:
    running_average = avg(value)
    print(running_average)

running_averages([1, 2, 3, 4])

def running_averager():
  total = 0
  count = 0
  running_average = None
  while True:
    value = yield running_average
    print('value', value)
    total += value
    print('total', total)
    count += 1
    print('count', count)
    running_average = total / count
    print('running_average total/count', running_average)

print('\n -------------')
run = running_averager()
next(run)
run.send(3)
run.send(4)
run.send(5)

print('\n -------------')
def running_averages(iterable):
  averager = running_averager()
  next(averager)
  for value in iterable:
    running_average = averager.send(value)
    print(running_average)

running_averages([1, 2, 3, 4, 5])