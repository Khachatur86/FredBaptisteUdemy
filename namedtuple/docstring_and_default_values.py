from collections import namedtuple
Point2D = namedtuple("Point2D", "x y")
print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)

# print(help(Point2D))

# Изменим докстринг
Point2D.__doc__ = "2D график координат"
Point2D.x.__doc__ = "Координата x"
Point2D.y.__doc__ = "Координата y"
print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")
print(Vector2D._fields)
v1 = Vector2D(0, 0, 10, 10, 0, 0)
print(v1._fields)
# Создадим прототип, начальный вектор

vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
print(vector_zero)
v2 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)
print(v2)

def func(a, b=10, c=20):
  print(a, b, c)

print("Дефолтные значения нашей функции",func.__defaults__)

# Переопределим явным образом дефолтные значения

func.__defaults__ = (100, 200, 300)

func()

print(Vector2D.__new__.__defaults__)

Vector2D.__new__.__defaults__ = (45, 0, 4, 56)
# Мы обращаемся к методу __new__ класса Vector2D и вызываем у него дефолтные значения переменных -
print(Vector2D.__new__.__defaults__)

v3 = Vector2D(10, 20)
print(v3)