from fractions import Fraction

f = Fraction(2, 3)
print(f.numerator)
print(f.denominator)


# Определение метода у класса Fractions

# Fraction.speak = lambda self, message: f"Fractions says: {message}"
# print(f.speak("Hello my friend"))

# Декоратор класса, который определяет новый метод для класса

def dec_speak(cls):
    cls.speak = lambda self, message: f"{self.__class__.__name__} says: {message}"
    return cls


Fraction = dec_speak(Fraction)
f1 = Fraction(2, 5)

print(f1.speak("Hello"))


class Person:
    pass


Person = dec_speak(Person)

p = Person()

print(p.speak("Hi, my friend Arseniy"))

from datetime import datetime, timezone


def info(self):
    results = []
    results.append(f"time: {datetime.now(timezone.utc)}")
    results.append(f"Class: {self.__class__.__name__}")
    results.append(f"id: {hex(id(self))}")
    for k, v in vars(self).items():
        results.append(f"{k}: {v}")
    return results


# Декоратор-функция принимает на вход сам класс и присваивает ей метод debug
def debug_info(cls):
    cls.debug = info
    return cls


# Декорируем класс Person
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return "Hello There"


p = Person("Arseniy", 1989)
# # Для понимания vars
# print(p.__dict__ is vars(p))
# for k, v in vars(p).items():
#   print(f"{k}: {v}")
dt = (2015, 1, 1, 12, 30, 59, 0)
print(p.debug())


# print(dir(timezone))
# print(timezone.tzname(dt))

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Speed can not esceeded top speed")
        else:
            self._speed = new_speed


favorite = Automobile("Ford", "Model T", 1908, 45)
favorite.speed = 25
print(favorite.debug())


# a <= b iff a < b or a == b
# a > b iff not(a<b) and a != b
# a >= b iff not(a<b)

def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, self.x, self.y)


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)