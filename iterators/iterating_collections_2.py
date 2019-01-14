class Squares:
  def __init__(self, length):
    self.i = 0
    self.length = length
  
  def next_(self):
    if self.i >= self.length:
      raise StopIteration
    else:
      result = self.i ** 2
      self.i += 1
      return result
  
  def __len__(self):
    return self.length

sq = Squares(3)

print(sq.next_())
print(sq.next_())
print(sq.next_())
# print(sq.next_())

sq = Squares(10)
while True:
  try:
    print(sq.next_())
  except StopIteration:
    break