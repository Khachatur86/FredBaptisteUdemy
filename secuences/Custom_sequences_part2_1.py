class MyClass:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"MyClass(name={self.name})"

  def __add__(self, other):
    print(f"You called + on {self} and {other}")
    return "Hello from __add__"

  def __iadd__(self, other):
    print(f"You called += on {self} and {other}")
    return "Hello from __iadd__"

c1 = MyClass("instance 1")
c2 = MyClass("instance 2")

result = c1 + c2
print(result)

print(f"Before id(c1) = {id(c1)} c1 = {c1}")

c1 += c2

print(f"After id(c1) = {id(c1)} c1 = {c1}")
