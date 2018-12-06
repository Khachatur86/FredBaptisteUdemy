class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


from collections import namedtuple

# Создание класса с помощью namedtuple
Point2D = namedtuple("Point2D", ["x", "y"])
# переменная Point2D указывает на класс Point2D
pt1 = Point2D(10, 20)
pt3d_1 = Point3D(10, 20, 30)
print(type(Point2D))
print(pt1)
print(pt3d_1)
# переменная Pt2D указывает на класс Point2D, переменную можно назвать как угодно.
# имя класса в скобках идет первым
pt2D = namedtuple("Point2D", ("x", "y"))

pt2 = pt2D(y=10, x=30)
# Можно также обращаться к переменным путем точечной нотации
print(pt2.x)
# pt2.x = 45 нельзя менять, так как неизменяемый объект
print(isinstance(pt2, tuple))
# print(tuple.__eq__)
a = (10, 20)
b = (10, 20)

print("Ссылаются ли переменные на одну память?", a is b)
print("Равны ли переменные?", a == b)

pt_1 = Point2D(10, 20)
pt_2 = Point2D(10, 20)

# При проделывании того же с классами, поведение будет разное
print("Ссылаются ли переменные, созданные namedtuple на одну память ?", pt_1 is pt_2)
print("Равны ли переменные, созданные namedtuple ?", pt_1 == pt_2)

pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

print("Ссылаются ли переменные, созданные через класс, на одну память ?", pt3d_1 is pt3d_2)
print("Равны ли переменные, созданные через класс ?", pt3d_1 == pt3d_2)


# Для того чтобы исправить данное недоразумение нужно прописать соответствующий дандерметод __eq__:

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__} (x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


# То же самое, после определения метода __eq__
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

print("Ссылаются ли переменные, созданные через класс, на одну память ?", pt3d_1 is pt3d_2)
print("Равны ли переменные, созданные через класс ?", pt3d_1 == pt3d_2)

print(pt3d_1)

pt1 = Point2D(10, 40)
pt2 = Point3D(10, 30, 56)
print(max(pt1))  # выведет 40, так как pt1 - это кортеж


# print(max(pt2)) # будет ошибка, так как pt2 - это класс

#  a.b = a.x b.x + a.y + b.y + a.z b.z - произведение векторов
def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


print(dot_product_3d(pt3d_1, pt3d_2))
# Реализация метода для tuple - ов
a = (1, 4)
b = (3, 8)
print("ZIP",tuple(zip(a, b)))
print([e[0] * e[1] for e in tuple(zip(a, b))])
# print((e[0] * e[1] for e in tuple(zip(a, b))))
print(sum([e[0] * e[1] for e in tuple(zip(a, b))]))


def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))


a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))

print([e[0] * e[1] for e in zip(a, b)])

print(sum([e[0] * e[1] for e in zip(a, b)]))
print(dot_product(a, b))

Vector3D = namedtuple("Vector3D", "x, y, z")

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)

print(v1)
print(v2)
print(dot_product(v1, v2))

print(tuple(v1))
print(tuple(v2))

# Определение класса окружности с использованием namedtuple

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])

circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x=10, center_y=20, radius=100)

print(circle_1)
print(circle_2)

Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)

for index, item in enumerate(djia):
    print(f"{index}:{item}")

symbol, year, month, day, *ignored, close = djia

print(f"symbol={symbol}, year={year}, month={month}, day={day}, close={close}")
print("Выведем на печать ignored", ignored)
print(dir(djia))
print(djia._asdict())

for item in djia._asdict().items():
    print(f"{item[0]} = {item[1]}")

# Person = namedtuple("Person", "name age _ssn") # переменная -атрибут не должна начинаться с знака нижнего подчеркивания
# Но так работает
Person = namedtuple("Person", "name age _ssn _3", rename=True)
print(Person._fields)
print(Stock._fields)
print("Ниже динамически созданный класс Stock")
print(Stock._source)
