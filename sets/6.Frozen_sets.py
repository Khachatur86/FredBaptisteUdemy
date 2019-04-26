s1 = {'a', 'b', 'c'}
print(type(s1))
s2 = frozenset('abc')
print(s2)
print(type(s2))
hash(s2)
# frozensets are hash objects

s2 = {frozenset({'a', 'b'}), frozenset({1, 2, 3})}
