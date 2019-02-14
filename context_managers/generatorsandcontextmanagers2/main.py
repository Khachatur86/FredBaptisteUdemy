def my_gen():
  try:
    print('creating context and yielding object')
    yield [1, 2, 3, 4]
  finally:
    print('exiting context and cleaning up')

class GenCtxManager:
  def __init__(self, gen_func, *args, **kwargs):
    self._gen = gen_func(*args, **kwargs)

  def __enter__(self):
    return next(self._gen)
  
  def __exit__(self, exc_type, exc_value, exc_tb):
    try:
      next(self._gen)
    except StopIteration:
      pass
    return False

def open_file(fname, mode):
  f = open(fname, mode)
  try:
    print('opening file...')
    yield f
  finally:
    print('closing file...')
    f.close()

with GenCtxManager(open_file, 'test.txt', 'w') as f:
  f.writelines('testing...')

with GenCtxManager(open_file, 'test.txt', 'r') as f:
  print(f.readlines())