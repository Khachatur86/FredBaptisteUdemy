def logged(fn):
  from functools import wraps
  from datetime import datetime, timezone

  @wraps(fn)
  def inner(*args, **kwargs):
    run_dt = datetime.now(timezone.utc)
    result = fn(*args, **kwargs)
    print(f"{run_dt}: called {fn.__name__}")
    return result
  return inner

@logged
def func_1():
  pass

@logged
def func_2():
  pass

def timed(fn):

  """
  Определяет сколько времени длятся вычисления
  """
  from time import perf_counter
  from functools import wraps

  @wraps(fn)
  def inner(*args, **kwargs):
    start = perf_counter()
    result = fn(*args, **kwargs)
    end = perf_counter()
    print(f"{fn.__name__} ran for {end - start :.6f} s")
    return result 
  return inner

@timed
@logged
def fact(n):
  from operator import mul
  from functools import reduce
  return reduce(mul, range(1, n+1))


print(fact(8))

# print(func_1())
# print(func_2())