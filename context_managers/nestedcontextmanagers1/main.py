with open('file1.txt') as f:
  for row in f:
    print(row, end='')

print('\n----------------------')

with open('file2.txt') as f:
  for row in f:
    print(row, end='')

print('\n----------------------')

with open('file3.txt') as f:
  for row in f:
    print(row, end='')

with open('file1.txt') as f1, open('file2.txt') as f2:
  print(f1.readlines())
  print(f2.readlines())

with open('file1.txt') as f1:
  with open('file2.txt') as f2:
    with open('file3.txt') as f3:
      print(f1.readlines())
      print(f2.readlines())
      print(f3.readlines())


from contextlib import contextmanager

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

exits = []
enters = []

for f_name in f_names:
  ctx = open_file(f_name)
  enters.append(ctx.__enter__)
  exits.append(ctx.__exit__)

files = [enter() for enter in enters]
print(files)

while True:
  try:
    rows = [next(f).strip('\n') for f in files]
    # print(rows)
  except StopIteration:
    break
  else:
    row = ','.join(rows)
    print(row)

for exit in exits[::-1]:
  exit(None, None, None)

print('************** New theme **************')


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

# creating context manager
exits = []
enters = []

for f_name in f_names:
  ctx = open_file(f_name)
  enters.append(ctx.__enter__)
  exits.append(ctx.__exit__)

# 'entering' context manager
files = [enter() for enter in enters]

# do work
while True:
  try:
    rows = [next(f).strip('\n') for f in files]
    # print(rows)
  except StopIteration:
    break
  else:
    row = ','.join(rows)
    print(row)

# exit context managers
for exit in exits[::-1]:
  exit(None, None, None)


# class NestedContexts:
#   def __init__(self, *contexts):
#     self._enters = []
#     self._exits = []
#     self._values = []

#     for ctx in contexts:
#       self._enters.append(ctx.__enter__)
#       self._exits.append(ctx.__exit__)

#     def __enter__(self):
#       for enter in self._enters:
#         self._values.append(enter())
#       return self._values

#     def __exit__(self, exc_type, exc_value, exc_tb):
#       for exit in self._exits[::-1]:
#         exit(exc_type, exc_value, exc_tb)
#       return False

class NestedContexts:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []
        
        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)
        
    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False
        
with NestedContexts(open_file('file1.txt'),
                   open_file('file2.txt'),
                   open_file('file3.txt')) as files:
    print('do work here')
    while True:
      try:
        rows = [next(f).strip('\n') for f in files]
      except StopIteration:
        break
      else:
        row = ','.join(rows)
        print(row)

print('Third example')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

contexts = [open_file(f_name) for f_name in f_names]

with NestedContexts(*contexts) as files:
  print('do work')


