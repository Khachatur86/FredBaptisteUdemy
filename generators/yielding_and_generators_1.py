import math
class FactIter:
  def __init__(self, n):
    self.n = n
    self.i = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i > self.n:
      raise StopIteration
    else:
      result = math.factorial(self.i)
      self.i += 1
      return result


fact_iter = FactIter(5)

print(list(fact_iter))
print(list(fact_iter))
# print(next(fact_iter))

def fact():
  i = 0
  def inner():
    nonlocal i
    result = math.factorial(i)
    i = i + 1
    return result
  return inner

f = fact()
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())