def my_gen():
  try:
    print('creating context and yielding object')
    yield [1, 2, 3, 4]
  finally:
    print('exiting context and cleaning up')

# gen = my_gen()
# lst = next(gen)
# print(lst)
# # next(gen) # StopIteration exception
# gen = my_gen()
# lst = next(gen)
# print(lst)
# try:
#   next(gen)
# except StopIteration:
#   pass

class GenCtxManager:
  def __init__(self, gen_func):
    self._gen = gen_func()

  def __enter__(self):
    return next(self._gen)

  def __exit__(self, exc_type, exc_value, exc_tb):
    try:
      next(self._gen)
    except StopIteration:
      pass
    return False

with GenCtxManager(my_gen) as obj:
  print(obj)


