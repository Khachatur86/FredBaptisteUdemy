import os

def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py.
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs.
    '''
    
    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)
    
    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")


create_module_file('test', k1=10, k2='python')

import test

test.print_values()

create_module_file('test', k1=10, k2='python', k3='cheese')

import test

test.print_values()
import sys
print("Id модуля test до удаления - ",id(test))
print("Id модуля test до удаления - ",id(sys.modules["test"]))


print('test' in sys.modules)
del sys.modules["test"]
print("Модуль test есть в sys.modules?",'test' in sys.modules) # False

import test

print("Id модуля test после удаления и повторного импорта- ",id(test))
print("Id модуля test после удаления и повторного импорта- ",id(sys.modules["test"]))

test.print_values()

create_module_file('test', k1=10, k2='python', 
                   k3='cheese', k4='parrots')

import importlib

importlib.reload(test)
print(id(test)) # Адрес не изменился!!!
test.print_values()

# 2 часть

create_module_file('test2', k1='python')

from test2 import print_values

print("test2" in globals()) # Ожидаемо вернет False
print("print_values" in globals()) # Ожидаемо вернет True

print("test2" in sys.modules) # Ожидаемо вернет True
print("print_values" in sys.modules) # Ожидаемо вернет False

print(print_values)
print_values()

# Переопределим модуль test2
create_module_file('test2', k1='python', k2='cheese')

importlib.reload(sys.modules["test2"])

print_values() # Не сработает так как нету привязки к новому объекту перезаписанному модулю, он обращается по старому адресу
print("Id объекта до переопределения", id(print_values))
print_values = sys.modules["test2"].print_values
print_values()

print("Id объекта после переопределения", id(print_values))
