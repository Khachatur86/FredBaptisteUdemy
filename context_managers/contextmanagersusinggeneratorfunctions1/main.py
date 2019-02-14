def open_file(fname, mode='r'):
  print('opening file...')
  f = open(fname, mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()

class GenContextManager:
  def __init__(self, gen):
    self.gen = gen
  
  def __enter__(self):
    print('calling next to get the yielded value from generator')
    return next(self.gen)

  def __exit__(self, exc_type, exc_value, exc_tb):
    print('calling next to perform cleanup in generator')
    try:
      next(self.gen)
    except StopIteration:
      pass
    return False

# file_gen = open_file('test.txt', 'w')
# with GenContextManager(file_gen) as f:
#   f.writelines('Sir Spamolot')

# Output
# calling next to get the yielded value from generator
# opening file...
# calling next to perform cleanup in generator
# closing file...

def context_manager_dec(gen_fn):
  def helper(*args, **kwargs):
    gen = gen_fn(*args, **kwargs)
    ctx = GenContextManager(gen)
    return ctx
  return helper

@context_manager_dec
def open_file(fname, mode='r'):
  print('opening file...')
  f = open(fname, mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()

with open_file('test.txt') as f:
  print(f.readlines())

from contextlib import contextmanager

@contextmanager
def open_file(fname, mode='r'):
  print('opening file...')
  f = open(fname, mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()

with open_file('test.txt', 'r') as f:
  print(f.readlines())
