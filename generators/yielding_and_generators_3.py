import math
def my_func():
  print('line_1')
  yield print('Flying')
  print('line2')
  yield print('Circus')

# print(type(my_func))

f = my_func()
# print(f)
# print("__iter__" in dir(f))
# print("__next__" in dir(f))
# print(iter(f) is f)

f.__next__()
f.__next__()
def silly():
  yield "the"
  yield 'ministry'
  yield 'of'
  return None
  yield 'silly'
gen = silly()
for el in gen:
  print(el)

# print(next(gen))

def fact(n):
  for i in range(n):
    yield math.factorial(i)
gen = fact(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
