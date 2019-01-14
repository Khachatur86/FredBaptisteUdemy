import math

class Polygon:
  def __init__(self, n, R):
    if n < 3:
      raise ValueError("Polygon mast have at least three sides.")
    self._n = n
    self._R = R
  
  def __repr__(self):
    return f"Polygon(n={self._n}, R={self._R})"
  
  @property
  def count_vertices(self):
    return self._n

  @property
  def count_edges(self):
    return self._n

  @property
  def circumradius(self):
    return self._R

  @property
  def interior_angle(self):
    return (self._n - 2) * 180 / self._n 

  @property 
  def side_length(self):
    return 2 * self._R * math.sin(math.pi / self._n)

  @property
  def apothem(self):
    return self._R * math.cos(math.pi / self._n)

  @property
  def area(self):
    return self._n / 2 * self.side_length * self.apothem

  @property
  def perimeter(self):
    return self._n * self.side_length
  
  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.count_edges == other.count_edges
               and self.circumradius == other.circumradius)
    else:
      return NotImplemented

  def __gt__(self, other):
    if isinstance(other, Polygon):
      return self.count_vertices > other.count_vertices
    else:
      return NotImplemented



def test_polygon():

  try:
    p = Polygon(2, 10)
    assert False, ("Creating a Polygon with 2 sides: "
                   "Exception expected but not received")
  except ValueError:
    pass
  rel_tol = 0.001
  abs_tol = 0.001

  n = 3
  R = 1
  p = Polygon(n, R)
  assert str(p) == f'Polygon(n=3, R=1)',f'actual:{str(p)}'
  assert p.count_vertices == n, (f"actual: {p.count_vertices}",
                                 f"expected: {n}")
  assert p.count_edges == n
  assert p.circumradius == R
  assert p.interior_angle == 60

  n = 4
  R = 1
  p = Polygon(n, R)
  assert math.isclose(p.interior_angle, 90)

  assert math.isclose(p.area, 2.0,
                      rel_tol=rel_tol,
                      abs_tol=abs_tol), (f"actual: {p.area}",
                                            f"expected: {2.0}")
  assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.apothem, 0.707,
                      rel_tol=rel_tol, 
                      abs_tol=abs_tol)
  
  n = 6
  R = 2
  p = Polygon(n, R)
  assert math.isclose(p.interior_angle, 120)

  assert math.isclose(p.area, 10.3923,
                      rel_tol=rel_tol,
                      abs_tol=abs_tol), (f"actual: {p.area}",
                                            f"expected: {2.0}")
  assert math.isclose(p.side_length, 2,
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.perimeter, 12,
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.apothem, 1.73205,
                      rel_tol=rel_tol, 
                      abs_tol=abs_tol)

  n = 12
  R = 3
  p = Polygon(n, R)
  assert math.isclose(p.interior_angle, 150)

  assert math.isclose(p.area, 27,
                      rel_tol=rel_tol,
                      abs_tol=abs_tol), (f"actual: {p.area}",
                                            f"expected: {2.0}")
  assert math.isclose(p.side_length, 1.55291,
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.perimeter, 18.635,
                       rel_tol=rel_tol, 
                       abs_tol=abs_tol)

  assert math.isclose(p.apothem, 2.89778,
                      rel_tol=rel_tol, 
                      abs_tol=abs_tol)

  p1 = Polygon(3, 10)
  p2 = Polygon(10, 10)
  p3 = Polygon(15, 10)
  p4 = Polygon(15, 100)
  p5 = Polygon(15, 100)

  assert p2 > p1
  assert p2 < p3
  assert p3 != p4
  assert p1 != p4
  assert p4 == p5

test_polygon()



class Polygons:
  def __init__(self, m, R):
    if m < 3:
      raise VelueError("m must be greater than 3")
    self._m = m
    self._R = R
    self._polygons = [Polygon(i, R) for i in range(3, m+1)]
  
  def __len__(self):
    return self._m - 2

  def __repr__(self):
    return f"Polygons(m={self._m}, R={self._R})"

  def __getitem__(self, s):
    return self._polygons[s]
  
  @property
  def max_efficiency_polygon(self):
    sorted_polygons = sorted(self._polygons,
                             key=lambda p: p.area / p.perimeter,
                             reverse=True)
    return sorted_polygons[0]


p = Polygons(8, 1)
# for el in p:
#   print(el)

for el in p[2:4]:
  print(el)
polygons = Polygons(10, 1)
print(polygons.max_efficiency_polygon)

print([(p.area / p.perimeter) for p in polygons])