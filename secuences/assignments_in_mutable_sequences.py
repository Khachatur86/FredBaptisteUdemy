print("Assignments in mutable sequences \n")
l = [1, 2, 3, 4, 5]
print(f"id(l) = {id(l)}")

print(l[0:3])
l[0:3] = "python"
print(f"After changing id(l) = {id(l)}, l = {l}")

print("Assigning slice empty []")
l = [1, 2, 3, 4, 5, 6]
print(f"Before assigning l[2:4] = []. id(l) = {id(l)} l = {l}")
print(f"l[2:4] = {l[2:4]}")
l[2:4] = [] # We can use instead of [] - ""

print(f"After assigning l[2:4] = []. id(l) = {id(l)} l = {l}")
print(l)

# Memory address has not changed

l = [1, 2, 3, 4, 5]
print(f"Before changing id(l) = {id(l)} l= {l}")

s = slice(2,2)
print("l[s] = ", l[s])

l[s] = ("a", 100, 500)

print(f"After changing id(l) = {id(l)} l= {l}")

# It does not work with tuples

# With set
print("\nWorking with set\n")
l = [1, 2, 3, 4, 5]
print(f"Before changing id(l) = {id(l)} l= {l}")

s = slice(2,2)
print("l[s] = ", l[s])

l[s] = {"a", 100, 500}

print(f"After changing id(l) = {id(l)} l= {l}")

print("\nExtended slices\n")
l = [1, 2, 3, 4, 5]
print(f"Before changing id(l) = {id(l)} l= {l}")
l[0:5:2] = "jlk" # or [2, 5,8] or {3, 6, 9}
print(f"After changing id(l) = {id(l)} l= {l}")