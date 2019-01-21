# def squares_gen(n):
#   for i in range(n):
#     yield i ** 2
  
# class Squares:
#   def __init__(self, n):
#     self.n = n
  
#   def __iter__(self):
#     return squares_gen(self.n)


# for num in sq:
#   print(num)

# print(list(sq))

class Squares:
  def __init__(self, n):
    self.n = n
  
  def __iter__(self):
    return Squares.squares_gen(self.n)
  
  @staticmethod
  def squares_gen(n):
    for i in range(n):
      yield i ** 2

sq = Squares(5)

print(list(sq))