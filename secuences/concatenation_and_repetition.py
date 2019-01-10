l1 = [1, 2, 3, 4]
l2 = [5, 6]
# Before
print("\n")
print("id(l1) = ", id(l1), l1)
print("id(l2) = ", id(l2), l2)

# After

l1 = l1 + l2
print("\n")
print("id(l1) = ", id(l1), l1)

t1 = (1, 2, 3)

# l1 = l1 + t1 
# TypeError: can only concatenate list (not "tuple") to list

### In place concatenation

l1 = [1, 2, 3, 4]
l2 = [5, 6]

print("\n")
print("id(l1) = ", id(l1), l1)
print("id(l2) = ", id(l2), l2)

l1 += l2

print("\n")
print("id(l1) = ", id(l1), l1)

### Concatenation += with tuple
print("\nConcatenation += with tuple\n")
l1 = [1, 2, 3, 4]
t1 = (5, 7, 8)
print(f"Before concatenation with tuple: id(l1) = {id(l1)}, l1 = {l1}")
l1 += t1
print(l1)
print(f"After concatenation with tuple: id(l1) = {id(l1)}, l1 = {l1}")

### Concatenation += with set
print("\n Concatenation += with set \n")
l1 = [1, 2, 3, 4, 5]

s1 = {"a", "adf"}
print(f"Before concatenation with set: id(l1) = {id(l1)}, l1 = {l1}")
l1 += s1
print(f"After concatenation with set: id(l1) = {id(l1)}, l1 = {l1}")

# Concatenation += works with the only mutable sequences
print("\n Concatenation += works with the only mutable sequences \n")
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(f"Before id(t1) = {id(t1)}, t1 = {t1}")
print(f"Before id(t2) = {id(t2)}, t2 = {t2}")

t1 += t2

print(f"After id(t1) = {id(t1)}, t1 = {t1}")

#  Repetition *= 
print("\n","Repetition", "\n")
l1 = [1, 2, 3]
print(f"Before id(l1) = {id(l1)}, l1 = {l1}")

l1 = 2 * l1

print(f"After id(l1) = {id(l1)}, l1 = {l1}")

print("\n In place repetition with *= \n")

l1 = [1, 2, 3]

print(f"Before id(l1) = {id(l1)}, l1 = {l1}")

l1 *= 2

print(f"After id(l1) = {id(l1)}, l1 = {l1}")
