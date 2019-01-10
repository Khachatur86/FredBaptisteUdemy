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

  def __rmul__(self, n):
    # return MyClass(self.name * n)
    return self.__mul__(n)

  def __imul__(self, n):
    self.name *= n
    return self

  def __contains__(self, value):
    return value in self.name

c1 = MyClass("Eric")
print(c1)
print(3*c1)

c2 = MyClass("Eric Idle")
print("z" in c2)
print("i" in c2)

