s = {"x", "y", "b", "c", "a"}

for item in s:
  print(item)

class Squares:
  def __init__(self):
    self.i = 0
  
  def next_(self):
    result = self.i ** 2
    self.i += 1
    return result

sq = Squares()


print(sq.next_())
print(sq.next_())
print(sq.next_())