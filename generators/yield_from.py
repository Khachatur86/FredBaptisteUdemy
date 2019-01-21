def matrix(n):
  gen = ((i*j for j in range(1,n+1))
         for i in range(1, n+1))
  return gen

m = list(matrix(5))
print(list(matrix(5)))

# def matrix_iterator(n):
#   for row in matrix(n):
#     for item in row:
#       yield item
      
def matrix_iterator(n):
  for row in matrix(n):
    yield from row

for item in matrix_iterator(5):
  print(item)