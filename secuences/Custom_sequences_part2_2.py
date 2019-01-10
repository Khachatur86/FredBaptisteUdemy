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
  

c1 = MyClass("Eric")
c2 = MyClass("Idle")

result = c1 + c2

print(f"id(c1) = {id(c1)}")
print(f"id(c2) = {id(c2)}")
print(f"id(result) = {id(result)}")
c1 += c2
print(f"After id(c1) = {id(c1)}")