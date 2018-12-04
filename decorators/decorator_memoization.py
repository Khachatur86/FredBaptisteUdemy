# Функция Фиббоначчи

# def fib(n):
#   print(f"Calculating fib({n})")
#   return 1 if n < 3 else fib(n-1) + fib(n-2)

# Реализация мемоизации для функции Фибоначчи классами

# class Fib:

#   def __init__(self):
#     # Словарь промежуточных вычислений {ключ (аргумент): результат вычисления}
#     self.cache = {1: 1, 2: 2}

#   def fib(self, n):
#     if n not in self.cache:
#     # Если n нету в словаре, промежуточных
#     # вычислений, то начать вычисления
#       print(f"Вычисление функции fib({n})")
#       self.cache[n] = self.fib(n-1) + self.fib(n-2)
#     return self.cache[n]

# f = Fib()

# f.fib(10)


# Реализация того же самого, с использованием замыкания

# def fib():
#   cache = {1: 1, 2: 1} # Тот же словарь

#   def calc_fib(n):
#     if n not in cache:
#       print(f"Вычисление функции fib({n})")
#       cache[n] = calc_fib(n-1) + calc_fib(n-2)
#     return cache[n]
#   return calc_fib

# f = fib()
# print(f(10))

# Создадим функцию мемоизации для вычисления функции fib
def fib(n):
  print(f"Calculating fib({n})")
  return 1 if n < 3 else fib(n-1) + fib(n-2)

# Декоратор memoize позволяет не выполнять те вычисления, которые уже были сделаны.
# Промежуточные вычисления сохраняются в специально созданном словаре.
# И при вычислениях, которые уже были сделаны, мы обращаемся к словарю.

def memoize(fn):
  cache = dict()
  def inner(n):
    if n not in cache:
      cache[n] = fn(n)
    return cache[n]
  return inner

@memoize
def fib(n):
  print(f"Calculating fib({n})")
  return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)