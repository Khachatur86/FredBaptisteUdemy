import itertools 
# with open("cars_2014.csv") as f:
#   next(f)
#   for row in itertools.islice(f, 0, 25):
#     print(row, end="")


from collections import defaultdict
makes = defaultdict(int)
with open("cars_2014.csv") as f:
  next(f)
  for row in f:
    make, _ = row.strip("\n").split(',')
    makes[make] += 1

for key, value in makes.items():
  print(f'{key}:{value}')

data = [1, 2, 2, 2, 3]

print(list(itertools.groupby(data)))