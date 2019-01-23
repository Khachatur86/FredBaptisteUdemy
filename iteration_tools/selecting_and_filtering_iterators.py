def gen_cubes(n):
  for i in range(n):
    print(f'yielding {i}')
    yield i**3

def is_odd(x):
  print(f"is_odd x={x % 2}")
  return x % 2 == 1

# print(is_odd(4), is_odd(81))

filtered = filter(is_odd, gen_cubes(8))

# print(list(filtered))

def is_even(x):
  return x % 2 == 0
  
filtered = filter(is_even, gen_cubes(8))
# print(list(filtered))

from itertools import filterfalse

filtered = filterfalse(is_odd, gen_cubes(10))
# print("Filterralse")
# print(list(filtered))

# dropwhile and takewhile

from itertools import dropwhile, takewhile
from math import sin, pi

def sine_wave(n):
  start = 0
  max_ = 2 * pi
  step = (max_ - start) / (n-1)

  for _ in range(n):
    yield round(sin(start), 2)
    start += step
  
print(list(sine_wave(15)))

print(list(takewhile(lambda x: 0 <= x <= 0.9,sine_wave(15))))

l = [1, 3, 5, 2, 1]
result = dropwhile(lambda x: x < 5, l)
print(list(result))

### Compress
from itertools import compress
data = ['a', 'b', 'c', 'd', 'e', None]
selectors = [True, False, 1, 0, 2, None]
print(list(zip(data, selectors)))

print(list(compress(data, selectors)))