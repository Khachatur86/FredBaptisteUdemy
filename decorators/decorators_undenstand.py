def outer(fn):


  from functools import wraps
  @wraps(fn)
  def inner(*args, **kwargs):
    print("inner running")
    print("hex id fn (add)", hex(id(fn)))
    print("inner hex id", hex(id(inner)))
    return fn(*args, **kwargs)
  return inner

# @outer
def add(a, b):
  return a + b

add = outer(add)
print("hex id add", hex(id(add)))


print(add(4, 5))
