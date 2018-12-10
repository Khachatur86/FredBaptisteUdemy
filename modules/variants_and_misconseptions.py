import sys

# for k in sorted(sys.modules.keys()):
#   print(k)

# for g in sorted(globals()):
#   print(g)

print('cmath' in sys.modules)
print("cmath" in globals())


# print(globals())
# dict_1 = {"key1": 1, "key2": 2, "key3": 3}
# print(1 in dict_1.values())

from cmath import exp

print("cmath находится в globals()","cmath" in globals())
print("exp находится в globals()","exp" in globals())
print("cmath находится в sys.modules","cmath" in sys.modules)

print(exp(2+2j))
cmath = sys.modules["cmath"]
print("cmath" in globals())
print(cmath.sin(39))

from cmath import *
print(globals())

from math import *
print(globals()) # Значения ключей совпадающих наименований будут перезаписаны
# print(sqrt(2+2j)) # Выдаст ожидаемую ошибку, так как это уже sqrt другой функции

def my_func():
  from collections import namedtuple
  return 8
my_func()

print("collections" in sys.modules)