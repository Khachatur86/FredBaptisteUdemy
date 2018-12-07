data_dict = dict(key1=100, key2=200, key3=300)

print(data_dict)


from collections import namedtuple

print(data_dict.keys())

Data = namedtuple('Data', data_dict.keys())

print(Data._fields)
print(data_dict.values())
d1 = Data(*data_dict.values())
print(d1)


data_dict_2 = dict(key1=100, key3=300, key2=200)
d2 = Data(*data_dict_2.values())
print(d2)

d2 = Data(**data_dict_2)
print(d2)

key_name = "key2"
print("Доступ по ключу", data_dict[key_name]) # Доступ по ключу
print("То же самое для namedtuple", getattr(d2, key_name)) # То же самое для namedtuple

print(data_dict.get("key1", None))
print(getattr(d2, "key10", None))

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

# Получим контейнер ключей

keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
print(keys)

# Или используя set comprehension
keys = {key for dict_ in data_list for key in dict_.keys()}

print(keys)

Struct = namedtuple("struct", sorted(keys))

print(Struct._fields)

# Попробуем дефолтные значения

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
print(Struct(key2 = 10))

# Список структур namedtuple формирование
tuple_list = []
for dict_ in data_list:
  tuple_list.append(Struct(**dict_))
print(tuple_list)
# То же самое, только с использование list comprehension
tuple_list = [Struct(**dict_) for dict_ in data_list]

# Все то же самое, записанное в функцию
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

print(tuplify_dicts(data_list))