from collections import namedtuple
Point2D = namedtuple("Point2D", "x y")
pt = Point2D(10, 20)
print(pt)

# pt.x = 19 не будет работать
print(pt[0])

# Можно изменить и сохранить в ту же переменную, создасться новый экземпляр, который ссылается на новую ячейку памяти
print(id(pt)) # Одно значение
pt = Point2D(100, pt.y)
print(id(pt)) # Другое значение значение

Stock = namedtuple("Stock", "symbol year month day open high low close")
djia = Stock("Djia", 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)
print("Здесь id до переопределения:", hex(id(djia)))
djia = Stock(djia.symbol, djia.year, djia.month,
             djia.day, djia.open,
             djia.high, djia.low, 1000)
print(djia)
print("Здесь id после переопределения:", hex(id(djia)))

*values, close = djia

print(values)
values.append(26_393)
print(values)
djia = Stock(*values)
print("Сам объект djia",djia)
values = djia[:7] # Вернет tuple объекта djia с нулевого по шестой элемент
print("Представлен values:", values)

djia = Stock(*(values + (100, ))) # Чтобы не распаковывать values, можно воспользоваться методом _make {djia = Stock._make(values + (100, ))}
print(djia)

# Можно воспользоваться методом _replace объекта namedtuple
djia = djia._replace(year=2015) # Поменяли поле year объекта djia
# При этом меняется id объекта. Нужно хорошо понимать, что мы создаем новый объект и сохраняем его в ту же переменную. НО ЭТО НОВЫЙ ОБЪЕКТ, КОТОРЫЙ ССЫЛАЕТСЯ НА ДРУГУЮ ЯЧЕЙКУ ПАМЯТИ
print("После изменения поля year", djia )

print("Поля класса Point2D",Point2D._fields)

# Расширение класса Point2D до Point3D

# 1 вариант

Point3D = namedtuple("Point3D", Point2D._fields + ("z",))
print("Поля класса Point3D после расширения Point2D", Point3D._fields)


