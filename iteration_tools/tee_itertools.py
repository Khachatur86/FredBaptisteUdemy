from itertools import tee

def squares(n):
  for i in range(n):
    yield i**2

gen = squares(10)
iters = tee(gen, 3)

iter1, iter2, iter3 = iters

print(iter1 is iter2)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))


print("\n", "Iter2")
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))


print("\n", "Iter3")
print(next(iter3))
print(next(iter3))
print(next(iter3))
print(next(iter3))
print(next(iter3))
print(next(iter3))

l = [1, 2, 3, 4, 5]

lists = tee(l, 2)
print("Lists[0]")
print(next(lists[0]))
print(next(lists[0]))
print(next(lists[0]))
print("Lists[1]")
print(next(lists[1]))
print(next(lists[1]))
print(next(lists[1]))