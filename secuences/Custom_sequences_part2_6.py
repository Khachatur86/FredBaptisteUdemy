import numbers
class Point:
  def __init__(self, x, y):
    if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
      self._pt = (x, y)
    else:
      raise TypeError("Point co-ordinates must be real numbers.")

  def __repr__(self):
    return f"Point(x={self._pt[0]}, y={self._pt[1]})"

  def __len__(self):
    return len(self._pt)
  
  def __getitem__(self, s):
    return self._pt[s]
  

p1 = Point(10, 2)
x, y = p1
print(f"p1={p1}")
print(f"x={x}")
print(f"y={y}")
p2 = Point(*p1)
print(f"p2 = {p2}")
#p1 and p2 are different objects
print(f"id(p1)={hex(id(p1))}, id(p2)={hex(id(p2))}")

class Polygon:
  def __init__(self, *pts):
    if pts:
      self._pts = [Point(*pt) for pt in pts]
    else:
      self._pts = []

  def __repr__(self):
    return f"Polygon({self._pts})"

p = Polygon((0, 0), Point(x=1,y=9))

print(p)