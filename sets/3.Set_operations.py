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
# Является ли множество s1 подмножеством s2
# Analog
print("s1 <= s2",s1<=s2)
print('s1 < s2 - ', s1 < s2)
print('s3.issuperset(s1) - ',s3.issuperset(s1))
# Является ли множество s3 надмножеством s1
# Операторы | & принимают слева и справа от себя только set
# В случаях ниже операторы принимают на вход отличные от множества структуры данных, поэтому операции приведут к ошибкам
# {1, 2} & [3, 5]
# {1, 2} | [4, 6]
# Хотя: 
print({1, 4}.intersection([2, 4]))
print({1, 6}.union([1, 9]))
# but 
print({1, 3, 4}.intersection([(1, 4), (5, 6)]))

print(set([(1, 5), (5, 8)]))

a = 0b101010
b = 0b110100
print(f"a = {a}, b = {b}")
print('Binary (умножение) &')
c = a & b
print(bin(a))
print(bin(b))
print(bin(c))

print('Binary (сложение)|')
c = a | b
print(bin(a))
print(bin(b))
print(bin(c))