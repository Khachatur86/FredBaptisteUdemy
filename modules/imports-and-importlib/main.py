import sys
import collections
print(sys)
print(collections)

mod_name = "math"
# import mod_name # не отрабатывает так как в sys.modules отсутствует модуль с именем "mod_name" а не - math
import importlib

print(importlib)

# importlib.import_module(mod_name) # в таком случае мы сможем импортировать модуль math
# print("math" in sys.modules, mod_name in sys.modules)
print("fractions" in sys.modules)
import fractions
print("fractions" in sys.modules)

# print(math.sqrt(2)) 

print("math" in globals()) # нужно math добавить в globals

import math # 1 способ
# math = importlib.import_module(mod_name) # 2 способ

print("math" in globals())

# print(id(math))
# print(id(sys.modules["math"]))
math = importlib.import_module("math")
print(id(math))
print(id(sys.modules["math"]))

# finders
# loaders
# finder + loader = imporet

import math
import fractions
print(fractions.__spec__)
print(sys.meta_path)
print(math.__spec__)
print(importlib.util.find_spec("math"))
print(importlib.util.find_spec("decimal"))
# Напишем свой собвственный модуль непосредственное здесь
with open("module1.py", "w") as code_file:
  code_file.write("print('running module1.py')\n")
  code_file.write("a=100\n")

print(importlib.util.find_spec("module1"))
import module1
print("module1" in globals())
print(module1.a)

import os

ext_module_path = os.environ["HOME"]
print(os.environ)
print(ext_module_path)
file_abs_path = os.path.join(ext_module_path, "module2.py")
with open(file_abs_path, "w") as code_file:
  code_file.write("print('running module2.py...')\n")
  code_file.write("x='python'\n")

print(sys.path)
sys.path.append(ext_module_path)
print(sys.path)
print(importlib.util.find_spec("module2"))
# import module2
# print("++++++++++++++++++++++++++++++++++")
# for k, v in sys.modules.items():
  # print(f"{k}:{v}")
# print(sys.modules)