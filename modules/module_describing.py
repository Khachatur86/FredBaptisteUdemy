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

print(math.__dict__)  # math attributes and functions in math module

import calendar

# print(calendar)
# print("---Calendar---")
# for k,v in calendar.__dict__.items():
#     print(f"{k}:{v}")

import types

print(isinstance(math, types.ModuleType))

from types import ModuleType

mod = ModuleType("test", "This is a test module")
print(isinstance(mod, ModuleType))

print(mod.__dict__)
mod.pi = 3.14
print(mod.__dict__)

mod.hello = lambda: "Hello"
print(mod.hello)
hello = mod.hello
print("mod" in globals())
print("hello" in globals())
from collections import namedtuple
mod.Point = namedtuple("Point", "x y")
p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)
print(p1)
print(p2)
print(dir(mod))
PT = getattr(mod, "Point")
print(PT(20, 30))
PT = mod.__dict__["Point"]
print(PT(10, 34))
