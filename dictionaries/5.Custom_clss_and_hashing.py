from pprint import pprint
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))

print(t1 is t2)
print(t1 == t2)

print(hash(t1), hash(t2))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"


p1 = Person('John', 78)
p2 = Person('John', 78)

print(f"hash(p1)={hash(p1)}, hash(p2)={hash(p1)}")
print("p1 is p2 -",p1 is p2)
print("p1 == p2 -",p1 == p2)

p1 = Person('John', 78)
p2 = Person('Eric', 75)

persons = {p1: 'John object', p2: 'Eric object'}

for k in persons.keys():
  print(k)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"

  def __eq__(self, other):
    if isinstance(other, Person):
      return self.name == other.name and self.age == other.age
    else:
      return False

p1 = Person('John', 78)
p2 = Person('John', 78)

# print(f"hash(p1)={hash(p1)}, hash(p2)={hash(p1)}")
print("p1 is p2 -", p1 is p2)
print("p1 == p2 -", p1 == p2)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"

  def __eq__(self, other):
    if isinstance(other, Person):
      return self.name == other.name and self.age == other.age
    else:
      return False
  
  def __hash__(self):
    return 100

p1 = Person('John', 78)
print(hash(p1))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"

  __hash__ = None


p1 = Person('John', 78)
# print(hash(p1)) 
# Traceback (most recent call last):
#   File "main.py", line 89, in <module>
#     print(hash(p1))
# TypeError: unhashabletype: 'Person'


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"

  def __eq__(self, other):
    if isinstance(other, Person):
      return self.name == other.name and self.age == other.age
    else:
      return False
  
  def __hash__(self):
    return hash((self.name, self.age))

p1 = Person('John', 78)
print(hash(p1))

p1 = Person('John', 78)
p2 = Person('Eric', 75)

persons = {p1: 'John object', p2: 'Eric object'}

print(persons[p1])
print(persons[Person('John', 78)])

print(p1 == Person('John', 78))

# __hash__ method must return an integer

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"

  def __eq__(self, other):
    if isinstance(other, Person):
      return self.name == other.name and self.age == other.age
    else:
      return False
  
  def __hash__(self):
    return 100

p1 = Person('John', 78)
p2 = Person('Eric', 75)

print("hash(p1) == hash(p2)", hash(p1) == hash(p2))
print("p1 == p2", p1 == p2)

persons = {p1: 'John object', p2: 'Eric object'}

pprint(persons)

class Number:
  def __init__(self, x):
    self.x = x

  def __eq__(self, other):
    if isinstance(other, Number):
      return self.x == other.x
    else:
      return False
    
  def __hash__(self):
    return hash(self.x)

class SameHash:
  def __init__(self, x):
    self.x = x
  
  def __eq__(self, other):
    if isinstance(other, SameHash):
      return self.x == other.x
    else:
      return False
    
  def __hash__(self):
    return 100


numbers = {Number(i): 'some value' for i in range(1000)}
same_hashes = {SameHash(i):'some value' for i in range(1000)}
# pprint(numbers)
# pprint(same_hashes)

from timeit import timeit

# print(timeit('numbers[Number(500)]', globals=globals(), number=10_000))
# print(timeit('same_hashes[SameHash(500)]', globals=globals(), number=10_000))

# def func_fstring():
#   for i in range(1000):
#     return f'{i}'

# def func_format():
#   for i in range(1000):
#     return '{}'.format(i)

# def func_format_str():
#   for i in range(1000):
#     return '%s'%i

# print('f_string', timeit('func_fstring()', globals=globals(), number=1000_000))
# print('format string', timeit('func_format()', globals=globals(), number=1000_000))
# print('% string', timeit('func_format_str()', globals=globals(), number=1000_000))

# f_string 8.85786579100386
# format string 13.635723553001299
# % string 11.310770388998208

# f_string 0.8536354699972435
# format string 1.153309276996879
# % string 0.9392164340024465

# f_string 0.9130312889974448
# format string 1.260975215001963
# % string 1.0864754959984566

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"
  
pt = Point(1, 2)
print(pt)

points = {
  Point(0, 0): 'origin',
  Point(1, 1): 'second pt'
}

pprint(points)

# print(points[Point(0, 0)]) # KeyError

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False
    
  def __hash__(self):
    return hash((self.x, self.y))

points = {
  Point(0, 0): 'origin',
  Point(1, 1): 'second pt'
}

pprint(points)

print(points[Point(0, 0)]) # KeyError does not happen.

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def __eq__(self, other):
    if isinstance(other, tuple) and len(other) == 2:
      other = Point(*other)
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False
    
  def __hash__(self):
    return hash((self.x, self.y))

points = {
  Point(0, 0): 'origin',
  Point(1, 1): 'second pt'
}

print(points[(0, 0)])
pt1 = Point(0, 0)
pt2 = Point(1, 1)
points = {
  pt1: 'origin',
  pt2: 'pt at (1,1)',
  (10,0) : 'Khachatur'
}

print(points[pt1], points[Point(0, 0)], points[(0, 0)])
print('Before key of pt1', hash(tuple(points.keys())[0]))
print('Before', hash(pt1))
pt1.x = 10
print('After ', hash(pt1))
print('After key of pt1', hash(tuple(points.keys())[0]))

print(points[pt1])

class Person:
  def __init__(self, id, name, age):
    self._id = id
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(id={self._id}, name={self.name}, age={self.age})"

  def __eq__(self, other):
    if isinstance(other, Person):
      return self._id == other._id
    else:
      return False
  
  def __hash__(self):
    return hash(self._id)

p1 = Person('john', 'John', 78)

persons = {
  p1: 'john object'
}

print(persons[p1])
print(persons[Person('john', 'John', 78)])

p1.name = 'Eric'
p1.age = 75
print(p1)
print(persons[p1])
