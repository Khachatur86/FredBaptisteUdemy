from contextlib import contextmanager
class NestedContexts:
    def __init__(self):
        self._exits = []
  
    def __enter__(self):
        return self
    
    def enter_context(self, ctx):
      self._exits.append(ctx.__exit__)
      value = ctx.__enter__()
      return value

    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False



@contextmanager
def open_file(f_name):
  print(f'opening {f_name}')
  f = open(f_name)
  try:
    yield f
  finally:
    print(f'closing {f_name}')
    f.close()

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
  files = [stack.enter_context(open_file(f_name)) for f_name in f_names]
  print('do work')

from contextlib import ExitStack

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
  files = [stack.enter_context(open_file(f_name)) for f_name in f_names]
  print('do work')