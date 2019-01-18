import math


class Circle:
  def __init__(self, r):
    self._radius = r
    self._area = None
    
  @property
  def radius(self):
    print("radius")
    return self._radius

  @radius.setter
  def radius(self, r):
    print("radius.seter", r)
    self._radius = r
    self._area = None
  
  @property
  def area(self):
    if self._area is None:
      print("Calculating area...")
      self._area = math.pi * (self.radius ** 2)
    return self._area


c = Circle(1)
print(c)
print(c.area)
c.radius = 2

print(c.radius)
print(c.area)


class Factorials:
  def __init__(self, length):
    self.length = length
  
  def __iter__(self):
    return self.FactIter(self.length)

  class FactIter:
    def __init__(self, length):
      self.length = length
      self.i = 0
    
    def __iter__(self):
      return self
    
    def __next__(self):
      if self.i >= self.length:
        raise StopIteration
      else:
        result = math.factorial(self.i)
        self.i += 1
        return result

facts = Factorials(5)

print(list(facts))

class Factorials:

  def __iter__(self):
    return self.FactIter()

  class FactIter:
    def __init__(self):
      self.i = 0
    
    def __iter__(self):
      return self
    
    def __next__(self):
      result = math.factorial(self.i)
      self.i += 1
      return result


facts = Factorials()
fact_iter = iter(facts)
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))