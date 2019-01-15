class Cities:
  def __init__(self):
    print(f"Cities __init__ called.id(self) = {id(self)}")
    self._cities = ["Paris", "Berlin", "Rome", "Madrid", "London"]
    # self._index = 0
  
  def __len__(self):
    return len(self._cities)
  
  def __iter__(self):
    print("Cities __iter__ called.")
    return self.CityIterator(self)
  
  def __getitem__(self, s):
    print("getting item...")
    return self._cities[s]
    
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

cities = Cities()

for city in cities:
  print(city)

print(list(enumerate(cities)))

print(sorted(cities, key=lambda x: len(x)))

city_iterator = cities.__iter__()

for city in city_iterator:
  print(city)

for city in city_iterator:
  print(city)

print(cities[7])