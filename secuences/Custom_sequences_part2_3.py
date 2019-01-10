class MyClass:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"MyClass(name={self.name})"

  def __add__(self, other):
    return MyClass(self.name + other.name)
    # if isinstance(other, MyClass):
    #   return MyClass(self.name + other.name)
    # else:
    #   raise TypeError

  def __iadd__(self, other):
    if isinstance(other, MyClass):
      self.name += other.name
    else:
      self.name += other
    return self
  
  def __mul__(self, n):
    return MyClass(self.name * n)

  def __imul__(self, n):
    self.name *= n
    return self

c1 = MyClass("Eric")
print(f"Before id(c1) is {id(c1)}. c1 = {c1}")

result = c1 * 3
print(f"id(result) is {id(result)}. resutl = {result}")

c1 *= 3
print(f"After id(c1) is {id(c1)}. c1 = {c1}")
