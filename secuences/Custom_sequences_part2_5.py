from collections import namedtuple

Point = namedtuple("Point", "x y")
p1 = Point(10.5, 3.2)
print(p1)
p2 = Point("abc", [1, 2, 3])

print(p2)

x, y = p2
print(x)

import numbers
print("isinstance(10, numbers.Number) - ",isinstance(10, numbers.Number))

print("isinstance(10+2j, numbers.Number) - ",isinstance(10+2j, numbers.Number))
print("isinstance(afd , numbers.Number) - ",isinstance("afd" , numbers.Number))

class Point:
  def __init__(self, x, y):
    if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
      self._pt = (x, y)
    else:
      raise TypeError("Point co-ordinates must be real numbers.")

  def __repr__(self):
    return f"Point(x={self._pt[0]}, y={self._pt[1]})"

p1 = Point(10, 2.5)
print("p1 - ", p1)
p2 = Point("a", 10)