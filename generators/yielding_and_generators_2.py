import math
def fact():
  i = 0
  def inner():
    nonlocal i
    result = math.factorial(i)
    return result
  return inner

f = fact()
fact_iter = iter(f, math.factorial(5))

print(list(fact_iter))