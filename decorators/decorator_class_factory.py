def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print(f"Декорированная функция вызвана с параметрами a = {a} b = {b}")
            return fn(*args, **kwargs)

        return inner

    return dec


@my_dec(10, 20)
def my_func(s):
    print(f"World {s}")


my_func("Hello")


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f"Декорированная функция вызвана с параметрами a = {self.a} b = {self.b}")
            return fn(*args, **kwargs)

        return inner


d = MyClass(10, 40)
d(10)


@MyClass(10, 40)
def my_func1(s):
    print(f"World {s}")


my_func1(100)