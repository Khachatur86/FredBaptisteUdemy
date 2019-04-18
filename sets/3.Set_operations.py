s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))
# Analog
print(s1 & s2)
print(s1, s2)

s3 = {3, 4, 5}
print(s1.intersection(s2, s3))
print(s1 & s2 & s3)

s3 = {10, 20}
print(s1.union(s2))
print(s1 | s2)
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(len(s1 & s2))
print(len(s1 & s3))

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)

s1 = {1, 2, 3}
s2 = {3, 4}
s3 = {3, 4}
print(s1 - (s2-s3))
print(s1 - s2 -s3)
print(s1.difference(s2, s3))
print(s1.difference(s2, s3) == s1 - s2 - s3)

# s1.difference(s2, s3) is equivalent s1 - s2 - s3

# Symmetric difference

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("s1 ^ s2 - ",s1 ^ s2)
# or
print("(s1 | s2) - (s1 & s2) - ",(s1 | s2) - (s1 & s2))
print("s1.union(s2) - s1.intersection(s2) - ",s1.union(s2) - s1.intersection(s2))
print("s1.symmetric_difference(s2) - ",s1.symmetric_difference(s2))

# Symmetric difference is commutative

s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {10, 20, 30}
print("s1.issubset(s2) - ",s1.issubset(s2))
# Analog
print("s1<=s2",s1<=s2)