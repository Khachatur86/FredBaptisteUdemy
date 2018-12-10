

import sys
# print(sys)
# print(sys.prefix)
# print(sys.path)

print("=========================================")
print(f"Running main.py - module name {__name__}")
import module1
print(module1)
# module1.pprint_dict("main.globals", globals())
print(sys.path)
print(sys.modules['module1'])

del globals()["module1"]

import module1 # после удаления модуля, нужно заново его импортировать
print(globals())
module1.pprint_dict("globals", globals()) # после удаления функция не работает
print("=========================================")

# print(sys.modules)
