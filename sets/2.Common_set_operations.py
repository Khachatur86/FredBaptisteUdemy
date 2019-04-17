s = {1, 2, 3}

print(len(s))

print(1 in s)
print(4 in s)
from timeit import timeit
n = 100_000
s = {i for i in range(n)}
l = [i for i in range(n)]
d = {i: None for i in range(n)}
t = tuple(i for i in range(n))
number = 1_000_000
search = 5

t_list = timeit(f"{search} in l", globals=globals(), number=number)

t_set = timeit(f"{search} in s", globals=globals(), number=number)

t_dict = timeit(f"{search} in d", globals=globals(), number=number)

t_tuple = timeit(f"{search} in t", globals=globals(), number=number)

print('t_list - ',t_list)
print('t_set - ', t_set)
print('t_dict - ',t_dict)
print('t_tuple - ',t_tuple)

print('d.__sizeof__() - ', d.__sizeof__())
print('s.__sizeof__() - ', s.__sizeof__())
print('l.__sizeof__() - ', l.__sizeof__())
print('t.__sizeof__() - ', t.__sizeof__())

l = []
s = set()
d = {}
print('Before')
print('d.__sizeof__() - ', d.__sizeof__())
print('s.__sizeof__() - ', s.__sizeof__())
print('l.__sizeof__() - ', l.__sizeof__())

s.add(10)
d[10] = None
l.append(4)
print('After')
print('d.__sizeof__() - ', d.__sizeof__())
print('s.__sizeof__() - ', s.__sizeof__())
print('l.__sizeof__() - ', l.__sizeof__())

s = {30, 20, 12}
s.add(100)
print(s)
s.add(100)
print(s)
s.remove(100)
print(s)

s = {1, 2, 3}
s.remove(1+0j)
print(s)
# s.remove(100) # KeyError
s.discard(100)
print(s)
s.discard(2)
print(s)
s = set('python')
print(s.pop())
print(s)
s.clear()
print(s)