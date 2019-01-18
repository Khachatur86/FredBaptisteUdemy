class CyclicIterator:
  def __init__(self, lst):
    self.lst = lst
    self.i = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    result = self.lst[self.i % len(self.lst)]
    self.i += 1
    return result

iter_cycl = CyclicIterator("NSWE")

for _ in range(5):
  print(next(iter_cycl))