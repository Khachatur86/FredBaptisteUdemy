import random

class RandomInts:
  def __init__(self, length, *, seed=0, lower=0, upper=10):
    self.length = length
    self.seed = seed
    self.lower = lower
    self.upper = upper

  def __len__(self):
    return self.length
  
  def __iter__(self):
    return self.RandomIterator(self.length, 
                               seed=self.seed, 
                               lower=self.lower, 
                               upper=self.upper)

  class RandomIterator:
    def __init__(self, length, *, seed, lower, upper):
      self.length = length
      self.seed = seed
      self.lower = lower
      self.upper = upper
      self.num_requests = 0
      random.seed(seed)
      
    def __iter__(self):
      return self

    def __next__(self):
      if self.num_requests >= self.length:
        raise StopIteration
      else:
        result = random.randint(self.lower, self.upper)
        self.num_requests += 1
        return result


randoms = RandomInts(10)
for num in randoms:
  print(num)