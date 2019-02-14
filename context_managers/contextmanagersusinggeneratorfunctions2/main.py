from contextlib import contextmanager
from time import perf_counter, sleep

@contextmanager
def timer():
  stats = dict()
  start = perf_counter()
  stats['start'] = start
  try:
    yield stats
  finally:
    end = perf_counter()
    stats['end'] = end
    stats['elapsed'] = end - start

with timer() as stats:
  sleep(3)

# with timer() as stats:
#   sleep(2)

print(stats)
print('*********************')
import sys

@contextmanager
def out_to_file(fname):
  current_stdout = sys.stdout
  print('current_stdout', current_stdout)
  file = open(fname, 'w')
  sys.stdout = file
  try:
    yield None
  finally:
    file.close()
    sys.stdout = current_stdout
    print('current stdout in finally',current_stdout)
    print('sys.stdou56t', sys.stdout)

with out_to_file('test.txt'):
  print('line 1')
  print('line 2')

# print('hello')

# with open('test.txt', 'r') as f:
#   print(f.readlines())

# from contextlib import redirect_stdout

# with open ('test2.txt', 'w') as f:
#   with redirect_stdout(f):
#     print('Look on the bright side of life')

# with open('test2.txt', 'r') as f:
#   print(f.readlines())