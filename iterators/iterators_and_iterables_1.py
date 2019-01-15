class Cities:
  def __init__(self):
    self._cities = ["Paris", "Berlin", "Rome", "Madrid", "London"]
    self._index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self._index >= len(self._cities):
      raise StopIteration
    else:
      item = self._cities[self._index]
      self._index += 1
      return item

# cities = Cities()
# print(type(cities))
# print(list(enumerate(cities)))
# print(next(cities))
# print(next(cities))
# print(next(cities))

class CityIterator:
  def __init__(self, _city_obj):
    self._city_obj = _city_obj
    self._index = 0
  
  def __iter__(self):
    return self

  def __next__(self):
    if self._index >= len(self._city_obj):
      raise StopIteration
    else:
      item = self._city_obj._cities[self._index]
      self._index += 1
      return item

cities = Cities()

for city in cities:
  print(city)