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

class Polygon:
  def __init__(self, *pts):
    if pts:
      self._pts = [Point(*pt) for pt in pts]
      # print(self._pts)
    else:
      self._pts = []

  def __repr__(self):
    pts_str = ", ".join([str(pt) for pt in self._pts])
    return f"Polygon({pts_str})"
  
  def __len__(self):
    return len(self._pts)

  def __getitem__(self, s):
    return self._pts[s]

  def __add__(self, other):
    if isinstance(other, Polygon):
      new_pts = self._pts + other._pts
      return Polygon(*new_pts)
    else:
      raise TypeError("Can only concatenate with another Polygon")
  
  def __iadd__(self, other):
    if isinstance(other, Polygon):
      self._pts = self._pts + other._pts
      return self
    else:
      raise TypeError("Can only concatenate with another Polygon")

    
p = Polygon((0, 0), Point(x=1,y=9))

print(p)

p1 = Polygon(Point(x=0, y=0), Point(x=1, y=1), Point(x=2, y=2))
print(p1)

print(f"p1[0]={p1[0]}")
print(f"p1[0:2]={p1[0:2]}")

p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2,2), (3, 3))
print(f"\n Before id(p1) is {id(p1)}. p1={p1}\n")
print(f"Before id(p2) is {id(p2)}. p2={p2}\n")
result = p1 + p2
print(f"Before id(result) is {id(result)}. result={result}\n")

print(f"\n Before id(p1) is {id(p1)}. p1={p1}\n")
p1 += p2

print(f"After id(p1) is {id(p1)}. p1={p1}\n")
