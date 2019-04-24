s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1, id(s1))
print(s2, id(s2))
s1 = s1 & s2

print(s1, id(s1))
print(id(globals()['s1']))
s1 = {1, 2, 3}
s2 = {2, 3, 4}


# |=, &=, - is update operations
# that operations doesn't change id of sets

print('id(s1) - ', id(s1))
s1 |= s2
print('id(s1) - ', id(s1))

# |= is equivalent .update()

# &= is equivalent .intersection_update
print('=='*18)
s1 = {1, 2, 3, 4}
s2 = {2, 3}
print('id(s1) - ', id(s1))
s1 -= s2
print("s1 - ", s1, 'id(s1) - ', id(s1))

# -= is equivalent .difference_update()

# s1 -= s2 - s3 сначала вычисляется правая часть, а после из множества s1 вычитается результат правой части
# s1.difference_update(s2, s3) - из множества s1 последовательно вычитаются s2 и s3 по очереди

# ^= - symmetric difference

def combine(string, target):
  target.update(string.split(' '))

def cleanup(combined):
  words = {'the', 'and', 'a', 'or', 'is', 'of'}
  combined -= words

result = set()
combine('lumberjacks sleep all night', result)
combine('the mistry of silly walks', result)
combine('this parrot is a late parrot', result)

print(result)
cleanup(result)
print(result)

def gen_read_data():
    yield ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']
    yield ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']
    yield ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']
  

data = gen_read_data()

print(next(data))
print(next(data))
print(next(data))
# print(next(data)) StopIteration

def filter_incoming(*cities, data_set):
    data_set.difference_update(cities)



result = set()
data = gen_read_data()
for page in data:
    result.update(page)
    filter_incoming('Paris', 'London', data_set=result)
    
print(result)