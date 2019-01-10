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
      # self._pts = [Point(*pt) for pt in pts]
      print(self._pts)
    else:
      self._pts = []

  def __repr__(self):
    pts_str = ", ".join([str(pt) for pt in self._pts])
    return f"Polygon({pts_str})"

p = Polygon((0, 0), Point(x=1,y=9))

print(p)