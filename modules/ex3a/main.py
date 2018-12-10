import os.path
import types 
import sys
module_name = "module2"
module_file = "module1_source.py"
module_path = "."
module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)
#
# print(module_rel_file_path)
# print(module_abs_file_path)

# read source code from path
with open(module_rel_file_path, "r") as code_file:
  source_code = code_file.read()

# print(source_code)
# create a module object

mod = types.ModuleType(module_name)
# print(mod)
# print(mod.__dict__)
mod.__file__ = module_abs_file_path

# set a ref in sys.modules

sys.modules[module_name] = mod

# compile source code

code = compile(source_code, filename=module_abs_file_path, mode="exec")

# execute compiled source code

exec(code, mod.__dict__)

# DONE

mod.hello()

import module2
module2.hello()
# # При импорте модуля, компилятор проверяет на наличие имени модуля в sys.modules, в случае если он его там находит - то выдает его результат и выполняет его. Если имени не оказалось в нем, то выдает ошибку.
for k, v in sys.modules.items():
  print(f"Key = {k}. Value = {v}")
print(type(sys.modules))