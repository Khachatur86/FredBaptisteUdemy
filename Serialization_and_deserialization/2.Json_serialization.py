import json

d1 = {'a': 100, 'b': 200}

d1_json = json.dumps(d1)
print(d1_json)

print(json.dumps(d1, indent=2))

d2 = json.loads(d1_json)
print(d2 == d1) # True
print(d2 is d1) # False

d1 = {1: 100, 2: 200}
d1_json = json.dumps(d1)
print(d1_json)

d2 = json.loads(d1_json)
# d1 = {'1': 100, '2': 200}

print(d2 == d1) # False
print(d2 is d1) # False

d_json = """
{
  "name": "John Cleese",
  "age": 82,
  "height": 1.96,
  "walksFunny": true,
  "sketches": [
    {
      "title": "Dead Parrot",
      "costars": ["Michael Palin"]
    },
    {
      "title": "Ministry of Silly Walks",
      "costars": ["Michael Palin", "Terry Jones"]
    }
  ],
  "boring": null
}
"""

d = json.loads(d_json)
from pprint import pprint
pprint(d)

d = {'a': (1, 2, 3)}
ser = json.dumps(d)
print(ser)
deser = json.loads(ser)
print(deser)

bad_json = """
  {"a": (1, 2, 3)}
"""

# json.loads(bad_json) # error

# from decimal import Decimal

# json.dumps({'a': Decimal('0.5')}) # TypeError


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'



p = Person('John', 82)
# json.dumps({"john": p}) TypeError: Object of type 'Person' is not JSON serializable


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return dict(name=self.name, age=self.age)

p = Person('John', 82)
print(json.dumps({"john": p.toJSON()}, indent=2))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return vars(self)
p1 = Person('John', 82)
print(json.dumps(dict(john=p1.toJSON())))
