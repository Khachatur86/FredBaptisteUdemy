# # Доступ к переменной value из module1: нужно импортировать сам модуль и через точку обратиться к значению value
# import pack1 # Package Обязательно нужно добавлять файл с именем __init__.py
#
# import module1 # Модуль


# print(pack1)
# print("pack1.__file__ - ",pack1.__file__)
# print("module1.__file__ - ",module1.__file__)
# print("pack1.__package__ - ",pack1.__package__)
# print("module1.__package__ - ",module1.__package__) # "" так как module1 не package
# # print(module1.__path__) # AttributeError - __path__ only for packages
# print("pack1.__path__ - ",pack1.__path__) # возвращает путь, где находится сам package
# print("type(pack1) - ",type(pack1))

# # Сначала закомментировать выше и выполнить файл
# import pack1.pack1_1


# # # Подгружается сначала pack1, а потом pack1_1
# print(pack1.pack1_1.value)
# import sys


# print('"pack1_1" in globals() - ',"pack1_1" in globals())
# print('"pack1_1" in sys.modules - ',"pack1_1" in sys.modules)

# print('"pack1.pack1_1" in globals() - ',"pack1.pack1_1" in globals())
# print('"pack1.pack1_1" in sys.modules - ',"pack1.pack1_1" in sys.modules)
# print('"pack1" in globals() - ',"pack1" in globals())

# # Сначала закомментировать выше и выполнить файл
# from pack1 import pack1_1 # таким образом мы добавили pack1_1 в область глобальных переменных
# import sys
#
# print('"pack1" in sys.modules - ',"pack1" in sys.modules)
# print('"pack1_1" in globals() - ',"pack1_1" in globals())
#
# print(f"id(pack1_1) == id(sys.modules['pack1.pack1_1']) - {id(pack1_1) == id(sys.modules['pack1.pack1_1'])}")
# # Это одинаковые объекты

# Сначала закомментировать выше и выполнить файл
# import sys
# import pack1.pack1_1.module1_1a
# # executing pack1... - это строка из init pack1
# # executing pack1_1... - это строка из init pack1_1
# # executing module1_1a... - это из самого модуля module1_1
# # sys.modules
# print("'pack1' in sys.modules - ",'pack1' in sys.modules)
# print("'pack1.pack1_1' in sys.modules - ",'pack1.pack1_1' in sys.modules)
# print("'pack1.pack1_1.module1_1a' in sys.modules - ",'pack1.pack1_1.module1_1a' in sys.modules)
# # Globals
# print("'pack1' in globals() - ",'pack1' in globals())
# print("'pack1.pack1_1' in globals() - ",'pack1.pack1_1' in globals())
# print("'pack1.pack1_1.module1_1a' in globals() - ",'pack1.pack1_1.module1_1a' in globals())

# Сначала закомментировать выше и выполнить файл

import pack1.pack1_1
# # executing pack1...
# # executing pack1_1...
import sys
# # sys.modules
print("'pack1.pack1_1.module1_1a' in sys.modules - ",'pack1.pack1_1.module1_1a' in sys.modules)
print("'pack1.pack1_1.module1_1b' in sys.modules - ",'pack1.pack1_1.module1_1b' in sys.modules)

# # globals()

print("'pack1.pack1_1.module1_1a' in globals() - ",'pack1.pack1_1.module1_1a' in globals())
print("'pack1.pack1_1.module1_1b' in globals() - ",'pack1.pack1_1.module1_1b' in globals())

# # __file__
# print("pack1.pack1_1.__file__ - ",pack1.pack1_1.__file__)
# print("pack1.pack1_1.module1_1a.__file__ - ",pack1.pack1_1.module1_1a.__file__)

# Сначала закомментировать выше и выполнить файл

# import pack1 # в файле init добавлены строки импорта соответствующих модулей. Поэтому при импорте pack1
# выполняются строчки кода, записанные в init
# executing pack1_1...
# executing module1_1a...
# executing module1_1b...
# executing pack1...

# Проверка на вхождение в sys.modules соответствующих строк с именами модулей 1a и 1b вернет значение True