# With dictionary
def outer1():
  c = {}
  print("from outer",hex(id(c)))
  def inner():
    # nonlocal c
    for n in range(10):
      print("From inner",hex(id(c)))
      c[n] = "Deg"
    return c
  return inner

print(outer1()())

# With list
def outer2():
  c = 5
  print("from outer",hex(id(c)))
  def inner():
    nonlocal c
    for n in range(10):
      print("From inner",hex(id(c)))
      c = 89
    return c
  return inner

print(outer2()())
