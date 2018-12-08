# Начало новой темы модули
def func():
    a = 10
    return a


print(func)
print(id(func))
print(globals())
print(type(globals()))  # тип объекта словарь
f = globals()["func"]  # это наша функция определенная выше
print(f is func)  # True

print(locals())


def func():
    a = 10
    b = 10
    print(locals())


func()  # locals() - словарь с переменными функции func

import math

print(math)

print(globals())
print(type(math))  # module
print(id(math))  # math is singleton object

import math

print(id(math))

import sys

print(sys.modules)
print(sys.modules["math"])
print(id(sys.modules["math"]))  # it has same id as math

print(math.__dict__)  # math atributes and functions in math module
