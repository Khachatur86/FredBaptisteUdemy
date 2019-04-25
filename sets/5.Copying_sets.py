class Person:
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return f"Person(name={self.name})"

p1 = Person("John")
p2 = Person("Eric")
# Objects are hashable
print(f"hash(p1) - {hash(p1)}")
print(f"hash(p2) - {hash(p2)}")
s1= {p1, p2}
s2 = s1.copy()
# Are objects s1 and s2 reference same memory adress
print('s1 is s2 - ', s1 is s2)
print("s1 == s2 - ", s1 == s2)
# Objects are difference

# How to check that the elements of s1 and s2 are same

print('p1 in s1 - ',p1 in s1)
print('p1 in s2 - ',p1 in s2)

# Unpacking

s3 = {*s1}
print("s3 is s1 - ",s3 is s1)

print("s3 == s1 - ",s3 == s1)
print((s1, s2, s3))

p1.name = "John Cleese"

print((s1, s2, s3))
# Because hash of p1 object are not changed

s4 = set(s1) # Another way to get shallow copy

from copy import deepcopy

s5 = deepcopy(s1)
print("p1 in s5 - ",p1 in s5) # returned false
# because deepcopy return object that contains not same object as in shallow copy

print('s1 == s5 - ', s1 == s5) # also return false

print([(o, id(o)) for o in s1])
print([(o, id(o)) for o in s5])
