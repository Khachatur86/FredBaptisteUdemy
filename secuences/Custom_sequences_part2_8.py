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
      points = other._pts
    else:
      points = [Point(*pt) for pt in other]
    self._pts = self._pts + points
    return self

  def append(self, pt):
    self._pts.append(Point(*pt))
  
  def insert(self, i, pt):
    self._pts.insert(i, Point(*pt))

  def extend(self, pts):
    if isinstance(pts, Polygon):
      self._pts += pts._pts
    else:
      points = [Point(*pt) for pt in pts]
      self._pts += points 


p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (3,3))
print(f"Before! id(p1)={id(p1)}. p1={p1}\n")
print(f"Before! id(p2)={id(p2)}. p2={p2}\n")

p1.append([10, 10])
p1.insert(1, Point(-1, -1))
p1.extend(p2)
print(f"After! id(p1)={id(p1)}. p1={p1}\n")

for item in p1:
  print(item)
# p1 += [(2, 2), (3, 3), Point(4,4)]

# print(f"After changing id(p1)={id(p1)}. p1={p1} \n")