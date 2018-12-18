# Применяя к функциям декоратор timed можем определить время наиболее тормозящих функций

def timed(fn: "function"):
  from time import perf_counter

  def inner(*args, **kwargs):
    start = perf_counter()
    result = fn(*args, **kwargs)
    end = perf_counter()
    elapsed = end - start
    print(f"Run time: {elapsed:.6f}")
    return result
  return inner

