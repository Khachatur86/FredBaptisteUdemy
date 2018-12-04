# def timed(fn: "function"):
#   from time import perf_counter

#   def inner(*args, **kwargs):
#     start = perf_counter()
#     result = fn(*args, **kwargs)
#     end = perf_counter()
#     elapsed = end - start
#     print(f"Run time: {elapsed:.6f}")
#     return result
#   return inner

# def calc_fib_recurse(n):
#   return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

# # @timed
# def fib(n):
#   return calc_fib_recurse(n)

# fib = timed(fib)

# print(fib(5))

# def timed(fn: "function"):
#   from time import perf_counter

#   def inner(*args, **kwargs):
#     total_elapsed = 0
#     for i in range(10): # Надо передать число 10 как параметр. 

#       start = perf_counter()
#       result = fn(*args, **kwargs)
#       end = perf_counter()
#       total_elapsed += (end- start)
#     avg_run_time = total_elapsed / 10
#     print(f"Average Run time: {avg_run_time:.6f}")
#     return result
#   return inner

# def calc_fib_recurse(n):
#   return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

# @timed
# def fib(n):
#   return calc_fib_recurse(n)

# # fib = timed(fib)

# print(fib(5))

# Создание фабрики декораторов 

# def dec(fn):
#   print("running dec")

#   def inner(*args, **kwargs):
#     print("Running inner")
#     return fn(*args, **kwargs)
#   return inner

# @dec
# def my_func():
#   print("My_func running")
# my_func()

# def dec_factory():
#   print("running dec_factory")

#   def dec(fn):
#     print("running dec")

#     def inner(*args, **kwargs):
#       print("running inner")
#       return fn(*args, **kwargs)

#     return inner
#   return dec

# Вызвав функцию dec_factory, мы вернем сам декоратор dec "()" - это вызов функции
# dec = dec_factory()

# # @dec
# def my_func():
#   print("My_func running")

# my_func = dec(my_func)
# my_func()

# То же самое - иная запись

# @dec_factory() # возвращает декоратора dec
# def my_func1():
#   print("running my_func1")

# my_func1()

# Передача параметров в фабрику декораторов


# def dec_factory_pass_parameters(a, b):
#   print("running dec_factory")

#   def dec(fn):
#     print("running dec")

#     def inner(*args, **kwargs):
#       print("running inner")
#       print(f"Parameters a={a}, b={b}")
#       return fn(*args, **kwargs)

#     return inner
#   return dec

# @dec_factory_pass_parameters(10, 30)
# def my_func2():
#   print("my_func2 running")

# print(my_func2.__closure__)
# print(hex(id(10)))
# print(hex(id(30)))
# print(my_func2.__code__.co_freevars)
# Передача параметров в замыкание посредством создания фабрики декораторов
def dec_factory(reps):
    def timed(fn: "function"):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):  # Надо передать число 10 как параметр.
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print(f"Average Run time: {avg_run_time:.6f} {reps} times")
            return result

        return inner

    return timed


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 2) + calc_fib_recurse(n - 1)


@dec_factory(8)
def fib(n):
    return calc_fib_recurse(n)


fib(9)