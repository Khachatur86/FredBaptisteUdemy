class CyclicIterator:
  def __init__(self, lst, length):
    self.lst = lst
    self.i = 0
    self.length = length

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i >= self.length:
      raise StopIteration
    else:  
      result = self.lst[self.i % len(self.lst)]
      self.i += 1
      return result

iter_cycl = CyclicIterator("NSWE", 15)

for item in iter_cycl:
  print(item)

