

import sys
# print(sys)
# print(sys.prefix)
# print(sys.path)

print("=========================================")
print(f"Running main.py - module name {__name__}")
import example1.module1
print(example1.module1)
example1.module1.pprint_dict("main.globals", globals())
print(sys.path)
print(sys.modules['example1.module1'])

del globals()["example1"]

import example1.module1 # после удаления модуля, нужно заново его импортировать

example1.module1.pprint_dict("main.globals", globals()) # после удаления функция не работает
print("=========================================")

