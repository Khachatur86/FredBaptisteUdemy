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
