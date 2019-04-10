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

p1 = Person('John', 78)
p2 = Person('John', 78)

print(f"hash(p1)={hash(p1)}, hash(p2)={hash(p1)}")
print("p1 is p2 -", p1 is p2)
print("p1 == p2 -", p1 == p2)