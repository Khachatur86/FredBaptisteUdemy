class Cities:
  def __init__(self):
    print(f"Cities __init__ called.id(self) = {id(self)}")
    self._cities = ["Paris", "Berlin", "Rome", "Madrid", "London"]
    # self._index = 0
  
  def __len__(self):
    return len(self._cities)
  
  def __iter__(self):
    print("Cities __iter__ called.")
    return CityIterator(self)

class CityIterator:
  def __init__(self, _city_obj):
    print(f"CityIterator __init__ called. id(self) = {id(self)} type(self)={type(self)}")
    self._city_obj = _city_obj
    self._index = 0
  
  def __iter__(self):
    print("CityIterator __iter__ called.")
    return self

  def __next__(self):
    print("CityIterator __next__ called.")
    if self._index >= len(self._city_obj):
      raise StopIteration
    else:
      item = self._city_obj._cities[self._index]
      self._index += 1
      return item

cities1 = Cities()
cities2 = Cities()
a = 65
for city in cities1:
  print(city)
a = 8
del a
for city in cities2:
  print(city)

a = 5445
b = 5445
print(f"id(a)={id(a)}, id(b)={id(b)}")
print(id(5445))
print(id(5445))
print(id(5445))