# First decorator

def dec_1(fn):
  def inner():
    print("Running dec_1")
    return fn()
  return inner

# Second decorator

def dec_2(fn):
  def inner():
    print("Running dec_2")
    return fn()
  return inner

# My_func decorated by dec_1 and dec_2

# my_func = dec_1(dec_2(my_func))
@dec_1
@dec_2
def my_func1():
  print("Running my_func1()")

# my_func = dec_1(dec_2(my_func))

my_func1()
# Decorators in other order
@dec_2
@dec_1
def my_func2():
  print("Running my_func2()")

my_func2()
